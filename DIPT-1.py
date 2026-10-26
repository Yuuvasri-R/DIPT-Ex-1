#!/usr/bin/env python
# coding: utf-8

# In[80]:


# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[81]:


# Display the image using Matplotlib
plt.imshow(img_rgb, cmap='viridis')  # You can change 'viridis' to another cmap or use None for RGB images
plt.title("Original Image")
plt.axis('off')  # Removes axis ticks and labels
plt.show()


# In[82]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[83]:


# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[84]:


img_rgb.shape


# In[85]:


# Draw a line from top-left to bottom-right
line_img = cv2.line(img_rgb, (0, 0), (768, 600), (0, 255, 0), 2) 


# In[92]:


# Second line: Top-right to bottom-left
line_img = cv2.line(line_img, (0, 0), (768, 600), (0, 255, 0), 2)

plt.imshow(line_img)
plt.title('Image with Two Lines')
plt.axis('off')
plt.show()


# In[87]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[88]:


img_rgb.shape


# In[89]:


circle_img = cv2.circle(img_rgb, (400, 200), 150, (255, 0, 0), 10)


# In[90]:


plt.imshow(circle_img,cmap='viridis')
plt.title('Image with Circle')
plt.axis('off')
plt.show()


# In[31]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[32]:


img.shape


# In[33]:


# Draw a rectangle around the Whole image
# Draw a rectangle around the whole apple image
height, width = img_rgb.shape[:2]
rectangle_img = cv2.rectangle(img_rgb.copy(),(0, 0),(width - 1, height - 1),(255, 0, 0),10)


# In[34]:


plt.imshow(rectangle_img, cmap='viridis')  
plt.title("Image with Rectangle")
plt.axis('off')  
plt.show()


# In[35]:


# Load the image
image = cv2.imread('Qno. 1.png') 

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[36]:


height, width = img_rgb.shape[:2]

text_img = cv2.putText(img_rgb.copy(),"OpenCV Drawing",
    (10, 40),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 0),2)


# In[37]:


plt.imshow(text_img, cmap='viridis')  
plt.title("Image with Text")
plt.axis('off')  
plt.show()


# In[38]:


# Load the image
image = cv2.imread('Qno. 1.png') 


# In[39]:


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# In[40]:


# Original RGB Image
plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.axis("off")


# In[41]:


# Convert RGB to HSV
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)


# In[42]:


# HSV Image
plt.imshow(image_hsv)
plt.title("HSV Image")
plt.axis("off")


# In[43]:


# Convert RGB to GRAY
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)


# In[44]:


# Grayscale Image
plt.imshow(image_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")


# In[45]:


# Convert RGB to YCrCb
image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)


# In[46]:


# YCrCb Image
plt.imshow(image_ycrcb)
plt.title("YCrCb Image")
plt.axis("off")


# In[47]:


# Convert HSV back to RGB
image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)


# In[48]:


plt.imshow(image_hsv_to_rgb)
plt.title("HSV to RGB Image")
plt.axis("off")


# In[49]:


# Modify a block of pixels (300x300) to white, starting from (200, 200)
image[200:500, 200:500] = [255, 255, 255]  # Rows: 200-499, Columns: 200-499


# In[50]:


# Convert BGR to RGB for displaying with Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# In[51]:


# Display the modified image
plt.imshow(image_rgb)
plt.title("Image with 300x300 White Block")
plt.axis("off")
plt.show()


# In[52]:


# Load the image
image = cv2.imread('Qno. 1.png') 


# In[53]:


image.shape


# In[54]:


# Resize the image to half its size
resized_image = cv2.resize(image, (768 // 2, 600 // 2))  # (new_width, new_height)


# In[55]:


# Convert BGR to RGB for displaying with Matplotlib
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)


# In[56]:


resized_image_rgb.shape


# In[57]:


# Display the resized image
plt.imshow(resized_image_rgb)
plt.title("Resized Image (Half Size)")
plt.axis("off")
plt.show()


# In[58]:


# Load the image
image = cv2.imread('Qno. 1.png') 


# In[59]:


image.shape


# In[60]:


# Crop a 300x300 region starting from (50, 50)
roi = image[50:350, 50:350]  # Rows: 50-349, Columns: 50-349


# In[61]:


# Convert BGR to RGB for displaying with Matplotlib
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)


# In[62]:


# Display the cropped region (ROI)
plt.imshow(roi_rgb)
plt.title("Cropped Region of Interest (ROI)")
plt.axis("off")
plt.show()


# In[63]:


# Load the image
image = cv2.imread('Qno. 1.png') 


# In[64]:


# Flip the image horizontally (left-right)
flipped_horizontally = cv2.flip(image, 1)


# In[65]:


# Convert BGR to RGB for displaying with Matplotlib
flipped_horizontally_rgb = cv2.cvtColor(flipped_horizontally, cv2.COLOR_BGR2RGB)


# In[66]:


# Horizontal flip
plt.imshow(flipped_horizontally_rgb)
plt.title("Flipped Horizontally")
plt.axis("off")


# In[67]:


# Flip the image vertically (up-down)
flipped_vertically = cv2.flip(image, 0)


# In[68]:


# Convert BGR to RGB for displaying with Matplotlib
flipped_vertically_rgb = cv2.cvtColor(flipped_vertically, cv2.COLOR_BGR2RGB)


# In[69]:


# Vertical flip
plt.imshow(flipped_vertically_rgb)
plt.title("Flipped Vertically")
plt.axis("off")


# In[ ]:





# In[ ]:




