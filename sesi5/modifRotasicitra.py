import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)
    
    height, width = image.shape[:2]
    max_dim = int(np.sqrt(height**2 + width**2))  # Bounding box size for rotation
    outputImage = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)
    
    # Rotation around the top-left corner (0,0)
    for y in range(height):
        for x in range(width):
            # Rotate using (0,0) as the pivot
            newX = int(cos_deg * x - sin_deg * y)
            newY = int(sin_deg * x + cos_deg * y)

            # Translate rotated coordinates to the new image
            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                outputImage[newY, newX] = image[y, x]

    return outputImage

image = img.imread('download (1).jpeg')
rotated_image = rotateImage(image, 45)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title("Rotated 45 Degrees (Top-Left Pivot)")

plt.show()
