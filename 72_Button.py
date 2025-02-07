import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        button = QPushButton("Click me!", self)
        button.setGeometry(150, 200, 200, 100)
        button.setStyleSheet("font-size:30px;")
        button.clicked.connect(self.on_click)

    def on_click(self):
        print("Button clicked")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
