import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import data

print("OpenCV:", cv2.__version__)

# helpers
def to_rgb(img_bgr_or_rgb):
    """Ensure image is RGB uint8."""
    if img_bgr_or_rgb is None:
        raise ValueError("Image is None. Check the path or loading step.")
    img = img_bgr_or_rgb
    if img.ndim == 2:
        return img
    # If it came from cv2.imread it's BGR; if from skimage it's RGB.
    # We detect by heuristic: assume cv2 format if loaded via cv2.imread.
    return img

def load_image(path=None):
    """Load an RGB image. If path is missing, fall back to a built-in sample."""
    if path and os.path.exists(path):
        bgr = cv2.imread(path, cv2.IMREAD_COLOR)
        if bgr is None:
            raise ValueError(f"Failed to read: {path}")
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        return rgb
    # offline sample (RGB)
    return data.astronaut()

def show_side_by_side(img1, img2, title1="Image 1", title2="Image 2", cmap1=None, cmap2=None):
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1); plt.imshow(img1, cmap=cmap1); plt.title(title1); plt.axis('off')
    plt.subplot(1,2,2); plt.imshow(img2, cmap=cmap2); plt.title(title2); plt.axis('off')
    plt.axis('off')
    plt.show()

def clip_uint8(x):
    """Clip and convert to uint8."""
    return np.clip(x, 0, 255).astype(np.uint8)


#  Load an image TODO:
img1 = "images/test_image.jpg"

img = load_image(img1)
print("Image shape (H, W, C):", img.shape, "| dtype:", img.dtype)

plt.figure(figsize=(5,5))
plt.imshow(img)
plt.title("Loaded image (RGB)")
plt.axis("off")
plt.show()


