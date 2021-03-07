import cv2
from PyQt5.QtCore import pyqtSignal, QThread
import numpy as np


class GreenCircleThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()

            # Convert to HSV -> Hue - Saturation - Value
            hsv_frame = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)
            low_range = np.array([40, 0, 0])
            high_range = np.array([80, 255, 255])
            mask = cv2.inRange(hsv_frame, low_range, high_range)
            image = cv2.bitwise_and(cv_img, cv_img, mask=mask)

            # Convert to grayscale.
            gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

            # Apply blur
            gray_blurred = cv2.blur(gray, (3, 3))

            # Apply Hough transform on the blurred image.
            detected_circles = cv2.HoughCircles(image=gray_blurred,
                                                method=cv2.HOUGH_GRADIENT,
                                                dp=1,  # inverse resolution ratio
                                                minDist=20,  # min distance between two circles centers
                                                param1=50,
                                                param2=70,
                                                minRadius=20,
                                                maxRadius=100)
            if detected_circles is not None:

                # Convert the circle parameters a, b and r to integers.
                detected_circles = np.uint16(np.around(detected_circles))

                for pt in detected_circles[0, :]:
                    a, b, r = pt[0], pt[1], pt[2]

                    # Draw existing circles
                    cv2.circle(image, (a, b), r, (0, 255, 0), 2)
                    cv2.circle(image, (a, b), 1, (0, 0, 255), 3)

            if ret:
                self.change_pixmap_signal.emit(image)

        cap.release()
