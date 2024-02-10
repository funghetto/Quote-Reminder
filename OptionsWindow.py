# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guioptions.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)
import resources_rc

class Ui_AdvancedOptionsDialog(object):
    def setupUi(self, AdvancedOptionsDialog):
        if not AdvancedOptionsDialog.objectName():
            AdvancedOptionsDialog.setObjectName(u"AdvancedOptionsDialog")
        AdvancedOptionsDialog.setWindowModality(Qt.ApplicationModal)
        AdvancedOptionsDialog.resize(232, 239)
        icon = QIcon()
        icon.addFile(u":/Icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        AdvancedOptionsDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(AdvancedOptionsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.CloseButton_2 = QPushButton(AdvancedOptionsDialog)
        self.CloseButton_2.setObjectName(u"CloseButton_2")
        self.CloseButton_2.setMaximumSize(QSize(20, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/closeicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseButton_2.setIcon(icon1)
        self.CloseButton_2.setFlat(True)

        self.horizontalLayout.addWidget(self.CloseButton_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.PositionLabel = QLabel(AdvancedOptionsDialog)
        self.PositionLabel.setObjectName(u"PositionLabel")
        font = QFont()
        font.setFamilies([u"Noto Sans Display"])
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.PositionLabel.setFont(font)

        self.horizontalLayout_6.addWidget(self.PositionLabel)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.PositionComboBox = QComboBox(AdvancedOptionsDialog)
        self.PositionComboBox.setObjectName(u"PositionComboBox")
        self.PositionComboBox.setMaxVisibleItems(4)

        self.horizontalLayout_6.addWidget(self.PositionComboBox)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.SecondsLabel = QLabel(AdvancedOptionsDialog)
        self.SecondsLabel.setObjectName(u"SecondsLabel")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans Display"])
        font1.setItalic(False)
        font1.setStrikeOut(False)
        self.SecondsLabel.setFont(font1)

        self.horizontalLayout_10.addWidget(self.SecondsLabel)

        self.SecondsSpinBox = QSpinBox(AdvancedOptionsDialog)
        self.SecondsSpinBox.setObjectName(u"SecondsSpinBox")
        self.SecondsSpinBox.setMaximumSize(QSize(42, 16777215))
        self.SecondsSpinBox.setMinimum(3)
        self.SecondsSpinBox.setMaximum(61)

        self.horizontalLayout_10.addWidget(self.SecondsSpinBox)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.MinimizedLabel = QLabel(AdvancedOptionsDialog)
        self.MinimizedLabel.setObjectName(u"MinimizedLabel")
        self.MinimizedLabel.setFont(font)

        self.horizontalLayout_13.addWidget(self.MinimizedLabel)

        self.horizontalSpacer_7 = QSpacerItem(98, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)

        self.MinimizedCheckBox = QCheckBox(AdvancedOptionsDialog)
        self.MinimizedCheckBox.setObjectName(u"MinimizedCheckBox")
        self.MinimizedCheckBox.setMaximumSize(QSize(22, 16777215))

        self.horizontalLayout_13.addWidget(self.MinimizedCheckBox)


        self.gridLayout.addLayout(self.horizontalLayout_13, 3, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.DarkThemeLabel = QLabel(AdvancedOptionsDialog)
        self.DarkThemeLabel.setObjectName(u"DarkThemeLabel")
        self.DarkThemeLabel.setFont(font)

        self.horizontalLayout_9.addWidget(self.DarkThemeLabel)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.DarkThemeCheckBox = QCheckBox(AdvancedOptionsDialog)
        self.DarkThemeCheckBox.setObjectName(u"DarkThemeCheckBox")
        self.DarkThemeCheckBox.setMaximumSize(QSize(21, 16777215))

        self.horizontalLayout_9.addWidget(self.DarkThemeCheckBox)


        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.DisableSoundLabel = QLabel(AdvancedOptionsDialog)
        self.DisableSoundLabel.setObjectName(u"DisableSoundLabel")
        self.DisableSoundLabel.setFont(font)

        self.horizontalLayout_11.addWidget(self.DisableSoundLabel)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.DisableSoundCheckBox = QCheckBox(AdvancedOptionsDialog)
        self.DisableSoundCheckBox.setObjectName(u"DisableSoundCheckBox")
        self.DisableSoundCheckBox.setMaximumSize(QSize(21, 16777215))

        self.horizontalLayout_11.addWidget(self.DisableSoundCheckBox)


        self.gridLayout.addLayout(self.horizontalLayout_11, 5, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.RandomLabel = QLabel(AdvancedOptionsDialog)
        self.RandomLabel.setObjectName(u"RandomLabel")
        self.RandomLabel.setMaximumSize(QSize(255, 16777215))
        self.RandomLabel.setFont(font)

        self.horizontalLayout_12.addWidget(self.RandomLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.RandomCheckBox = QCheckBox(AdvancedOptionsDialog)
        self.RandomCheckBox.setObjectName(u"RandomCheckBox")
        self.RandomCheckBox.setMaximumSize(QSize(21, 16777215))

        self.horizontalLayout_12.addWidget(self.RandomCheckBox)


        self.gridLayout.addLayout(self.horizontalLayout_12, 6, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.AutostartLabel = QLabel(AdvancedOptionsDialog)
        self.AutostartLabel.setObjectName(u"AutostartLabel")
        self.AutostartLabel.setMaximumSize(QSize(255, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        self.AutostartLabel.setFont(font2)

        self.horizontalLayout_8.addWidget(self.AutostartLabel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.AutostartCheckBox = QCheckBox(AdvancedOptionsDialog)
        self.AutostartCheckBox.setObjectName(u"AutostartCheckBox")
        self.AutostartCheckBox.setMaximumSize(QSize(22, 16777215))

        self.horizontalLayout_8.addWidget(self.AutostartCheckBox)


        self.gridLayout.addLayout(self.horizontalLayout_8, 7, 0, 1, 1)


        self.retranslateUi(AdvancedOptionsDialog)

        QMetaObject.connectSlotsByName(AdvancedOptionsDialog)
    # setupUi

    def retranslateUi(self, AdvancedOptionsDialog):
        AdvancedOptionsDialog.setWindowTitle(QCoreApplication.translate("AdvancedOptionsDialog", u"Advanced Options", None))
        self.CloseButton_2.setText("")
        self.PositionLabel.setText(QCoreApplication.translate("AdvancedOptionsDialog", u"Quote position:", None))
        self.SecondsLabel.setText(QCoreApplication.translate("AdvancedOptionsDialog", u"Autoclose Quote after seconds:", None))
        self.MinimizedLabel.setText(QCoreApplication.translate("AdvancedOptionsDialog", u"Start Minimized", None))
        self.MinimizedCheckBox.setText("")
        self.DarkThemeLabel.setText(QCoreApplication.translate("AdvancedOptionsDialog", u"Dark theme", None))
        self.DarkThemeCheckBox.setText("")
        self.DisableSoundLabel.setText(QCoreApplication.translate("AdvancedOptionsDialog", u"Disable sound effects", None))
        self.DisableSoundCheckBox.setText("")
        self.RandomLabel.setText(QCoreApplication.translate("AdvancedOptionsDialog", u"Randomize Quote order", None))
        self.RandomCheckBox.setText("")
        self.AutostartLabel.setText(QCoreApplication.translate("AdvancedOptionsDialog", u"Autostart", None))
        self.AutostartCheckBox.setText("")
    # retranslateUi

