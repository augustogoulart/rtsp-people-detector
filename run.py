from decouple import config
from detector import Detector

detector = Detector(config('STREAM'))

while True:
    detector.run()

detector.release()
