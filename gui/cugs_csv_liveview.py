# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cugs_csv_liveview.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHeaderView,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 600)
        Form.setMinimumSize(QSize(900, 600))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.centralframe = QFrame(Form)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setFrameShape(QFrame.StyledPanel)
        self.centralframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.centralframe)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.table_csv = QTableWidget(self.centralframe)
        if (self.table_csv.columnCount() < 3):
            self.table_csv.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_csv.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_csv.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_csv.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.table_csv.rowCount() < 1):
            self.table_csv.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_csv.setVerticalHeaderItem(0, __qtablewidgetitem3)
        self.table_csv.setObjectName(u"table_csv")
        self.table_csv.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_csv.horizontalHeader().setMinimumSectionSize(75)
        self.table_csv.horizontalHeader().setDefaultSectionSize(90)
        self.table_csv.horizontalHeader().setStretchLastSection(True)
        self.table_csv.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.table_csv)

        self.button_frame = QFrame(self.centralframe)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setMinimumSize(QSize(0, 30))
        self.button_frame.setFrameShape(QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.btn_clear = QPushButton(self.button_frame)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(0, 0, 131, 30))
        self.btn_clear.setMinimumSize(QSize(0, 30))
        self.btn_clear.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.btn_pop = QPushButton(self.button_frame)
        self.btn_pop.setObjectName(u"btn_pop")
        self.btn_pop.setGeometry(QRect(140, 0, 131, 30))
        self.btn_pop.setMinimumSize(QSize(0, 30))
        self.btn_pop.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_pop.setFont(font1)

        self.verticalLayout_2.addWidget(self.button_frame)


        self.verticalLayout.addWidget(self.centralframe)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.table_csv.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"TEAM_ID", None));
        ___qtablewidgetitem1 = self.table_csv.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"PACKET", None));
        ___qtablewidgetitem2 = self.table_csv.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"TIME", None));
        ___qtablewidgetitem3 = self.table_csv.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"1", None));
        self.btn_clear.setText(QCoreApplication.translate("Form", u"Clear Table", None))
        self.btn_pop.setText(QCoreApplication.translate("Form", u"Pop Table", None))
    # retranslateUi

