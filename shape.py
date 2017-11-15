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









