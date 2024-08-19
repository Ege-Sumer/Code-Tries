import sys

from PyQt5 import QtWidgets

class Widget(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()
    def  init_ui(self):

        self.writing_area = QtWidgets.QLabel("I have been never pressed...")
        self.button = QtWidgets.QPushButton("Press on me")
        self.count = 0


        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.button)
        v_box.addWidget(self.writing_area)
        v_box.addStretch()


        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.button.clicked.connect(self.click)

        self.show()
    def click(self):
        self.count += 1
        self.writing_area.setText("I've been" + str(self.say) + " times pressed.")





app = QtWidgets.QApplication(sys.argv)

widget = Widget()

sys.exit(app.exec_())

