import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from PIL import Image
import cv2

b_img=np.zeros((512,512),np.int8)
plt.Figure(figsize=(20,20))
def dc(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)
        
cv2.namedWindow(winname='my')

cv2.setMouseCallback('my',dc)

while True:
    plt.imshow('my',b_img)
    if cv2.waitKey(20)  & 0xFF==27:
        break
cv2.destroyAllWindows()