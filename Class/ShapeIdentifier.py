# import the necessary packages
import cv2


class ShapeIdentifier:
    def __init__(self):
        pass

    def detect(self, c):
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        # fine tune len comparison ints to accuratley find a true circle,
        #  if circle is found keep the writing on the frame until a new one is found
        # only match circle if x and y are shade of green
        if 2 <= len(approx) <= 5:
            shape = "circle"

        return shape