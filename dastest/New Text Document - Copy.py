import sys
from PyQt6.QtWidgets import QApplication, QWidget , QProgressBar
from PyQt6 import QtCore

class ui_MainWindow(QWidget):
        #super().__init__()
    def __init__(self):
        super().__init__()
        self.progressBar = QProgressBar()
        self.progressBar.setGeometry(QtCore.QRect(10, 360, 961, 21))
    def closeEvent(self, event):
        print('colsed')
        y = 'yes'
        if y == 'yes':
            event.ignore()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
