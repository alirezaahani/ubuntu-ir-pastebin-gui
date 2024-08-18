import ui
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal

class RequestThread(QThread):
    result_ready = pyqtSignal(str)

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text

    def run(self):
        try:
            response = requests.post("https://paste.ubuntu-ir.org/", data={'text': self.text})
            if response.status_code == 200:
                self.result_ready.emit(response.url)
            else:
                self.result_ready.emit(f"خطا در ارسال: {response.status_code}")
        except requests.RequestException:
            self.result_ready.emit("لطفا اتصال اینترنت خود را بررسی کنید.")

class App(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.thread = None

    @pyqtSlot()
    def send_button_pressed(self):
        self.link.clear()

        text = self.text.toPlainText().strip()
        if not text:
            self.link.setPlainText("لطفا متنی جهت ارسال وارد کنید.")
            return

        self.thread = RequestThread(text)
        self.thread.result_ready.connect(self.on_result_ready)
        self.thread.start()

    @pyqtSlot(str)
    def on_result_ready(self, result):
        self.link.setPlainText(result)

def main():
    app = QApplication([])
    window = App()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