# TODO (Task 2.1): print two pixel values
h, w = img.shape[:2]
print("Top-left pixel:", img[0, 0])
print("Center pixel:", img[h//2, w//2])
# Task 2.1 (Answer):
# An RGB image stores each pixel using three intensity values corresponding to the Red (R), Green (G), and Blue (B) color channels.
# Each value typically ranges from 0 to 255, where 0 means no intensity and 255 means maximum intensity of that color.
# The combination of these three values determines the final color of a pixel (for example, [255, 0, 0] represents pure red, and [0, 0, 0] represents black).


# TODO (Task 2.2): save and reload
output_path = "images/output_saved.png"

# OpenCV expects BGR when writing
bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite(output_path, bgr)

reloaded_bgr = cv2.imread(output_path, cv2.IMREAD_COLOR)
reloaded_rgb = cv2.cvtColor(reloaded_bgr, cv2.COLOR_BGR2RGB)

print("Reloaded shape:", reloaded_rgb.shape, "| dtype:", reloaded_rgb.dtype)
show_side_by_side(img, reloaded_rgb, "Original", "Reloaded")
# The reloaded image has the same shape as the original image, confirming that no spatial information was lost during saving and loading.
# The data type of the reloaded image is uint8, which is the standard format for 8-bit images and is preserved by OpenCV.
# This verifies that saving the image to disk and loading it back does not change the image dimensions or data type when proper color conversion is used.


# TODO (Task 3.1): grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
show_side_by_side(img, gray, "RGB", "Grayscale", cmap2="gray")
print("Gray shape:", gray.shape, "| dtype:", gray.dtype)
# The grayscale image is created by converting the RGB image to a single-channel image using OpenCV.
# In the grayscale image, each pixel represents intensity (brightness) instead of color information, which reduces the image from three channels (RGB) to one channel.


# TODO (Task 3.2): thresholding
th_manual = 128
_, binary_manual = cv2.threshold(gray, th_manual, 255, cv2.THRESH_BINARY)

_, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

show_side_by_side(binary_manual, binary_otsu, f"Manual (T={th_manual})", "Otsu", cmap1="gray", cmap2="gray")
print("Otsu threshold chosen by OpenCV:", _)
# Manual threshold uses a fixed value (128) for all images, which may not be optimal under different lighting conditions.
# Otsu’s method automatically selects an optimal threshold based on the image histogram, often producing a cleaner and more balanced binary result.


# TODO (Task 4.1): set ROI coordinates
h, w = img.shape[:2]
x1, y1 = int(0.25*w), int(0.25*h)
x2, y2 = int(0.75*w), int(0.75*h)

roi = img[y1:y2, x1:x2].copy()
show_side_by_side(img, roi, "Original", f"ROI x[{x1}:{x2}] y[{y1}:{y2}]")
print("ROI shape:", roi.shape)
# A region of interest (ROI) was extracted using array slicing in the form img[y1:y2, x1:x2].
# The selected region captures the central part of the image, which typically contains the most meaningful visual information.


# Task 4.2 (Answer):
# Images are stored as NumPy arrays in row-major order, where the first index represents the row (y-coordinate) and the second index represents the column (x-coordinate).
# Therefore, pixel access and slicing use the format img[y, x], not img[x, y].


# TODO (Task 5.1): HSV conversion and channel display
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
H, S, V = hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]

plt.figure(figsize=(12,3))
for i, (ch, name) in enumerate([(H,"H"), (S,"S"), (V,"V")], start=1):
    plt.subplot(1,3,i); plt.imshow(ch, cmap="gray"); plt.title(name); plt.axis("off")
plt.show()
# The RGB image was converted to the HSV color space, which separates color information (Hue), color intensity (Saturation), and brightness (Value).
# Displaying the H, S, and V channels individually helps visualize how color, purity, and brightness are represented independently in an image.


# 6.1 Provided example (edit the constant and re-run)
sub_val = 100  # TODO: try 30, 100, 150
img_sub = cv2.subtract(img, sub_val)

show_side_by_side(img, img_sub, "Original", f"Subtracted (-{sub_val})")
# As the value of sub_val increases, the image becomes progressively darker because more intensity is subtracted from each pixel.
# The image gets darker since subtracting a constant reduces pixel intensity values, and OpenCV saturates negative values at 0, leading to loss of brightness in dark regions.


# TODO (Task 6.2): subtract from Red channel only
sub_val_r = 80

img_red_only = img.copy()
# RGB: channel 0=R, 1=G, 2=B
img_red_only[:,:,0] = cv2.subtract(img_red_only[:,:,0], sub_val_r)

show_side_by_side(img, img_red_only, "Original", f"Red channel subtracted (-{sub_val_r})")
# Only the red (R) channel was modified by subtracting a constant value, while the green and blue channels were left unchanged.
# As a result, the image appears less reddish and shifts toward cooler colors, demonstrating the effect of modifying a single color channel.


#Task 6.3
add_val = 100  # TODO: try 30, 100, 150
img_add = cv2.add(img, add_val)

show_side_by_side(img, img_add, "Original", f"Added (+{add_val})")
# As the value of add_val increases, the image becomes progressively brighter.
# The image gets brighter because adding a constant increases pixel intensity values, and OpenCV saturates values at 255, preventing overflow.


# Task 6.4 
# TODO (Task 6.4): add to Red channel only
add_val_r = 80

img_red_only_add = img.copy()
img_red_only_add[:,:,0] = cv2.add(img_red_only_add[:,:,0], add_val_r)

show_side_by_side(img, img_red_only_add, "Original", f"Red channel added (+{add_val_r})")
# Only the red (R) channel was increased by adding a constant value, while the green and blue channels remained unchanged.
# This causes red components in the image to become more prominent, giving the image a warmer or reddish appearance.


# 6.5 TODO: try factors like 0.5, 1.2, 2.0
factor = 2.0

img_f = img.astype(np.float32)
img_mul = clip_uint8(img_f * factor)

show_side_by_side(img, img_mul, "Original", f"Multiplied (×{factor})")
# Multiplying the image by a factor greater than 1 increases pixel intensity values, making the image brighter and increasing contrast, but it can also cause saturation at 255.
# Multiplying by a factor less than 1 reduces pixel intensity values, resulting in a darker image with lower contrast.


# 6.6 TODO: try divisors like 2.0, 3.0, 0.5
divisor = 2.0

img_f = img.astype(np.float32)
img_div = clip_uint8(img_f / divisor)

show_side_by_side(img, img_div, "Original", f"Divided (÷{divisor})")
# Dividing the image by a number greater than 1 decreases pixel intensity values, resulting in a darker image.
# Dividing by a number less than 1 increases pixel intensity values, making the image brighter, but it may cause saturation at 255.


# Report:
# In this assignment, I learned the fundamental concepts of digital image processing using Python, NumPy,
# and OpenCV. I practiced loading and saving images, inspecting pixel values, and understanding how
# images are represented as numerical arrays. I also learned how RGB images contain three color channels
# and how grayscale images reduce the data to a single intensity channel.
# The most useful operations were the arithmetic transformations such as addition, subtraction,
# multiplication, and division. These operations clearly demonstrated how brightness and contrast can be
# adjusted numerically. In particular, modifying a single color channel (red channel only) helped me
# understand how individual channels affect the overall appearance of an image. Otsu’s thresholding
# method was also very useful because it automatically determines an optimal threshold based on the image histogram.
# During the assignment, I encountered a few practical issues, such as handling file paths correctly in VS Code
# and understanding the difference between BGR (OpenCV format) and RGB (Matplotlib display format).
# I also learned the importance of managing data types like uint8 and preventing overflow using clipping.
# Overall, this lab strengthened my understanding of how digital images are processed programmatically.