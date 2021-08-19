import numpy as np
import cv2

def test():
    stream = cv2.VideoCapture(0)
    while True:
        ret, frame = stream.read()
        if ret is False:
            break

        cv2.imshow("test", frame)
        
        key = cv2.waitKey(1)
        if key == ord("q"): break
test()