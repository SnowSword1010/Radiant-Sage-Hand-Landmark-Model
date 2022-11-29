import cv2
import mediapipe

# function to mark coordiates on an input image
def mark_coordinates(image, coordinates):
    drawingModule = mediapipe.solutions.drawing_utils
    handsModule = mediapipe.solutions.hands
    # img_path = r'/home/mayank/Downloads/GettyImages-77937874-9ed4b0b.jpg'
    with handsModule.Hands(static_image_mode=True) as hands:
        # image = cv2.imread(img_path)
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                drawingModule.draw_landmarks(image, handLandmarks, handsModule.HAND_CONNECTIONS)

        cv2.imshow('Test image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()