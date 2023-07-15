import sys
from PySide2.QtWidgets import QApplication, QWidget , QLabel , QVBoxLayout , QLineEdit , QPushButton , QMessageBox
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import re
import numpy as np


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.ui()

    def ui(self):
        self.layout = QVBoxLayout()

        self.function_label = QLabel("Enter Function :")
        self.function_input = QLineEdit()

        self.range_minmax_label = QLabel("Enter Range (Min,Max)")
        self.range_minmax_input = QLineEdit()

        self.button = QPushButton("Plot")
        self.button.clicked.connect(self.plot)

        self.button2 = QPushButton("Clear Plot")
        self.button2.clicked.connect(self.clearPlot)

        self.layout.addWidget(self.function_label)
        self.layout.addWidget(self.function_input)
        self.layout.addWidget(self.range_minmax_label)
        self.layout.addWidget(self.range_minmax_input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

    def clearPlot(self):
        self.figure.clear()
        self.canvas.draw()


    def plot(self):
        function = self.function_input.text()
        range = self.range_minmax_input.text()


        if not function or not range:
            QMessageBox.critical(self,"Error" , "Please enter function and range")
            return

        if not self.validate_function(function):
            QMessageBox.critical(self, "Error", "Please enter a valid function")
            return

        if not self.validate_range(range):
            QMessageBox.critical(self, "Error", "Please enter a valid range")
            return

        x_min,x_max = map(float,range.split(','))

        numbers = np.linspace(x_min,x_max,100)
        function = function.replace('^', '**')

        y = eval(function, {'x': numbers})

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(numbers,y)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Plot")
        self.canvas.draw()


    def validate_function(self,function):
        check = r"^[0-9+\-*/^x\s]+$"
        return re.match(check, function)

    def validate_range(self,range):
        check = r"^\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*$"
        return re.match(check, range)




if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(myApp.exec_())
import sys
from PySide2.QtWidgets import QApplication, QWidget , QLabel , QVBoxLayout , QLineEdit , QPushButton , QMessageBox
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import re
import numpy as np


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.ui()

    def ui(self):
        self.layout = QVBoxLayout()

        self.function_label = QLabel("Enter Function :")
        self.function_input = QLineEdit()

        self.range_minmax_label = QLabel("Enter Range (Min,Max)")
        self.range_minmax_input = QLineEdit()

        self.button = QPushButton("Plot")
        self.button.clicked.connect(self.plot)

        self.button2 = QPushButton("Clear Plot")
        self.button2.clicked.connect(self.clearPlot)

        self.layout.addWidget(self.function_label)
        self.layout.addWidget(self.function_input)
        self.layout.addWidget(self.range_minmax_label)
        self.layout.addWidget(self.range_minmax_input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

    def clearPlot(self):
        self.figure.clear()
        self.canvas.draw()


    def plot(self):
        function = self.function_input.text()
        range = self.range_minmax_input.text()


        if not function or not range:
            QMessageBox.critical(self,"Error" , "Please enter function and range")
            return

        if not self.validate_function(function):
            QMessageBox.critical(self, "Error", "Please enter a valid function")
            return

        if not self.validate_range(range):
            QMessageBox.critical(self, "Error", "Please enter a valid range")
            return

        x_min,x_max = map(float,range.split(','))

        numbers = np.linspace(x_min,x_max,100)
        function = function.replace('^', '**')

        y = eval(function, {'x': numbers})

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(numbers,y)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Plot")
        self.canvas.draw()


    def validate_function(self,function):
        check = r"^[0-9+\-*/^x\s]+$"
        return re.match(check, function)

    def validate_range(self,range):
        check = r"^\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*$"
        return re.match(check, range)




if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(myApp.exec_())
