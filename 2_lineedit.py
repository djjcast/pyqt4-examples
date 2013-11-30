#!/usr/bin/env python

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyQt4 lineedit Example')
        self.input_line = QtGui.QLineEdit()
        print_button = QtGui.QPushButton("print 'hello, ' + lineedit", self)
        print_button.clicked.connect(self.print_hello_lineedit)
        central_widget = QtGui.QWidget()
        central_layout = QtGui.QVBoxLayout()
        central_layout.addWidget(self.input_line)
        central_layout.addWidget(print_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def print_hello_lineedit(self):
        print 'hello, ' + self.input_line.text()

def main():
    application = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()
