# RTSP People Detector

Detect people from a RTSP stream using OpenCV's HOG algorithm and notify the subscribers via SMS.

## How to run
1. Clone de project.
```
git clone https://github.com/augustogoulart/rtsp-people-detector
```
2. Create a `.env` at the root level and change the STREAM variable:
```
cp contrib/env-sample.txt .env

# for intelbras cameras
STREAM=rtsp://USER:PASSWORD@IP:PORT/cam/realmonitor?channel=CHANNEL&subtype=0

```
3. Run:
```
python run.py
```