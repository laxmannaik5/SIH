import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from skimage.io import imread, imshow, imsave
l_img = cv2.imread('C:/Users/laxma/Desktop/SIH_PROJECT/Website/server/images/image5.jpg')
l_img = cv2.resize(l_img,(1000,1000))
img = l_img[500:900,300:,:]
kernel1 = np.ones( (3,3), dtype=np.uint8 )
erode_img1 = cv2.erode(img,kernel1,iterations=2)
dil_img1 = cv2.dilate(erode_img1,kernel1)
cv2.imwrite('C:/Users/laxma/Desktop/SIH_PROJECT/Website/server/images/img.png', erode_img1)
model = tf.keras.models.load_model('C:/Users/laxma/Desktop/SIH_PROJECT/Website/server/model_cyclone.h5')
img = cv2.imread('C:/Users/laxma/Desktop/SIH_PROJECT/Website/server/images/img.png')
img = cv2.resize(img,(128,128))     # resize image to match model's expected sizing
img = img.reshape(1,128,128,3)
pred = model.predict(img, verbose=1)
preds = (pred >0.2).astype(np.uint8)
plt.imsave('C:/Users/laxma/Desktop/SIH_PROJECT/Website/server/images/annotated_image.png',np.squeeze(preds))
m = cv2.imread('C:/Users/laxma/Desktop/SIH_PROJECT/Website/server/images/annotated_image.png')
grayImage = cv2.cvtColor(m, cv2.COLOR_BGR2GRAY)
grayImage_list = grayImage.tolist()
white = sum([i.count(215) for i in grayImage_list])
black = sum([i.count(30) for i in grayImage_list])
area_of_cyclone = (black/(black+white))*100
print(area_of_cyclone)
