from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_ReportWindow(object):
    def setupUi(self, ReportWindow):
        ReportWindow.setObjectName("ReportWindow")
        ReportWindow.resize(487, 185)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        ReportWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("11954229571856793418warning_naught101_01.svg.med.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        #C:\\Users\\Legion\\Documents\\GitHub\\pic2ascii\\GUI Code Qt6 & Qt5\\u232\\ALARM! (don\'t touch) Note to self plz del affter done\\
        ReportWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ReportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setGeometry(QtCore.QRect(406, 153, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.pushButtonGitHub = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGitHub.setGeometry(QtCore.QRect(20, 112, 153, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButtonGitHub.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("github.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        #C:\\Users\\Legion\\Documents\\GitHub\\pic2ascii\\GUI Code Qt6 & Qt5\\u232\\ALARM! (don\'t touch) Note to self plz del affter done\\
        self.pushButtonGitHub.setIcon(icon1)
        self.pushButtonGitHub.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonGitHub.setCheckable(False)
        self.pushButtonGitHub.setAutoDefault(False)
        self.pushButtonGitHub.setDefault(False)
        self.pushButtonGitHub.setFlat(False)
        self.pushButtonGitHub.setObjectName("pushButtonGitHub")
        self.pushButtonMsForms = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMsForms.setGeometry(QtCore.QRect(206, 112, 163, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.pushButtonMsForms.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("microsoft-infopath-3.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        #C:\\Users\\Legion\\Documents\\GitHub\\pic2ascii\\GUI Code Qt6 & Qt5\\u232\\ALARM! (don\'t touch) Note to self plz del affter done\\
        self.pushButtonMsForms.setIcon(icon2)
        self.pushButtonMsForms.setIconSize(QtCore.QSize(44, 25))
        self.pushButtonMsForms.setObjectName("pushButtonMsForms")
        self.Explain = QtWidgets.QLabel(self.centralwidget)
        self.Explain.setGeometry(QtCore.QRect(8, 6, 472, 94))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.Explain.setFont(font)
        self.Explain.setWordWrap(True)
        self.Explain.setObjectName("Explain")
        ReportWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ReportWindow)
        QtCore.QMetaObject.connectSlotsByName(ReportWindow)

    def retranslateUi(self, ReportWindow):
        _translate = QtCore.QCoreApplication.translate
        ReportWindow.setWindowTitle(_translate("ReportWindow", "Report an Error!"))
        self.pushButtonCancel.setText(_translate("ReportWindow", "Cancel"))
        self.pushButtonGitHub.setText(_translate("ReportWindow", "GitLab Issues"))
        self.pushButtonMsForms.setText(_translate("ReportWindow", "MS Form"))
        self.Explain.setText(_translate("ReportWindow", "To report an error click one of these buttons. If you choose GitLab issuses the responce to fix a bug will be much faster (along with adtional feedback) but you will need an acount. If you choose the MS Form then you will be anonymous but it will take more time for us to see it."))

        self.pushButtonCancel.clicked.connect(lambda:ReportWindow.close())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ReportWindow = QtWidgets.QMainWindow()
    ui = Ui_ReportWindow()
    ui.setupUi(ReportWindow)
    ReportWindow.show()
    sys.exit(app.exec())
