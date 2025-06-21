# ---------------------------------------------------------
#   Name : Randula R.D.
#   Reg No: EG/2020/4149
#   Take Home Assignment 1
#   Question 3
# ---------------------------------------------------------
# Load OpenCV library for image processing
import cv2

# Load the source image from file path
image = cv2.imread('C:/Users/busin/Desktop/MY/SEM 7/Com vision/Computer Vision and Image Processing Take Home Assignment 1/data/sample.jpg')

# Create 45 degree rotation transformation
rows, cols = image.shape[:2]
rotation_matrix_45 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
rotated_image_45 = cv2.warpAffine(image, rotation_matrix_45, (cols, rows))

# Create 90 degree rotation transformation 
rotation_matrix_90 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
rotated_image_90 = cv2.warpAffine(image, rotation_matrix_90, (cols, rows))

# Define window names for display
windows = ['Original Image', 'Rotated Image 45', 'Rotated Image 90']

# Configure display windows
for window in windows:
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window, 640, 480)

# Show original and transformed images
cv2.imshow(windows[0], image)
cv2.imshow(windows[1], rotated_image_45)
cv2.imshow(windows[2], rotated_image_90)

# Maintain display until user input
cv2.waitKey(0)
cv2.destroyAllWindows()
