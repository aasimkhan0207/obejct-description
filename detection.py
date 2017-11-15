import cv2
from shape import ShapeDetector

img = cv2.imread('test5.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)# below 150 doesnt give desired output

#cv2.imshow('thresh',thresh)

_,contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img,contours,-1,(0,255,255),3) # to draw all at once

print len(contours)

sd = ShapeDetector()
obj = ['test.png']
for c in contours:
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    shape = sd.detect(c) # store name of shape
    cv2.drawContours(img, [c], -1, (0, 0, 0), 2) # only one contour(can also use index 0)
    cv2.putText(img, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2)
    color = 'color'
    desc =[shape,color]
    obj.append(desc)


cv2.imshow('img',img)
print obj
cv2.waitKey(0)
cv2.destroyAllWindows()