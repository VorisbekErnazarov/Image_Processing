# /TODO 1:
from PIL import Image

# Open image
img_pil = Image.open('images/test_image.jpg')

# Print type, size, and mode
print(type(img_pil))
print("Size:", img_pil.size)
print("Mode:", img_pil.mode)

# Display image
img_pil.show()


# /TODO 2
import numpy as np

# Convert PIL image to NumPy array
img_np = np.array(img_pil)

# Print shape and data type
print("Shape:", img_np.shape)
print("Data type:", img_np.dtype)

# /TODO 3
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Read image
img_mpl = mpimg.imread('images/test_image.jpg')

# Print shape
print("Shape:", img_mpl.shape)

# Display image
plt.imshow(img_mpl)
plt.axis("off")
plt.show()

# /TODO 4
from skimage import io, img_as_float
import matplotlib.pyplot as plt

# Read image
img_sk = io.imread('images/test_image.jpg')

# Convert to float
img_float = img_as_float(img_sk)

# Print min and max values
print("Min pixel value:", img_float.min())
print("Max pixel value:", img_float.max())

# Display image
plt.imshow(img_float)
plt.axis("off")
plt.show()

#/TODO 5
import cv2
import matplotlib.pyplot as plt

# Read grayscale image
img_gray = cv2.imread('images/test_image.jpg', cv2.IMREAD_GRAYSCALE)

# Read color image (BGR)
img_bgr = cv2.imread('images/test_image.jpg')

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Display RGB image
plt.imshow(img_rgb)
plt.axis("off")
plt.show()

#/TODO 6
# Perform Canny edge detection
edges = cv2.Canny(img_gray, 100, 200)

# Display result
plt.imshow(edges, cmap="gray")
plt.axis("off")
plt.show()

# /Bonus B
import glob
import cv2
import matplotlib.pyplot as plt

path = "images/test_image.jpg"

for file in glob.glob(path):
    img = cv2.imread(file)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img_rgb)
    plt.title(file)
    plt.axis("off")
    plt.show()


# Reflection Questions's answers
# 1. Which library was easiest? Why?
# PIL was the easiest because it has simple syntax and is easy to use for basic image operations.

# 2. Which library for real-time video processing?
# OpenCV, because it is fast and optimized for real-time computer vision tasks.

# 3. Difference between RGB and BGR?
# RGB stores colors as Red-Green-Blue, while BGR stores them as Blue-Green-Red.
