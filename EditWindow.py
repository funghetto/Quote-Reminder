# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiedit.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_EditQuote(object):
    def setupUi(self, EditQuote):
        if not EditQuote.objectName():
            EditQuote.setObjectName(u"EditQuote")
        EditQuote.setWindowModality(Qt.ApplicationModal)
        EditQuote.resize(400, 300)
        EditQuote.setMinimumSize(QSize(400, 300))
        EditQuote.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/Icons/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        EditQuote.setWindowIcon(icon)
        EditQuote.setStyleSheet(u"")
        self.layoutWidget = QWidget(EditQuote)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 381, 271))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.EditplainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.EditplainTextEdit.setObjectName(u"EditplainTextEdit")

        self.horizontalLayout.addWidget(self.EditplainTextEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.EditButton = QPushButton(self.layoutWidget)
        self.EditButton.setObjectName(u"EditButton")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EditButton.setIcon(icon1)
        self.EditButton.setIconSize(QSize(16, 21))
        self.EditButton.setFlat(True)

        self.verticalLayout.addWidget(self.EditButton)

        self.CloseEditButton = QPushButton(self.layoutWidget)
        self.CloseEditButton.setObjectName(u"CloseEditButton")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/closeicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseEditButton.setIcon(icon2)
        self.CloseEditButton.setIconSize(QSize(16, 21))
        self.CloseEditButton.setFlat(True)

        self.verticalLayout.addWidget(self.CloseEditButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(EditQuote)

        QMetaObject.connectSlotsByName(EditQuote)
    # setupUi

    def retranslateUi(self, EditQuote):
        EditQuote.setWindowTitle(QCoreApplication.translate("EditQuote", u"Edit Quote", None))
        self.EditButton.setText("")
        self.CloseEditButton.setText("")
    # retranslateUi

