# import sys
# print(sys.executable)

# import os
# print(os.getcwd())

# import cv2
# import numpy as np
# import matplotlib
# print(cv2.__version__)

# import cv2
# img = cv2.imread('images/test_image.jpg')
# cv2.imshow('It is good image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(type(img))
# print (img.shape)

# print ('Height of Image:', int(img.shape[0]), 'pixels')
# print ('Width of Image: ', int(img.shape[1]), 'pixels')

# cv2.imwrite('output.jpg', img)
# cv2.imwrite('output.png', img)

# import matplotlib.pyplot as plt
# plt.imshow(img)
# plt.imshow(img[:,:,::-1])

# rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(rgb_image)

# import cv2
# img = cv2.imread('beautiful-shot-lake-middle-mountainous-scenery.jpg')
# img[300:400,100:700,:] = 200
# plt.imshow(img[...,::-1])

# img[100:500,200:400,:] = (0, 0, 255)
# plt.imshow(img[...,::-1])

# import cv2
# img = cv2.imread('images/test_image.jpg')
# cv2.imshow('Original', img)
# cv2.waitKey()
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale', gray_img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# import cv2
# img = cv2.imread('images/test_image.jpg',0)
# cv2.imshow('Grayscale', img)
# cv2.waitKey()
# cv2.destroyAllWindows()
# print(img.shape)

# import matplotlib.pyplot as plt
# import cv2
# img = cv2.imread('images/test_image.jpg',0)
# plt.imshow(img)
# plt.imshow(img, cmap='gray')
# import cv2
# image = cv2.imread('images/test_image.jpg')

# B, G, R = image[10, 50]
# print (B, G, R)
# print ("shape:", image.shape)