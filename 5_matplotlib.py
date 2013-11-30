#!/usr/bin/env python

import sys
from PyQt4 import QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import numpy as np

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyQt4 matplotlib Example')
        central_widget = QtGui.QWidget()
        # init plot
        figure = Figure(figsize=(100, 100), dpi=72, facecolor=(1, 1, 1), edgecolor=(1, 1, 1), tight_layout=True)
        self.axes = figure.add_subplot(111)
        self.axes.grid(b=True)
        self.axes.set_title('Plot Title')
        self.axes.set_xlabel('x-axis Label')
        self.axes.set_ylabel('y-axis Label')
        self.canvas = FigureCanvas(figure)
        toolbar = NavigationToolbar(self.canvas, central_widget)
        # init plot controls
        self.equation_output_label = QtGui.QLabel('equation: y = ax^2 + bx + c')
        a_input_label = QtGui.QLabel('a-value:')
        self.a_input_line = QtGui.QLineEdit()
        b_input_label = QtGui.QLabel('b-value:')
        self.b_input_line = QtGui.QLineEdit()
        c_input_label = QtGui.QLabel('c-value:')
        self.c_input_line = QtGui.QLineEdit()
        plot_button = QtGui.QPushButton('Generate Plot', self)
        plot_button.clicked.connect(self.plot_equation)
        # put everything together
        central_layout = QtGui.QVBoxLayout()
        central_layout.addWidget(self.canvas)
        central_layout.addWidget(toolbar)
        central_layout.addWidget(self.equation_output_label)
        central_layout.addWidget(a_input_label)
        central_layout.addWidget(self.a_input_line)
        central_layout.addWidget(b_input_label)
        central_layout.addWidget(self.b_input_line)
        central_layout.addWidget(c_input_label)
        central_layout.addWidget(self.c_input_line)
        central_layout.addWidget(plot_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def plot_equation(self):
        if len(self.a_input_line.text()) == 0 or len(self.b_input_line.text()) == 0 or len(self.c_input_line.text()) == 0:
            self.equation_output_label.setText('equation: y = ax^2 + bx + c')
            return
        self.equation_output_label.setText('equation: y = ' + self.a_input_line.text() + 'x^2 + ' + self.b_input_line.text() + 'x + ' + self.c_input_line.text())
        self.axes.cla()
        self.axes.grid(b=True)
        self.axes.set_title('Plot Title')
        self.axes.set_xlabel('x-axis Label')
        self.axes.set_ylabel('y-axis Label')
        x = np.arange(-10, 10, 0.01)
        y = int(self.a_input_line.text()) * x**2 + int(self.b_input_line.text()) * x + int(self.c_input_line.text())
        self.axes.plot(x, y)
        self.canvas.draw()

def main():
    application = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()
