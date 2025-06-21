# ---------------------------------------------------------
#   Name : Randula R.D.
#   Reg No: EG/2020/4149
#   Take Home Assignment 1
#   Question 2
# ---------------------------------------------------------
# Import computer vision and numerical processing packages
import cv2
import numpy as np

# Load the input image from specified path
image = cv2.imread('C:/Users/busin/Desktop/MY/SEM 7/Com vision/Computer Vision and Image Processing Take Home Assignment 1/data/sample.jpg')

# Initialize display configuration
image_windows = 'Original Image', '3x3 Average', '10x10 Average', '20x20 Average'
for window in image_windows:
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window, 640, 480)
processed_image = np.copy(image)

# Create smoothing function with 3x3 kernel
def average_3x3():
    global processed_image
    processed_image = cv2.blur(image, (3, 3))
    cv2.imshow(image_windows[1], processed_image)

# Create smoothing function with 10x10 kernel
def average_10x10():
    global processed_image
    processed_image = cv2.blur(image, (10, 10))
    cv2.imshow(image_windows[2], processed_image)

# Create smoothing function with 20x20 kernel
def average_20x20():
    global processed_image
    processed_image = cv2.blur(image, (20, 20))
    cv2.imshow(image_windows[3], processed_image)

# Show all image processing results
cv2.imshow(image_windows[0], image)
average_3x3()
average_10x10()
average_20x20()

# Keep windows open until keypress
cv2.waitKey(0)
cv2.destroyAllWindows()
