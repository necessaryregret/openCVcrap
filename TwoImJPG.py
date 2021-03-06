import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
f=set()
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    sensitivity = 100
    f.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))
cv2.imwrite('res.jpg',img_rgb)
template = cv2.imread('template2.jpg',0)
w,h = template.shape[::-1]
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
a=set()
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] +h), (0,0,255),2)
    sensitivity = 100
    a.add((round(pt[0]/sensitivity),round(pt[1]/sensitivity)))
cv2.imwrite('res2.jpg', img_rgb)

print len(f)+len(a)
