import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# Load the image
path = 'download (1).jpeg'
image = img.imread(path)

height, width = image.shape[:2]

# Initialize arrays for mirrored images
horizontal_vertical = np.zeros_like(image)  # To hold the result of both transformations

# Create both horizontal and vertical mirror images simultaneously
for y in range(height):
    for x in range(width):
        horizontal_vertical[y, x] = image[y, width - 1 - x]  # Horizontal flip
        horizontal_vertical[height - 1 - y, x] = image[y, x]  # Vertical flip

# Plot the original and mirrored images
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(horizontal_vertical)
plt.title("Combined Horizontal and Vertical Mirror")

plt.show()
