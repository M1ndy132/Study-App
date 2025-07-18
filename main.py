from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("StudyApp v1")
        self.setGeometry(100, 100, 600, 400)



app = QApplication(sys.argv)
Window = Main_Window()
Window.show()
sys.exit(app.exec_())