import cv2

class WebcamStream():
    def __init__(self, **kwargs):
        self.cam_num = kwargs.get("cam_num")
        self.stream = cv2.VideoCapture(self.cam_num)
        _, frame = self.stream.read()
        height, width = frame.shape[:2]
    
    def play():
        print("init inf loop")
        while True:
            ret, frame = self.stream.read()
            if ret is False:
                break

            cv2.imshow(type(self).__name__, frame)
            
            key = cv2.waitKey(1)
            if key == ord("q"): break

stream = WebcamStream(cam_num=0)
stream.play()