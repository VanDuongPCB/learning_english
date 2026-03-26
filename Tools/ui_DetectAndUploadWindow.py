# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DetectAndUploadWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_DetectAndUploadWindow(object):
    def setupUi(self, DetectAndUploadWindow):
        if not DetectAndUploadWindow.objectName():
            DetectAndUploadWindow.setObjectName(u"DetectAndUploadWindow")
        DetectAndUploadWindow.resize(1044, 600)
        self.centralwidget = QWidget(DetectAndUploadWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txtInputs = QPlainTextEdit(self.centralwidget)
        self.txtInputs.setObjectName(u"txtInputs")

        self.gridLayout_2.addWidget(self.txtInputs, 1, 0, 1, 1)

        self.lsvLinks = QListView(self.centralwidget)
        self.lsvLinks.setObjectName(u"lsvLinks")
        self.lsvLinks.setMaximumSize(QSize(350, 16777215))

        self.gridLayout_2.addWidget(self.lsvLinks, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txtOwner = QLineEdit(self.centralwidget)
        self.txtOwner.setObjectName(u"txtOwner")

        self.horizontalLayout.addWidget(self.txtOwner)

        self.chxListen = QCheckBox(self.centralwidget)
        self.chxListen.setObjectName(u"chxListen")
        self.chxListen.setChecked(True)

        self.horizontalLayout.addWidget(self.chxListen)

        self.chxRead = QCheckBox(self.centralwidget)
        self.chxRead.setObjectName(u"chxRead")
        self.chxRead.setChecked(True)

        self.horizontalLayout.addWidget(self.chxRead)

        self.chxVocabulary = QCheckBox(self.centralwidget)
        self.chxVocabulary.setObjectName(u"chxVocabulary")
        self.chxVocabulary.setChecked(True)

        self.horizontalLayout.addWidget(self.chxVocabulary)

        self.chxGrammar = QCheckBox(self.centralwidget)
        self.chxGrammar.setObjectName(u"chxGrammar")
        self.chxGrammar.setChecked(True)

        self.horizontalLayout.addWidget(self.chxGrammar)

        self.chxQuiz = QCheckBox(self.centralwidget)
        self.chxQuiz.setObjectName(u"chxQuiz")
        self.chxQuiz.setChecked(True)

        self.horizontalLayout.addWidget(self.chxQuiz)

        self.btnDetect = QPushButton(self.centralwidget)
        self.btnDetect.setObjectName(u"btnDetect")

        self.horizontalLayout.addWidget(self.btnDetect)

        self.btnUpload = QPushButton(self.centralwidget)
        self.btnUpload.setObjectName(u"btnUpload")

        self.horizontalLayout.addWidget(self.btnUpload)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        DetectAndUploadWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DetectAndUploadWindow)

        QMetaObject.connectSlotsByName(DetectAndUploadWindow)
    # setupUi

    def retranslateUi(self, DetectAndUploadWindow):
        DetectAndUploadWindow.setWindowTitle(QCoreApplication.translate("DetectAndUploadWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("DetectAndUploadWindow", u"Owner", None))
        self.chxListen.setText(QCoreApplication.translate("DetectAndUploadWindow", u"Listen", None))
        self.chxRead.setText(QCoreApplication.translate("DetectAndUploadWindow", u"Read", None))
        self.chxVocabulary.setText(QCoreApplication.translate("DetectAndUploadWindow", u"Vocabulary", None))
        self.chxGrammar.setText(QCoreApplication.translate("DetectAndUploadWindow", u"Grammar", None))
        self.chxQuiz.setText(QCoreApplication.translate("DetectAndUploadWindow", u"Quiz", None))
        self.btnDetect.setText(QCoreApplication.translate("DetectAndUploadWindow", u"Detect", None))
        self.btnUpload.setText(QCoreApplication.translate("DetectAndUploadWindow", u"Upload", None))
    # retranslateUi

