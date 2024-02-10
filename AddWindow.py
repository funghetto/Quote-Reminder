# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiadd.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_AddQuote(object):
    def setupUi(self, AddQuote):
        if not AddQuote.objectName():
            AddQuote.setObjectName(u"AddQuote")
        AddQuote.setWindowModality(Qt.ApplicationModal)
        AddQuote.resize(400, 300)
        AddQuote.setMinimumSize(QSize(400, 300))
        AddQuote.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/Icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        AddQuote.setWindowIcon(icon)
        AddQuote.setStyleSheet(u"")
        self.frame33 = QFrame(AddQuote)
        self.frame33.setObjectName(u"frame33")
        self.frame33.setGeometry(QRect(369, 15, 141, 67))
        self.frame33.setStyleSheet(u"background-color: #858fff;")
        self.frame33.setFrameShape(QFrame.StyledPanel)
        self.frame33.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(AddQuote)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(25, 14, 371, 271))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.PlainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.PlainTextEdit.setObjectName(u"PlainTextEdit")

        self.horizontalLayout.addWidget(self.PlainTextEdit)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AddButton = QPushButton(self.layoutWidget)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setStyleSheet(u"background-color: #f8f9fa;")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/add_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddButton.setIcon(icon1)
        self.AddButton.setIconSize(QSize(16, 21))
        self.AddButton.setFlat(True)

        self.verticalLayout.addWidget(self.AddButton)

        self.QuitButton = QPushButton(self.layoutWidget)
        self.QuitButton.setObjectName(u"QuitButton")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/closeicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.QuitButton.setIcon(icon2)
        self.QuitButton.setIconSize(QSize(16, 21))
        self.QuitButton.setFlat(True)

        self.verticalLayout.addWidget(self.QuitButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(AddQuote)

        QMetaObject.connectSlotsByName(AddQuote)
    # setupUi

    def retranslateUi(self, AddQuote):
        AddQuote.setWindowTitle(QCoreApplication.translate("AddQuote", u"Add Quote", None))
        self.AddButton.setText("")
        self.QuitButton.setText("")
    # retranslateUi

