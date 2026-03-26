import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow #type: ignore
from PySide6.QtUiTools import QUiLoader #type: ignore
from PySide6.QtCore import QFile, Qt, QStringListModel #type: ignore

from Tools.ui_DetectAndUploadWindow import Ui_DetectAndUploadWindow #type: ignore

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DetectAndUploadWindow()
        self.ui.setupUi(self)
        # self.setWindowState(self.windowState() | Qt.WindowMaximized)

        self.ui.btnDetect.clicked.connect(self.detect)
        self.ui.btnUpload.clicked.connect(self.upload)

        self.list_model = None
        pass


    def detect(self):
        print("Detecting...")
        import re

        pattern = r'/reel/\d+'
        html_text = self.ui.txtInputs.toPlainText()
        matches = re.findall(pattern, html_text)
    
        self.full_links = [f"https://www.facebook.com{m}" for m in matches]

        if self.list_model is None:
            self.list_model = QStringListModel()

        self.list_model.setStringList(self.full_links)
        self.ui.lsvLinks.setModel(self.list_model)


    def upload(self):
        import requests
        print("Uploading...")
        if self.full_links is None:
            return
        
        sheet_names = []
        if self.ui.chxListen.isChecked():
            sheet_names.append("Listen")
        if self.ui.chxRead.isChecked():
            sheet_names.append("Read")
        if self.ui.chxVocabulary.isChecked():
            sheet_names.append("Vocabulary")
        if self.ui.chxGrammar.isChecked():
            sheet_names.append("Grammar")
        if self.ui.chxQuiz.isChecked():
            sheet_names.append("Quiz")
        
        owner = self.ui.txtOwner.text()

        for sheet_name in sheet_names:
            for link in self.full_links:
                WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxROgXdQhnSoX6cDqcptYOSboy4V9Tq-sfV7RthQ-w4_IMmJEiNwUyfMFaArCvtqyRu/exec"
                payload = {
                    "owner": owner,
                    "link": link,
                    "sheetName": sheet_name
                }

                r = requests.post(WEB_APP_URL, json=payload)
                print(f"{owner}-{sheet_name}-{link}")
                if r.status_code == 200:
                    print("Kết quả:", r.json())
                else:
                    print("Lỗi:", r.status_code)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
