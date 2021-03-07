import cv2
from PyQt5.QtCore import pyqtSignal, QThread
import numpy as np


class GreenThread(QThread):
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

            if ret:
                self.change_pixmap_signal.emit(image)

        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

