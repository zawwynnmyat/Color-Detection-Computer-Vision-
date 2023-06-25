import cv2
import numpy as np
from PIL import Image

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    width = int(capture.get(3))
    height = int(capture.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue = np.uint8([[[255,0,0]]])
    hsvBlue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)

    lower_bound = hsvBlue[0][0][0] - 10, 100, 100
    upper_bound = hsvBlue[0][0][0] + 10, 255, 255

    print(lower_bound, "|", upper_bound)
    imageMask = cv2.inRange(hsv, np.array(lower_bound), np.array(upper_bound))

    mask_ = Image.fromarray(imageMask)

    bbox = mask_.getbbox()

    if(bbox is not None):
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 12)

    cv2.imshow("frame", frame)

    if(cv2.waitKey(1) == ord("q")):
        break

capture.release()
cv2.destroyAllWindows()