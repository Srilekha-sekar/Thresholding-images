import cv2
import numpy as np
image1 = cv2.imread('input.jpg')

# Save the input image
cv2.imwrite('input_thresholded.jpg', image1)

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image to grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# The window showing output images
# with the corresponding thresholding
# techniques applied to the input images
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

# Python program to threshold an image and save it

# Organizing imports
import cv2
import numpy as np

# Path to input image is specified and
# the image is loaded with imread command
image1 = cv2.imread('input.jpg')

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image to grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Applying thresholding technique
ret, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

# Specify the file path where you want to save the thresholded image
output_file_path = 'thresholded_image.jpg'

# Save the thresholded image to the specified file path
cv2.imwrite(output_file_path, thresh)

print(f'Thresholded image saved to {output_file_path}')
