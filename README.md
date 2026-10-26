# Image-Handling-and-Pixel-Transformations-Using-OpenCV

# AIM:
Write a Python program using OpenCV that performs the following tasks:

Read and Display an Image.

Adjust the brightness of an image.

Modify the image contrast.

Generate a third image using bitwise operations.

# Software Required:

Anaconda - Python 3.7
Jupyter Notebook (for interactive development and execution)

# Algorithm:
Step 1:
Load an image from your local directory and display it.

Step 2:
Create a matrix of ones (with data type float64) to adjust brightness.

Step 3:
Create brighter and darker images by adding and subtracting the matrix from the original image.
Display the original, brighter, and darker images.

Step 4:
Modify the image contrast by creating two higher contrast images using scaling factors of 1.1 and 1.2 (without overflow fix).
Display the original, lower contrast, and higher contrast images.

Step 5:
Split the image (boy.jpg) into B, G, R components and display the channels

#Program Developed By:
Name: Yuuvasri R

Register Number: 212225230313

Ex. No. 01
1. Read the image ('Apple.jpg') using OpenCV imread() as a grayscale image.
```
img = cv2.imread('city.jpg', cv2.IMREAD_GRAYSCALE)
```
Q2: Print image dimensions and channels
```
print(f"Width: {img.shape[1]}, Height: {img.shape[0]}, Channels: {len(img.shape)}")
```
Q3: Display grayscale image
```
plt.imshow(img, cmap='gray')
plt.show()
```
Q4: Save image as PNG
```
cv2.imwrite('city.png', img)
```
Q5: Read PNG as color image
```
img_color = cv2.imread('city.png')
img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
```
Q6: Display color image and print dimensions
```
plt.imshow(img_rgb)
plt.show()
print(f"Width: {img_rgb.shape[1]}, Height: {img_rgb.shape[0]}, Channels: {img_rgb.shape[2]}")
```
Q7: Crop image
```
roi = img_rgb[100:400, 150:500]  # [y1:y2, x1:x2]
```
Q8: Resize image by 2x
```
resized = cv2.resize(img_rgb, (img_rgb.shape[1]*2, img_rgb.shape[0]*2))
```
Q9: Flip image horizontally
```
flipped = cv2.flip(roi, 1)
```
Q10: Read image and convert to RGB
```
img = cv2.imread('city.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
Q11: Add centered text
```
text = "Smart City View"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img_rgb, text, (50, img_rgb.shape[0]-30), font, 1, (255,255,255), 2)
```
Q12: Draw rectangle around object
```
cv2.rectangle(img_rgb, (x1, y1), (x2, y2), (255, 0, 255), 2)  # Magenta rectangle
```
Q13: Display annotated image
```
plt.imshow(img_rgb)
plt.show()
```
Q14: Read image again
```
img = cv2.imread('city.jpg')
```
Q15: Adjust brightness with ones matrix
```
ones = np.ones(img.shape, dtype=np.uint8) * 50
```
Q16: Create brighter and darker versions
```
brighter = cv2.add(img, ones)
darker = cv2.subtract(img, ones)
```
Q17: Display original, darker, and brighter images
```
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title("Original")
axes[1].imshow(cv2.cvtColor(darker, cv2.COLOR_BGR2RGB))
axes[1].set_title("Darker")
axes[2].imshow(cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB))
axes[2].set_title("Brighter")
plt.show()
```
Q18: Adjust contrast with scaling factors
```
contrast_1_1 = (img.astype(np.float32) * 1.1).astype(np.uint8)
contrast_1_2 = (img.astype(np.float32) * 1.2).astype(np.uint8)
```
Q19: Display original, lower, and higher contrast images
```
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title("Original")
axes[1].imshow(cv2.cvtColor(contrast_1_1, cv2.COLOR_BGR2RGB))
axes[1].set_title("Contrast 1.1x")
axes[2].imshow(cv2.cvtColor(contrast_1_2, cv2.COLOR_BGR2RGB))
axes[2].set_title("Contrast 1.2x")
plt.show()
```
Q20: Split and display BGR channels
```
b, g, r = cv2.split(img)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(b, cmap='gray')
axes[0].set_title("Blue")
axes[1].imshow(g, cmap='gray')
axes[1].set_title("Green")
axes[2].imshow(r, cmap='gray')
axes[2].set_title("Red")
plt.show()
```
Q21: Merge BGR channels with original
```
merged = cv2.merge([b, g, r])
fig, axes = plt.subplots(1, 4, figsize=(20, 5))
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title("Original")
axes[1].imshow(b, cmap='gray')
axes[1].set_title("Blue")
axes[2].imshow(g, cmap='gray')
axes[2].set_title("Green")
axes[3].imshow(r, cmap='gray')
axes[3].set_title("Red")
plt.show()
```
Q22: Split and display HSV channels
```
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(h, cmap='hsv')
axes[0].set_title("Hue")
axes[1].imshow(s, cmap='gray')
axes[1].set_title("Saturation")
axes[2].imshow(v, cmap='gray')
axes[2].set_title("Value")
plt.show()
```
Q23: Merge HSV channels with original
```
merged_hsv = cv2.merge([h, s, v])
result = cv2.cvtColor(merged_hsv, cv2.COLOR_HSV2BGR)
fig, axes = plt.subplots(1, 4, figsize=(20, 5))
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title("Original")
axes[1].imshow(h, cmap='hsv')
axes[1].set_title("Hue")
axes[2].imshow(s, cmap='gray')
axes[2].set_title("Saturation")
axes[3].imshow(v, cmap='gray')
axes[3].set_title("Value")
plt.show()
```

# Output:
i) Read and Display an Image.
<img width="436" height="417" alt="image" src="https://github.com/user-attachments/assets/c53e5fd5-9c6a-4a84-a946-3b0a4275a550" />
<img width="441" height="447" alt="image" src="https://github.com/user-attachments/assets/b9a61db9-435c-45a7-a8ea-f37ad9a28841" />
<img width="445" height="445" alt="image" src="https://github.com/user-attachments/assets/0006400d-a0ed-4c59-aed8-00c97fee0b68" />
<img width="447" height="450" alt="image" src="https://github.com/user-attachments/assets/c95da4e4-a145-4156-903a-3d543c5ee13b" />
<img width="427" height="425" alt="image" src="https://github.com/user-attachments/assets/634e131f-8a98-455a-ac23-00c0141f7743" />
<img width="423" height="422" alt="image" src="https://github.com/user-attachments/assets/cde9837b-9ea7-41c8-8915-d04462439c64" />
<img width="432" height="446" alt="image" src="https://github.com/user-attachments/assets/83d6ffc1-66a7-4371-ba8b-0b5aa928fced" />
<img width="421" height="413" alt="image" src="https://github.com/user-attachments/assets/809a6416-3515-409a-9800-37e183ebb8bc" />
<img width="427" height="447" alt="image" src="https://github.com/user-attachments/assets/f489b9e8-112d-436e-bad1-2d72605aae2b" />
<img width="411" height="432" alt="image" src="https://github.com/user-attachments/assets/409ee1e4-e5e7-4be6-b5d5-da5378a8e03c" />
<img width="420" height="415" alt="image" src="https://github.com/user-attachments/assets/0d7b794a-fe7c-4f37-93b1-12804c288982" />
<img width="520" height="422" alt="image" src="https://github.com/user-attachments/assets/63049ee7-70cc-4b9e-9621-131ec6644f84" />
<img width="421" height="466" alt="image" src="https://github.com/user-attachments/assets/40ec1419-58f8-482a-a076-a7588dec7cf4" />
<img width="416" height="447" alt="image" src="https://github.com/user-attachments/assets/54eefe53-9f32-4116-b0fe-0c2c0ed776df" />
<img width="492" height="447" alt="image" src="https://github.com/user-attachments/assets/32a430aa-f4b1-448f-a6d2-b88d27535868" />

ii) Adjust Image Brightness.
iii) Modify Image Contrast.
iv) Generate Third Image Using Bitwise Operations.
Result:
Thus, the images were read, displayed, brightness and contrast adjustments were made, and bitwise operations were performed successfully using the Python progra
