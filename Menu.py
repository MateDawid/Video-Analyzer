from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5.QtGui import QFont
from CircleApp import CircleApp
from VideoApp import VideoApp
from GreenApp import GreenApp

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Analyzer - Menu")
        self.display_width = 640
        self.display_height = 480
        self.add_buttons()

    def add_buttons(self):
        self.clean_button = QPushButton("Clean view")
        self.clean_button.clicked.connect(self.open_clean_view)
        self.clean_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.clean_button.setFont(QFont('Times', 15))
        self.circle_button = QPushButton("Circle detection")
        self.circle_button.clicked.connect(self.open_circle_detection)
        self.circle_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.circle_button.setFont(QFont('Times', 15))
        self.green_button = QPushButton("Green colour detection")
        self.green_button.clicked.connect(self.open_green_detection)
        self.green_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.green_button.setFont(QFont('Times', 15))

        # create a vertical box layout with image and buttons
        grid = QGridLayout()
        grid.addWidget(self.clean_button, 0, 0)
        grid.addWidget(self.circle_button, 1, 0)
        grid.addWidget(self.green_button, 2, 0)
        self.setLayout(grid)

    def open_circle_detection(self):
        # if self.view_clean:
        #     self.view_clean.closeEvent()
        # elif self.view_green:
        #     self.view_green.closeEvent()
        self.view_circle = CircleApp()
        self.view_circle.show()

    def open_clean_view(self):
        self.view_clean = VideoApp()
        self.view_clean.show()

    def open_green_detection(self):
        self.view_green = GreenApp()
        self.view_green.show()
