# ---------------------------------------------------------
#   Name : Randula R.D.
#   Reg No: EG/2020/4149
#   Take Home Assignment 1
#   Question 1
# ---------------------------------------------------------
# Load necessary image processing packages
import cv2
import numpy as np

# Load target image in grayscale mode
image = cv2.imread('C:/Users/busin/Desktop/MY/SEM 7/Com vision/Computer Vision and Image Processing Take Home Assignment 1/data/sample.jpg', cv2.IMREAD_GRAYSCALE)

# Configure display window properties
window_name = 'Intensity Adjustment Display'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

# Initialize intensity control parameters
max_intensity = 8  
initial_intensity = 3  
current_intensity = initial_intensity


# Callback function for intensity adjustment
def update_intensity(value):
    global current_intensity
    current_intensity = 2 ** (8-value)

    # Reduce color depth based on current intensity
    img_reduced = np.uint8(np.floor(np.double(image) / (current_intensity)))

    # Enhance contrast through normalization
    updated_image = cv2.normalize(img_reduced, None, 0, 255, norm_type=cv2.NORM_MINMAX)

    # Refresh display with modified image
    cv2.imshow(window_name, updated_image)

# Add interactive intensity control slider
cv2.createTrackbar('Intensity', window_name, initial_intensity, max_intensity, update_intensity)

# Show original image on startup
cv2.imshow(window_name, image)

# Maintain display until user input
cv2.waitKey(0)
cv2.destroyAllWindows()
