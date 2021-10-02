import numpy as np
import cv2
from decouple import config

STREAM = config('STREAM')
stream = cv2.VideoCapture(STREAM)

while True:
    ret, frame = stream.read()
    cv2.imshow(config('NAME'), frame)
    cv2.waitKey(1)

stream.release()
cv2.destroyAllWindows()
