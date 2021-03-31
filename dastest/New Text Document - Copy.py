import sys
from PyQt6.QtWidgets import QApplication, QWidget

class ui_MainWindow(QWidget):
        #super().__init__()
    pass
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
