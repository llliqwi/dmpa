import cv2
import numpy as np

def process_image(file_path):
    # Read the image
    img = cv2.imread(file_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Show the images
    cv2.imshow('Original', img)
    cv2.imshow('Blurred', blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function with the file path
process_image('C:/opencv/bruno.jpg')