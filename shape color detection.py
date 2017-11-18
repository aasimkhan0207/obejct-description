import cv2

class ShapeDetector:
    def __init__(self):
        pass
    def detect(self, c):

        #initialize the shape name and approximate the contour

        # we first compute the perimeter of the contour
        # followed by constructing the actual contour approximation( requires perimeter)
        shape = 'undefined'
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04*peri, True) # list of vertices
        # Common values for the second parameter to cv2.approxPolyDP
        # normally in the range of 1-5% of the original contour perimeter.
        # TRIANGLE( 3 vertices )

        if len(approx) ==3:
            shape = 'triangle'
        # Rectangle or sqaure

        elif len(approx) ==4:
            # calculate side lengths
            x,y,w,h = cv2.boundingRect(approx)
            ratio = w/float(h)
            # square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
            shape = 'square' if ratio>=0.95 and ratio<1.05 else 'rectangle'

        elif len(approx) ==5:
            shape='pentagon'

        else:
            shape ='circle'

        return shape
def color(i, x, y):
    bgr = i[x][y]
    if bgr[1] == 255 and bgr[0] == 0 and bgr[2] == 0:
        c = 'green'
    elif bgr[2] == 255 and bgr[1] == 0 and bgr[0] == 0:
        c = 'red'
    elif bgr[0] == 255 and bgr[1] == 0 and bgr[2] == 0:
        c = 'blue'
    else:
        c = 'white'
    return c
# color(img, x, y cordinates)
img = cv2.imread('test5.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # one channel
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)  # below 150 doesnt give desired output

#cv2.imshow('thresh',thresh)

_, contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img,contours,-1,(0,255,255),3) # to draw all at once

print 'total contours :', len(contours)

sd = ShapeDetector()
obj = ['test.png']

for c in contours:
    M = cv2.moments(c)
    cx = int(M['m01'] / M['m00'])
    cy = int(M['m10'] / M['m00'])

    shape = sd.detect(c)  # store name of shape
    cl = color(img, cx, cy)

    cv2.drawContours(img, [c], -1, (0, 0, 0), 2)  # only one contour(can also use index 0)

    cv2.putText(img, shape, (cy, cx), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2)
    print [cx,cy]
    desc = [shape, cl]
    obj.append(desc)

cv2.imshow('img', img)
print 'Shape of Image', img.shape
print 'Result :', obj
cv2.waitKey(0)
cv2.destroyAllWindows()
