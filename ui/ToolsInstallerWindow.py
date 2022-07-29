# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToolsInstallerWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(548, 284)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txt_tool_loc = QTextEdit(Form)
        self.txt_tool_loc.setObjectName(u"txt_tool_loc")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_tool_loc.sizePolicy().hasHeightForWidth())
        self.txt_tool_loc.setSizePolicy(sizePolicy)
        self.txt_tool_loc.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.txt_tool_loc)

        self.btn_browse = QPushButton(Form)
        self.btn_browse.setObjectName(u"btn_browse")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_browse.sizePolicy().hasHeightForWidth())
        self.btn_browse.setSizePolicy(sizePolicy1)
        self.btn_browse.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btn_browse)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.txt_module_call = QTextEdit(Form)
        self.txt_module_call.setObjectName(u"txt_module_call")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_module_call.sizePolicy().hasHeightForWidth())
        self.txt_module_call.setSizePolicy(sizePolicy2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.txt_module_call)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.btn_install = QPushButton(Form)
        self.btn_install.setObjectName(u"btn_install")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_install.sizePolicy().hasHeightForWidth())
        self.btn_install.setSizePolicy(sizePolicy3)
        self.btn_install.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.btn_install)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Maya Tools Installer", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tool Location:", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"browse", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Module Call:", None))
        self.btn_install.setText(QCoreApplication.translate("Form", u"Install", None))
    # retranslateUi

