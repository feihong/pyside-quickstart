# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.output = QPlainTextEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        font = QFont()
        font.setPointSize(40)
        self.output.setFont(font)
        self.output.setReadOnly(True)

        self.verticalLayout.addWidget(self.output)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.count = QSpinBox(self.centralwidget)
        self.count.setObjectName(u"count")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.count.sizePolicy().hasHeightForWidth())
        self.count.setSizePolicy(sizePolicy)
        self.count.setValue(8)

        self.horizontalLayout.addWidget(self.count)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.onlyCommon = QCheckBox(self.centralwidget)
        self.onlyCommon.setObjectName(u"onlyCommon")
        self.onlyCommon.setChecked(True)

        self.horizontalLayout.addWidget(self.onlyCommon)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")

        self.verticalLayout.addWidget(self.button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Random Hanzi Generator", None))
        self.output.setPlainText(QCoreApplication.translate("MainWindow", u"\u4f60\u597d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number of hanzi", None))
        self.onlyCommon.setText(QCoreApplication.translate("MainWindow", u"Only show common hanzi", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

