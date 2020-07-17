#This file writed by alirezaahani :)
import ui
import requests
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication,QFileDialog
from PyQt5.QtCore import pyqtSlot

class App(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self,parent=None):
        super(App,self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def go_button_pressed(self):
        self.link.setPlainText("")
        if len(self.text.toPlainText()) > 0:
            payload = {
            'text':self.text.toPlainText()
            }
            try:
                data = requests.post("https://paste.ubuntu.ir/",payload)
                self.link.setPlainText(data.url)
            except:
                self.link.setPlainText("لطفا اتصال اینترنت خود را چک کنید")
        else:
            self.link.setPlainText("لطفا متنی در بخش دریافت متن بنویسید")
def main():
    mainApp = QApplication(['Pastebin'])
    mainwindow = App()
    mainwindow.show()
    mainApp.exec_()

if __name__ == "__main__":
    main()
