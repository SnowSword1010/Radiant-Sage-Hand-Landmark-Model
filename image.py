import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# function that takes static image as input and sends it 
# to mediapipe to return coordinates of 21 hand landmarks
def get_coordinates(img):
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=2,
        min_detection_confidence=0.5) as hands:
        image = cv2.flip(img, 1)
        # Convert the BGR image to RGB before processing.
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Print handedness and draw hand landmarks on the image.
        print('Handedness:', results.multi_handedness)
        if not results.multi_hand_landmarks:
            return
        image_height, image_width, _ = image.shape
        print(image_height)
        print(image_width)
        print(_)
        annotated_image = image.copy()
        coordinates = []
        print("MULTI HAND LANDMARKS: ", len(results.multi_hand_landmarks))
        for idx, hand_landmark in enumerate(results.multi_hand_landmarks):
            print("INDEXX: ", idx)
            norm_coordinates = hand_landmark.landmark
            for norm_cord in norm_coordinates:
                # getting actual coordinates from normalised coordinates by multiplying with image_width and image_height
                coordinates.append([norm_cord.x * image_width, norm_cord.y * image_height])
        return coordinates