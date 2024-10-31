import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)  # Increase height
    new_width = int(width * factor)    # Increase width
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            # Calculate original pixel positions, ensuring they do not exceed original dimensions
            ori_y = int(y / factor)
            ori_x = int(x / factor)
            
            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)

            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom

# Load the original image
image = img.imread('download (1).jpeg')
skala = 0.5  # Zoom out by a factor of 0.5

# Perform zoom-out
imgZoom = zoomMinus(image, skala)

# Save the zoomed out image with a new filename
img.imwrite("zoomed_out_image.jpeg", imgZoom)

# Display original and zoomed images
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(imgZoom)
plt.title(f"Zoomed Out Image (x{1/skala})")

plt.show()
