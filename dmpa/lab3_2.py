import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('C:/opencv/bruno.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the gradient in the X and Y direction
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Calculate the gradient length
gradient_length = np.sqrt(np.square(sobel_x) + np.square(sobel_y))

# Calculate the gradient angle
gradient_angle = np.arctan2(sobel_y, sobel_x)

# Display the two matrices
print('Gradient Length Matrix:')
print(gradient_length)
print('Gradient Angle Matrix:')
print(gradient_angle)

# Display the result
plt.imshow(gradient_length, cmap='gray')
plt.show()