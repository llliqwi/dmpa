import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/opencv/bruno.jpg", 0)

# Calculate gradient values
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
magnitude = np.sqrt(np.square(sobelx) + np.square(sobely))

# Normalize gradient values
magnitude = (magnitude / magnitude.max()) * 255

# Apply double threshold
high_threshold = 0.3 * 255
low_threshold = 0.1 * 255
double_threshold = np.zeros_like(magnitude)
double_threshold[(magnitude >= high_threshold)] = 255
double_threshold[(magnitude <= low_threshold)] = 0
double_threshold[(magnitude > low_threshold) & (magnitude < high_threshold)] = 128

# Display the result
cv2.imshow("Double Threshold", double_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()