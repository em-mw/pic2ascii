import pic2ascii, sys
from PyQt6 import QtWidgets


class some():
    def lols(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = pic2ascii.Ui_MainWindow()
        ui.setupUi(MainWindow)
        input('yes')
        print(ui.progressBar.value())
        ui.progressBar.setValue(int(5))
        MainWindow.show()
        sys.exit(pic2ascii.app.exec())
some().lols()
