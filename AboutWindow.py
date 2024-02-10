# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiabout.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.setWindowModality(Qt.ApplicationModal)
        About.resize(259, 397)
        About.setMaximumSize(QSize(270, 16777215))
        self.gridLayout = QGridLayout(About)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.CloseButton = QPushButton(About)
        self.CloseButton.setObjectName(u"CloseButton")
        self.CloseButton.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/Icons/closeicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseButton.setIcon(icon)
        self.CloseButton.setFlat(True)

        self.horizontalLayout_5.addWidget(self.CloseButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.IconLabel = QLabel(About)
        self.IconLabel.setObjectName(u"IconLabel")
        self.IconLabel.setMaximumSize(QSize(100, 100))
        self.IconLabel.setPixmap(QPixmap(u":/Icons/icon.png"))
        self.IconLabel.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.IconLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.TitleLabel = QLabel(About)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.TitleLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.VersionLabel = QLabel(About)
        self.VersionLabel.setObjectName(u"VersionLabel")
        self.VersionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.VersionLabel)

        self.AuthorLabel = QLabel(About)
        self.AuthorLabel.setObjectName(u"AuthorLabel")
        self.AuthorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.AuthorLabel)

        self.YearLabel = QLabel(About)
        self.YearLabel.setObjectName(u"YearLabel")
        self.YearLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.YearLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.line = QFrame(About)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.AboutLabel = QLabel(About)
        self.AboutLabel.setObjectName(u"AboutLabel")
        self.AboutLabel.setWordWrap(True)
        self.AboutLabel.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.AboutLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.GithubButton = QPushButton(About)
        self.GithubButton.setObjectName(u"GithubButton")
        self.GithubButton.setMaximumSize(QSize(75, 16777215))
        self.GithubButton.setFlat(True)

        self.horizontalLayout.addWidget(self.GithubButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"About", None))
        self.CloseButton.setText("")
        self.IconLabel.setText("")
        self.TitleLabel.setText(QCoreApplication.translate("About", u"Quote Reminder", None))
        self.VersionLabel.setText(QCoreApplication.translate("About", u"v1.0", None))
        self.AuthorLabel.setText(QCoreApplication.translate("About", u"By Michele Renosto", None))
        self.YearLabel.setText(QCoreApplication.translate("About", u"2024", None))
        self.AboutLabel.setText(QCoreApplication.translate("About", u"Quote Reminder is a free and open source application, licensed under the GPLv3 licence to programmatically display user inserted quotes in the form of popups. \n"
"It is based on Python, Qt 6, qdarktheme, pygame and tendo.", None))
        self.GithubButton.setText(QCoreApplication.translate("About", u"GitHub", None))
    # retranslateUi

