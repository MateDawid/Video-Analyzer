# from PyQt5 import QtGui, QtCore, QtWidgets
# import numpy as np
# import cv2
# import sys
#
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
#
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Convert to grayscale.
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Blur using 3 * 3 kernel.
#     gray_blurred = cv2.blur(gray, (3, 3))
#
#     # Apply Hough transform on the blurred image.
#     detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=70, minRadius=20, maxRadius=100)
#     if detected_circles is not None:
#
#         # Convert the circle parameters a, b and r to integers.
#         detected_circles = np.uint16(np.around(detected_circles))
#
#         for pt in detected_circles[0, :]:
#             a, b, r = pt[0], pt[1], pt[2]
#
#             # Draw the circumference of the circle.
#             cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
#             cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)
#
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
#
import sys
from PyQt5.QtWidgets import QApplication
from VideoApp import VideoApp
from Menu import Menu


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Menu()
    main.setGeometry(100, 100, 300, 300)
    main.show()
    sys.exit(app.exec_())


