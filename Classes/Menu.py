from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5.QtGui import QFont
from Classes.App import App
from Classes.VideoThread import VideoThread
from Classes.CircleThread import CircleThread
from Classes.GreenThread import GreenThread
from Classes.GreenCircleThread import GreenCircleThread

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Analyzer - Menu")
        self.display_width = 640
        self.display_height = 480
        self.add_buttons()

    def add_buttons(self):
        # add buttons for all views
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
        self.green_circle_button = QPushButton("Green circle detection")
        self.green_circle_button.clicked.connect(self.open_green_circle_detection)
        self.green_circle_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.green_circle_button.setFont(QFont('Times', 15))

        # create a vertical box layout with image and buttons
        grid = QGridLayout()
        grid.addWidget(self.clean_button, 0, 0)
        grid.addWidget(self.circle_button, 1, 0)
        grid.addWidget(self.green_button, 2, 0)
        grid.addWidget(self.green_circle_button, 3, 0)
        self.setLayout(grid)

    # define functions displaying video from different threads
    def open_clean_view(self):
        self.app = App(VideoThread())
        self.app.setWindowTitle("Video Analyzer - Clean View")
        self.app.show()

    def open_circle_detection(self):
        self.app = App(CircleThread())
        self.app.setWindowTitle("Video Analyzer - Circle Detection")
        self.app.show()

    def open_green_detection(self):
        self.app = App(GreenThread())
        self.app.setWindowTitle("Video Analyzer - Green colour detection")
        self.app.show()

    def open_green_circle_detection(self):
        self.app = App(GreenCircleThread())
        self.app.setWindowTitle("Video Analyzer - Green circle detection")
        self.app.show()

