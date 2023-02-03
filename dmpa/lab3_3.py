import cv2
import numpy as np

# read image
img = cv2.imread('C:/opencv/bruno.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# perform gradient calculation using Sobel operator
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# calculate gradient magnitude and direction
magnitude = np.sqrt(np.square(sobelx) + np.square(sobely))
direction = np.arctan2(sobely, sobelx)

# perform non-maximum suppression
def non_maximum_suppression(magnitude, direction):
    M, N = magnitude.shape
    result = np.zeros((M, N), dtype=np.float32)
    angle = direction * 180. / np.pi
    angle[angle < 0] += 180

    for i in range(1, M - 1):
        for j in range(1, N - 1):
            try:
                q = 255
                r = 255

                # 0 degrees
                if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                    q = magnitude[i, j + 1]
                    r = magnitude[i, j - 1]
                # 45 degrees
                elif (22.5 <= angle[i, j] < 67.5):
                    q = magnitude[i + 1, j - 1]
                    r = magnitude[i - 1, j + 1]
                # 90 degrees
                elif (67.5 <= angle[i, j] < 112.5):
                    q = magnitude[i + 1, j]
                    r = magnitude[i - 1, j]
                # 135 degrees
                elif (112.5 <= angle[i, j] < 157.5):
                    q = magnitude[i - 1, j - 1]
                    r = magnitude[i + 1, j + 1]

                if (magnitude[i, j] >= q) and (magnitude[i, j] >= r):
                    result[i, j] = magnitude[i, j]
                else:
                    result[i, j] = 0
            except IndexError as e:
                pass

    return result

suppressed_magnitude = non_maximum_suppression(magnitude, direction)

# display the results
cv2.imshow('Original Image', img)
cv2.imshow('Gradient Magnitude', magnitude)
cv2.imshow('Suppressed Magnitude', suppressed_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()