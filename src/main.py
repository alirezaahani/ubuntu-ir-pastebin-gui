import ui
import requests
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication,QFileDialog
from PyQt5.QtCore import pyqtSlot

class App(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App,self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def send_button_pressed(self):
        self.link.clear()

        if not (text := self.text.toPlainText()):
            self.link.setPlainText(f"لطفا متنی جهت ارسال وارد کنید.")
            return

        try:
            data = requests.post("https://paste.ubuntu.ir/", {
                'text': text,
            })

            self.link.setPlainText(data.url)
        except requests.RequestException:
            self.link.setPlainText(f"لطفا اتصال اینترنت خود را بررسی کنید.")


def main():
    mainApp = QApplication([])
    mainwindow = App()
    mainwindow.show()
    mainApp.exec()

if __name__ == "__main__":
    main()
