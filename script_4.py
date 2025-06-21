# ---------------------------------------------------------
#   Name : Randula R.D.
#   Reg No: EG/2020/4149
#   Take Home Assignment 1
#   Question 4
# ---------------------------------------------------------
# Import computer vision and array processing packages
import cv2
import numpy as np

# Load the input image in color mode
image = cv2.imread('C:/Users/busin/Desktop/MY/SEM 7/Com vision/Computer Vision and Image Processing Take Home Assignment 1/data/sample.jpg', cv2.IMREAD_COLOR)

# Set different grid dimensions for pixelation effect
block_sizes = [3, 5, 7]

# Function to apply pixelation effect using mean color blocks
def process_image(image, block_size):
    processed_image = np.copy(image)

    # Process image in block_size increments
    for y in range(0, image.shape[0], block_size):
        for x in range(0, image.shape[1], block_size):
            # Extract current image block
            roi = image[y:y+block_size, x:x+block_size]
            # Compute average color of the block
            mean_color = np.mean(roi, axis=(0, 1))
            # Apply uniform color to the entire block
            processed_image[y:y+block_size, x:x+block_size] = mean_color

    return processed_image

# Generate pixelated versions for all block sizes
processed_images = [process_image(image, size) for size in block_sizes]

# Create window for source image display
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original Image', image)


# Display each processed result in separate windows
for i, processed_image in enumerate(processed_images):
    window_name = f'Processed Image {block_sizes[i]}x{block_sizes[i]}'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 640, 480)
    cv2.imshow(window_name, processed_image)

# Keep windows open until keypress
cv2.waitKey(0)
cv2.destroyAllWindows()
