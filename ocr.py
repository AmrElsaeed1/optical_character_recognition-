#!/usr/bin/env python
# coding: utf-8

# # optical character recognition 

# # author : Amr Elsaeed

# In[1]:


import cv2
import pytesseract
import os 
import matplotlib.pyplot as plt
import sys


# In[2]:


pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# In[3]:


img= cv2.imread(r"C:\Users\Computec\Downloads\testocr.png")


# In[4]:


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# In[5]:


adaptive_thre=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)


# In[6]:


text=pytesseract.image_to_string(img)


# In[7]:


print(text)


# In[8]:


cv2.imshow("photo", img)
cv2.waitKey(0)
cv2.destroyAllWindows() # destroy all windows


# In[ ]:





# In[ ]:




