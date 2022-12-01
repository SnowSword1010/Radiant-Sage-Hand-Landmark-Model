import coordinates
import os
from dotenv import load_dotenv

# LOADING ENVIRONMENT VARIABLES FROM .env FILE
load_dotenv()
# loading IMG_PATH env variable
img_path = os.getenv('IMG_PATH')
# returns the coordinates of mediapipe hand landmarks
coordinates.get_coordinates(img_path)