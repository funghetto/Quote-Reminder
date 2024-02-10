# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiquotewin.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_QuoteWindow(object):
    def setupUi(self, QuoteWindow):
        if not QuoteWindow.objectName():
            QuoteWindow.setObjectName(u"QuoteWindow")
        QuoteWindow.resize(355, 106)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QuoteWindow.sizePolicy().hasHeightForWidth())
        QuoteWindow.setSizePolicy(sizePolicy)
        QuoteWindow.setMinimumSize(QSize(355, 0))
        QuoteWindow.setMaximumSize(QSize(899, 16777215))
        icon = QIcon()
        icon.addFile(u":/Icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        QuoteWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(QuoteWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setContentsMargins(-1, 9, -1, 9)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 12, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.CloseQuoteButton = QPushButton(QuoteWindow)
        self.CloseQuoteButton.setObjectName(u"CloseQuoteButton")
        self.CloseQuoteButton.setMaximumSize(QSize(21, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/closeicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseQuoteButton.setIcon(icon1)
        self.CloseQuoteButton.setIconSize(QSize(16, 12))
        self.CloseQuoteButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.CloseQuoteButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalSpacer_2 = QSpacerItem(15, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.QuoteText = QLabel(QuoteWindow)
        self.QuoteText.setObjectName(u"QuoteText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.QuoteText.sizePolicy().hasHeightForWidth())
        self.QuoteText.setSizePolicy(sizePolicy1)
        self.QuoteText.setMinimumSize(QSize(372, 25))
        self.QuoteText.setMaximumSize(QSize(755, 999))
        self.QuoteText.setTextFormat(Qt.AutoText)
        self.QuoteText.setScaledContents(False)
        self.QuoteText.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.QuoteText.setWordWrap(True)
        self.QuoteText.setMargin(2)

        self.horizontalLayout.addWidget(self.QuoteText)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(QuoteWindow)

        QMetaObject.connectSlotsByName(QuoteWindow)
    # setupUi

    def retranslateUi(self, QuoteWindow):
        QuoteWindow.setWindowTitle(QCoreApplication.translate("QuoteWindow", u"Quote", None))
        self.CloseQuoteButton.setText("")
        self.QuoteText.setText(QCoreApplication.translate("QuoteWindow", u"text", None))
    # retranslateUi

