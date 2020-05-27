import sys

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

def create_gui():

    window = QWidget()
    window.setWindowTitle('PyQt5 App')
    window.setGeometry(100, 100, 280, 80)
    window.move(60, 15)
    helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
    helloMsg.move(60, 15)

    return window

