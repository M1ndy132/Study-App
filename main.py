from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("StudyApp v1")
        self.setGeometry(100, 100, 600, 400)
        

        main = QWidget()
        self.setCentralWidget(main)
        main_layout = QHBoxLayout()
        main.setLayout(main_layout)

        sidebar = QWidget()
        sidebar_layout = QVBoxLayout()
        content_area = QStackedWidget()
        content_area_layout = QVBoxLayout()
        sidebar.setLayout(sidebar_layout)
        content_area.setLayout(content_area_layout)
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content_area)
        Home = QPushButton("Home")
        Flashcard = QPushButton("Flashcard")
        Quiz = QPushButton("Quiz")
        sidebar_layout.addWidget(Home)
        sidebar_layout.addWidget(Flashcard)
        sidebar_layout.addWidget(Quiz)

        def On_home_clicked():
            index = 0
            print("Home clicked")
        
        Home.clicked.connect(On_home_clicked)

        def on_flashcard_clicked():
            print("Flashcard clicked")

        Flashcard.clicked.connect(on_flashcard_clicked)

        def on_quiz_clicked():
            print("Quiz clicked")

        Quiz.clicked.connect(on_quiz_clicked)
            


    



app = QApplication(sys.argv)
Window = Main_Window()
Window.show()
sys.exit(app.exec_())