import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('weeviled-rice.jpg') 
original = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Thresholding
_, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)

# Edge Detection
edges = cv2.Canny(thresh, 30, 150)

# Find contours of the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask for the thresholded regions
mask = np.zeros_like(img)

# Draw contours on the mask
cv2.drawContours(mask, contours, -1, (0, 0, 255), 2)  # Highlight contours in red

# Apply the mask onto the original image
result = cv2.bitwise_or(original, mask)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(mask)
plt.title('Thresholded Weevils')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title('Highlighted Weevils')
plt.axis('off')

plt.tight_layout()
plt.show()
