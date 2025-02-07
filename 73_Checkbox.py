# PyQt5 checkbox
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do You like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(0, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 20px;"
                                    "font-family:Arial;")

        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == 2:  # 2: the value is take from the state function if we checked the box then state=0 unchecked box state= 2
            print("You like food!")
        else:
            print("You DO NOT liked food")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
