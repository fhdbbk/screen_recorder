__author__ = "Fahad"

import sys
from screen_capture import capture_screen
import gui


def setup_gui(gui_type):
    if gui_type == 'pyqt':
        from PyQt5.QtWidgets import QApplication
        app = QApplication([])
        gui_window = gui.create_gui()
        gui_window.show()
        sys.exit(app.exec_())

    else:
        print("Pass a valid gui system.")

def main():
    print(f"Welcome to the screen recorder built by {__author__}")
    #capture_screen()
    setup_gui(gui_type='pyqt')



if __name__ == '__main__':
    main()
