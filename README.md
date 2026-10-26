Image-Handling-and-Pixel-Transformations-Using-OpenCV
AIM:
Write a Python program using OpenCV that performs the following tasks:

Read and Display an Image.
Adjust the brightness of an image.
Modify the image contrast.
Generate a third image using bitwise operations.
Software Required:
Anaconda - Python 3.7
Jupyter Notebook (for interactive development and execution)
Algorithm:
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

Program Developed By:
Name: [Your Name Here]

Register Number: 212225230313

Ex. No. 01
1. Read the image ('Eagle_in_Flight.jpg') using OpenCV imread() as a grayscale image.
# YOUR CODE HERE
2. Print the image width, height & Channel.
# YOUR CODE HERE
3. Display the image using matplotlib imshow().
# YOUR CODE HERE
4. Save the image as a PNG file using OpenCV imwrite().
# YOUR CODE HERE
5. Read the saved image above as a color image using cv2.cvtColor().
# YOUR CODE HERE
6. Display the Colour image using matplotlib imshow() & Print the image width, height & channel.
# YOUR CODE HERE
7. Crop the image to extract any specific (Eagle alone) object from the image.
# YOUR CODE HERE
8. Resize the image up by a factor of 2x.
# YOUR CODE HERE
9. Flip the cropped/resized image horizontally.
# YOUR CODE HERE
10. Read in the image ('Apollo-11-launch.jpg').
# YOUR CODE HERE
11. Add the following text to the dark area at the bottom of the image (centered on the image):
text = 'Apollo 11 Saturn V Launch, July 16, 1969'
font_face = cv2.FONT_HERSHEY_PLAIN
# YOUR CODE HERE: use putText()
12. Draw a magenta rectangle that encompasses the launch tower and the rocket.
rect_color = magenta
# YOUR CODE HERE
13. Display the final annotated image.
# YOUR CODE HERE
14. Read the image ('Boy.jpg').
# YOUR CODE HERE
15. Adjust the brightness of the image.
# Create a matrix of ones (with data type float64)
# matrix_ones = 
# YOUR CODE HERE
16. Create brighter and darker images.
img_brighter = cv2.add(img, matrix)
img_darker = cv2.subtract(img, matrix)
# YOUR CODE HERE
17. Display the images (Original Image, Darker Image, Brighter Image).
# YOUR CODE HERE
18. Modify the image contrast.
# Create two higher contrast images using the 'scale' option with factors of 1.1 and 1.2 (without overflow fix)
matrix1 = 
matrix2 = 
# img_higher1 = 
# img_higher2 = 
# YOUR CODE HERE
19. Display the images (Original, Lower Contrast, Higher Contrast).
# YOUR CODE HERE
20. Split the image (boy.jpg) into the B,G,R components & Display the channels.
# YOUR CODE HERE
21. Merged the R, G, B , displays along with the original image
# YOUR CODE HERE
22. Split the image into the H, S, V components & Display the channels.
# YOUR CODE HERE
23. Merged the H, S, V, displays along with original image.
# YOUR CODE HERE
Output:
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
