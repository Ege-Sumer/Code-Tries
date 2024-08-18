import sys

from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):

        self.script_line = QtWidgets.QLineEdit()
        self.clear = QtWidgets.QPushButton("Clear")
        self.print = QtWidgets.QPushButton("Print")

        v_b = QtWidgets.QVBoxLayout()
        v_b.addWidget(self.script_line)
        v_b.addWidget(self.clear)
        v_b.addWidget(self.print)

        v_b.addStretch()

        self.setLayout(v_b)

        self.clear.clicked.connect(self.click)
        self.print.clicked.connect(self.click)


        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Clear":
            self.script_line.clear()

        else:
            print(self.script_line.text())








app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
