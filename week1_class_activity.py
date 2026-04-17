# Task 1
# import cv2
# color_img = cv2.imread('/Users/macbook_uz/Downloads/beautiful-shot-lake-middle-mountainous-scenery.jpg')
# cv2.imshow('Color Image', color_img)
# print("Image shape (H, W, C):", color_img.shape)
# cv2.waitKey(0)

# Task 2
#this is without cvtColor
# import cv2
# grayscale_image1 = cv2.imread("/Users/macbook_uz/Downloads/beautiful-shot-lake-middle-mountainous-scenery.jpg", cv2.IMREAD_GRAYSCALE)

# cv2.imshow("Grayscale Image (IMREAD_GRAYSCALE)", grayscale_image1)

# cv2.imwrite("gray_imread.jpg", grayscale_image1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#This is with cvtColor
# import cv2

# color_image = cv2.imread("/Users/macbook_uz/Downloads/beautiful-shot-lake-middle-mountainous-scenery.jpg")

# grayscale_image2 = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Grayscale Image (cvtColor)", grayscale_image2)

# cv2.imwrite("gray_cvtcolor.jpg", grayscale_image2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Task 3
# import cv2

# image = cv2.imread('/Users/macbook_uz/Downloads/beautiful-shot-lake-middle-mountainous-scenery.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# thresholds = [100, 150, 128]

# for t in thresholds:
#     _, binary = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)

#     cv2.imshow(f'Binary threshold {t}', binary)
#     cv2.imwrite(f'binary_{t}.jpg', binary)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
