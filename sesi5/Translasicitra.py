import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi (image, shiftx, shifty):

    imgTranslasi = np.roll(image, shift=shifty, axis=0)  # Geser vertikal
    imgTranslasi = np.roll(imgTranslasi, shift=shiftx, axis=1)  # Geser horizontal

    # mengisi bagian yang kosong dengan warna hitam (0)
    if shifty > 0:
        imgTranslasi[shifty, :] = 0 #Bagian atas jika geser ke bawah
    elif shifty < 0:
        imgTranslasi[shifty:, :] = 0 # Bagian bawah jika geser ke atas
    if shiftyx > 0:
        imgTranslasi[ :, :shiftx] = 0 # bagian kiri jika geser ke kanan
    elif shiftx < 0:
        imgTranslasi[:, shiftx:] = 0 #Bagian kanan jika geser ke kiri


    return imgTranslasi

image = img. imread("download (1).jpeg")

imgResult = Translasi(image, shiftx =50, shifty=-300)

plt. figure(figsize=(10,10))
plt. subplot(2,1,1)
plt. imshow(image)
plt. subplot(2,1,2)
plt. imshow(imgResult)
plt. imshow()