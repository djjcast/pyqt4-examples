#!/usr/bin/env python

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyQt4 pushbutton Example')
        print_button = QtGui.QPushButton("print 'hello, world'", self)
        print_button.clicked.connect(self.print_hello_world)
        central_widget = QtGui.QWidget()
        central_layout = QtGui.QVBoxLayout()
        central_layout.addWidget(print_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def print_hello_world(self):
        print 'hello, world'

def main():
    application = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()
