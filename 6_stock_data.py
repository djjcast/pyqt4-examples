#!/usr/bin/env python

import sys
from PyQt4 import QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.finance import quotes_historical_yahoo
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
from datetime import date

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Yahoo! Finance')
        central_widget = QtGui.QWidget()
        # init plot
        self.figure = Figure(figsize=(100, 100), dpi=72, facecolor=(1, 1, 1), edgecolor=(1, 1, 1), tight_layout=True)
        self.axes = self.figure.add_subplot(111)
        self.axes.grid(b=True, which='both')
        self.axes.set_title('Historical Opening/Closing Prices')
        self.axes.set_xlabel('Date')
        self.axes.set_ylabel('Price')
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, central_widget)
        # init plot controls
        ticker_symbol_input_label = QtGui.QLabel('Ticker Symbol:')
        self.ticker_symbol_input_line = QtGui.QLineEdit()
        start_date_input_label = QtGui.QLabel('Start Date (Format: yyyy-mm-dd):')
        self.start_date_input_line = QtGui.QLineEdit()
        end_date_input_label = QtGui.QLabel('End Date (Format: yyyy-mm-dd):')
        self.end_date_input_line = QtGui.QLineEdit()
        plot_button = QtGui.QPushButton('Generate Plot', self)
        plot_button.clicked.connect(self.plot_opening_closing_prices)
        # put everything together
        central_layout = QtGui.QVBoxLayout()
        central_layout.addWidget(self.canvas)
        central_layout.addWidget(toolbar)
        central_layout.addWidget(ticker_symbol_input_label)
        central_layout.addWidget(self.ticker_symbol_input_line)
        central_layout.addWidget(start_date_input_label)
        central_layout.addWidget(self.start_date_input_line)
        central_layout.addWidget(end_date_input_label)
        central_layout.addWidget(self.end_date_input_line)
        central_layout.addWidget(plot_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def plot_opening_closing_prices(self):
        if len(self.ticker_symbol_input_line.text()) == 0 or len(self.start_date_input_line.text()) == 0 or len(self.end_date_input_line.text()) == 0:
            return
        start_date = date(*[int(x) for x in self.start_date_input_line.text().split('-')])
        end_date = date(*[int(x) for x in self.end_date_input_line.text().split('-')])
        quotes = quotes_historical_yahoo(str(self.ticker_symbol_input_line.text()), start_date, end_date)
        if len(quotes) == 0:
            return
        dates, opening_prices, closing_prices = zip(*[[q[0], q[1], q[2]] for q in quotes])
        self.axes.cla()
        self.axes.grid(b=True, which='both')
        self.axes.set_title('Historical Opening/Closing Prices')
        self.axes.set_xlabel('Date')
        self.axes.set_ylabel('Price')
        opening_plot, = self.axes.plot_date(dates, opening_prices, 'b-')
        closing_plot, = self.axes.plot_date(dates, closing_prices, 'r-')
        self.axes.legend([opening_plot, closing_plot], ['Opening Price', 'Closing Price'], title='Ticker Symbol: ' + str(self.ticker_symbol_input_line.text()).upper(), loc=2)
        years = YearLocator()
        years_format = DateFormatter('%Y')
        months = MonthLocator()
        self.axes.xaxis.set_major_locator(years)
        self.axes.xaxis.set_major_formatter(years_format)
        self.axes.xaxis.set_minor_locator(months)
        self.axes.autoscale_view()
        self.figure.autofmt_xdate()
        self.axes.fmt_xdata = DateFormatter('%Y-%m-%d')
        self.axes.fmt_ydata = lambda x: '$%1.2f' % x
        self.canvas.draw()

def main():
    application = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()
