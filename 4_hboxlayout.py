#!/usr/bin/env python

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyQt4 hboxlayout Example')
        self.output_label = QtGui.QLabel('hello, world')
        self.input_line = QtGui.QLineEdit()
        set_button = QtGui.QPushButton('set label', self)
        set_button.clicked.connect(self.set_label)
        central_widget = QtGui.QWidget()
        central_layout = QtGui.QHBoxLayout()
        central_layout.addWidget(self.output_label)
        central_layout.addWidget(self.input_line)
        central_layout.addWidget(set_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)
        self.setGeometry(0, 0, 500, 500)
        #self.move(0, 0)
        #self.resize(500, 500)

    def set_label(self):
        self.output_label.setText('hello, ' + self.input_line.text())

def main():
    application = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()
