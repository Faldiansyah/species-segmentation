import cv2
import numpy as np

species = cv2.imread('lebah.jpg')
species = cv2.cvtColor(species, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(species, cv2.COLOR_RGB2HSV)
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)
mask = cv2.inRange(hsv, light_orange, dark_orange)
result = cv2.bitwise_and(species, species, mask=mask)

cv2.imwrite("hasil.jpeg", species)
cv2.imwrite("hasil2.jpeg", hsv)
cv2.imwrite("hasil3.jpeg", mask)
cv2.imwrite("hasil4.jpeg", result)
print("Berhasil Memproses Citra")