# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(515, 517)
        font = QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 40, 485, 461))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.QuoteLabel = QLabel(self.layoutWidget)
        self.QuoteLabel.setObjectName(u"QuoteLabel")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        self.QuoteLabel.setFont(font1)
        self.QuoteLabel.setTextFormat(Qt.AutoText)

        self.horizontalLayout.addWidget(self.QuoteLabel, 0, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"border: 1px solid #dadce0; border-radius: 15px;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchicon = QLabel(self.frame)
        self.searchicon.setObjectName(u"searchicon")
        self.searchicon.setEnabled(True)
        font2 = QFont()
        font2.setKerning(True)
        self.searchicon.setFont(font2)
        self.searchicon.setStyleSheet(u"border: none")
        self.searchicon.setFrameShape(QFrame.NoFrame)
        self.searchicon.setLineWidth(0)
        self.searchicon.setPixmap(QPixmap(u":/Icons/baseline_search_black_20.ico"))

        self.horizontalLayout_3.addWidget(self.searchicon)

        self.SearchBar = QLineEdit(self.frame)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setMinimumSize(QSize(115, 0))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans Display"])
        self.SearchBar.setFont(font3)
        self.SearchBar.setFrame(False)
        self.SearchBar.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.SearchBar)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ListView = QListView(self.layoutWidget)
        self.ListView.setObjectName(u"ListView")
        font4 = QFont()
        font4.setFamilies([u"Noto Sans Display"])
        font4.setPointSize(11)
        font4.setItalic(False)
        font4.setStrikeOut(False)
        self.ListView.setFont(font4)
        self.ListView.setEditTriggers(QAbstractItemView.EditKeyPressed)
        self.ListView.setDragEnabled(False)
        self.ListView.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.ListView.setDefaultDropAction(Qt.IgnoreAction)
        self.ListView.setTextElideMode(Qt.ElideNone)
        self.ListView.setResizeMode(QListView.Adjust)
        self.ListView.setSpacing(7)
        self.ListView.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.ListView)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.AddButton = QPushButton(self.layoutWidget)
        self.AddButton.setObjectName(u"AddButton")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/add_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddButton.setIcon(icon1)
        self.AddButton.setIconSize(QSize(16, 25))
        self.AddButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.AddButton)

        self.RemoveButton = QPushButton(self.layoutWidget)
        self.RemoveButton.setObjectName(u"RemoveButton")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/remove_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RemoveButton.setIcon(icon2)
        self.RemoveButton.setIconSize(QSize(15, 25))
        self.RemoveButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.RemoveButton)

        self.EditButton = QPushButton(self.layoutWidget)
        self.EditButton.setObjectName(u"EditButton")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EditButton.setIcon(icon3)
        self.EditButton.setIconSize(QSize(16, 25))
        self.EditButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.EditButton)

        self.UpButton = QPushButton(self.layoutWidget)
        self.UpButton.setObjectName(u"UpButton")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/expand_less_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.UpButton.setIcon(icon4)
        self.UpButton.setIconSize(QSize(16, 25))
        self.UpButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.UpButton)

        self.DownButton = QPushButton(self.layoutWidget)
        self.DownButton.setObjectName(u"DownButton")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/keyboard_arrow_down_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DownButton.setIcon(icon5)
        self.DownButton.setIconSize(QSize(16, 25))
        self.DownButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.DownButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.MinutesLabel = QLabel(self.layoutWidget)
        self.MinutesLabel.setObjectName(u"MinutesLabel")
        font5 = QFont()
        font5.setFamilies([u"Noto Sans Display"])
        font5.setItalic(False)
        font5.setStrikeOut(False)
        self.MinutesLabel.setFont(font5)

        self.horizontalLayout_11.addWidget(self.MinutesLabel)

        self.MinutesSpinBox = QSpinBox(self.layoutWidget)
        self.MinutesSpinBox.setObjectName(u"MinutesSpinBox")
        self.MinutesSpinBox.setMaximumSize(QSize(52, 16777215))
        self.MinutesSpinBox.setMinimum(1)
        self.MinutesSpinBox.setMaximum(9999)

        self.horizontalLayout_11.addWidget(self.MinutesSpinBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.OptionsButton = QPushButton(self.layoutWidget)
        self.OptionsButton.setObjectName(u"OptionsButton")
        self.OptionsButton.setMaximumSize(QSize(120, 16777215))
        self.OptionsButton.setIconSize(QSize(8, 8))
        self.OptionsButton.setFlat(True)

        self.horizontalLayout_6.addWidget(self.OptionsButton)

        self.horizontalSpacer_5 = QSpacerItem(180, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_4 = QSpacerItem(273, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.DonateButton = QPushButton(self.layoutWidget)
        self.DonateButton.setObjectName(u"DonateButton")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Paypal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DonateButton.setIcon(icon6)
        self.DonateButton.setIconSize(QSize(155, 72))
        self.DonateButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.DonateButton)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.AboutButton = QPushButton(self.layoutWidget)
        self.AboutButton.setObjectName(u"AboutButton")
        self.AboutButton.setFlat(True)

        self.horizontalLayout_5.addWidget(self.AboutButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)


        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-130, 40, 341, 51))
        self.frame_2.setStyleSheet(u"background-color: #5cffff; border-radius: 24px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(400, 92, 164, 41))
        self.frame_3.setStyleSheet(u"background-color: #38fa11; border-radius: 19px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(430, 135, 121, 38))
        self.frame_5.setStyleSheet(u"background-color: #fc7777; border-radius: 19px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.CloseButton = QPushButton(self.centralwidget)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setGeometry(QRect(480, 10, 21, 21))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/closeicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseButton.setIcon(icon7)
        self.CloseButton.setFlat(True)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(360, 380, 178, 120))
        font6 = QFont()
        font6.setItalic(False)
        font6.setStrikeOut(False)
        font6.setKerning(False)
        self.frame_4.setFont(font6)
        self.frame_4.setStyleSheet(u"background-color: #ff87fb;")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(430, 176, 121, 38))
        self.frame_6.setStyleSheet(u"background-color: #1500ff; border-radius: 19px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(430, 217, 121, 79))
        self.frame_7.setStyleSheet(u"background-color: #ff9900; border-radius: 19px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.frame_5.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_2.raise_()
        self.layoutWidget.raise_()
        self.CloseButton.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QuoteRemainder", None))
        self.QuoteLabel.setText(QCoreApplication.translate("MainWindow", u"QUOTE REMINDER", None))
        self.searchicon.setText("")
        self.AddButton.setText("")
        self.RemoveButton.setText("")
        self.EditButton.setText("")
        self.UpButton.setText("")
        self.DownButton.setText("")
        self.MinutesLabel.setText(QCoreApplication.translate("MainWindow", u"Minutes between Quotes:", None))
        self.OptionsButton.setText(QCoreApplication.translate("MainWindow", u"Advanced Options", None))
        self.DonateButton.setText("")
        self.AboutButton.setText(QCoreApplication.translate("MainWindow", u"About Quote Reminder", None))
        self.CloseButton.setText("")
    # retranslateUi

