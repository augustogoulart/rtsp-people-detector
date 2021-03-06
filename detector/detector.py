"""
Inspired by https://thedatafrog.com/en/articles/human-detection-video/
"""
import numpy as np
import cv2
from decouple import config


class Detector:
    def __init__(self, rtsp):
        self.stream = cv2.VideoCapture(rtsp)

    def run(self):
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        ret, frame = self.stream.read()
        if not ret:
            # break if there's not next frame
            return

        # resizing for faster detection
        frame = cv2.resize(frame, (640, 480))
        # using a greyscale picture, also for faster detection
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        # detect people in the image
        boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8))
        # returns the bounding boxes for the detected objects
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        for (xA, yA, xB, yB) in boxes:
            # draw boxes
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

        # Show Video
        cv2.imshow(config('NAME', default="WINDOW"), frame)
        cv2.waitKey(1)

    def release(self):
        self.stream.release()
        cv2.destroyAllWindows()
