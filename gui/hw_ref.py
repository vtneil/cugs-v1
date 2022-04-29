# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hw_ref.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName(u"HomeWindow")
        HomeWindow.resize(960, 720)
        HomeWindow.setMinimumSize(QSize(960, 720))
        HomeWindow.setFocusPolicy(Qt.TabFocus)
        HomeWindow.setStyleSheet(u"background-color: none;")
        HomeWindow.setTabShape(QTabWidget.Rounded)
        HomeWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionSave = QAction(HomeWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(HomeWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionRefresh = QAction(HomeWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.actionPreferences = QAction(HomeWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionAbout = QAction(HomeWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionStart = QAction(HomeWindow)
        self.actionStart.setObjectName(u"actionStart")
        self.actionPause = QAction(HomeWindow)
        self.actionPause.setObjectName(u"actionPause")
        self.actionStop = QAction(HomeWindow)
        self.actionStop.setObjectName(u"actionStop")
        self.actionReset = QAction(HomeWindow)
        self.actionReset.setObjectName(u"actionReset")
        self.centralwidget = QWidget(HomeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_30 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.s01 = QFrame(self.centralwidget)
        self.s01.setObjectName(u"s01")
        self.s01.setStyleSheet(u"color: rgb(203, 212, 255);\n"
"border-radius: 0px;")
        self.s01.setFrameShape(QFrame.NoFrame)
        self.s01.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.s01)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.s01a = QFrame(self.s01)
        self.s01a.setObjectName(u"s01a")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s01a.sizePolicy().hasHeightForWidth())
        self.s01a.setSizePolicy(sizePolicy)
        self.s01a.setMinimumSize(QSize(260, 0))
        self.s01a.setMaximumSize(QSize(320, 16777215))
        self.s01a.setStyleSheet(u"background-color: rgba(62, 67, 112, 255);\n"
"border-top-left-radius: 28px;\n"
"border-bottom-left-radius: 28px;")
        self.s01a.setFrameShape(QFrame.NoFrame)
        self.s01a.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.s01a)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.s01a01 = QFrame(self.s01a)
        self.s01a01.setObjectName(u"s01a01")
        self.s01a01.setMinimumSize(QSize(0, 520))
        self.s01a01.setMaximumSize(QSize(16777215, 520))
        self.s01a01.setStyleSheet(u"background-color: none;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.s01a01.setFrameShape(QFrame.NoFrame)
        self.s01a01.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.s01a01)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(16, 16, 32, 0)
        self.s01a01_ = QFrame(self.s01a01)
        self.s01a01_.setObjectName(u"s01a01_")
        self.s01a01_.setEnabled(True)
        self.s01a01_.setMinimumSize(QSize(0, 20))
        self.s01a01_.setMaximumSize(QSize(16777215, 20))
        self.s01a01_.setFrameShape(QFrame.StyledPanel)
        self.s01a01_.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.s01a01_)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_3button = QFrame(self.s01a01_)
        self.frame_3button.setObjectName(u"frame_3button")
        self.frame_3button.setMinimumSize(QSize(70, 0))
        self.frame_3button.setMaximumSize(QSize(70, 16777215))
        self.frame_3button.setFrameShape(QFrame.StyledPanel)
        self.frame_3button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3button)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bt_close = QPushButton(self.frame_3button)
        self.bt_close.setObjectName(u"bt_close")
        self.bt_close.setMinimumSize(QSize(12, 12))
        self.bt_close.setMaximumSize(QSize(12, 12))
        self.bt_close.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 99, 79);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(214, 83, 66);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(162, 63, 50);\n"
"}")

        self.horizontalLayout_10.addWidget(self.bt_close)

        self.bt_minimize = QPushButton(self.frame_3button)
        self.bt_minimize.setObjectName(u"bt_minimize")
        self.bt_minimize.setMinimumSize(QSize(12, 12))
        self.bt_minimize.setMaximumSize(QSize(12, 12))
        self.bt_minimize.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 199, 49);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(213, 169, 51);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(178, 150, 42);\n"
"}")

        self.horizontalLayout_10.addWidget(self.bt_minimize)

        self.bt_maximize = QPushButton(self.frame_3button)
        self.bt_maximize.setObjectName(u"bt_maximize")
        self.bt_maximize.setMinimumSize(QSize(12, 12))
        self.bt_maximize.setMaximumSize(QSize(12, 12))
        self.bt_maximize.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(97, 197, 84);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(82, 166, 70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 138, 58);\n"
"}")

        self.horizontalLayout_10.addWidget(self.bt_maximize)


        self.horizontalLayout_9.addWidget(self.frame_3button)

        self.blank_3button = QFrame(self.s01a01_)
        self.blank_3button.setObjectName(u"blank_3button")
        self.blank_3button.setFrameShape(QFrame.StyledPanel)
        self.blank_3button.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.blank_3button)


        self.verticalLayout_2.addWidget(self.s01a01_)

        self.s01a01a = QFrame(self.s01a01)
        self.s01a01a.setObjectName(u"s01a01a")
        self.s01a01a.setMinimumSize(QSize(0, 130))
        self.s01a01a.setMaximumSize(QSize(16777215, 130))
        self.s01a01a.setFrameShape(QFrame.NoFrame)
        self.s01a01a.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.s01a01a)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(28, -1, -1, -1)
        self.sys_title = QLabel(self.s01a01a)
        self.sys_title.setObjectName(u"sys_title")
        font = QFont()
        font.setBold(True)
        self.sys_title.setFont(font)
        self.sys_title.setStyleSheet(u"font-weight: bold;")
        self.sys_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.sys_title)

        self.sys_clock = QLabel(self.s01a01a)
        self.sys_clock.setObjectName(u"sys_clock")
        font1 = QFont()
        font1.setPointSize(36)
        self.sys_clock.setFont(font1)
        self.sys_clock.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.sys_clock)

        self.sys_stopwatch = QLabel(self.s01a01a)
        self.sys_stopwatch.setObjectName(u"sys_stopwatch")
        font2 = QFont()
        font2.setPointSize(24)
        self.sys_stopwatch.setFont(font2)
        self.sys_stopwatch.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.sys_stopwatch)


        self.verticalLayout_2.addWidget(self.s01a01a)

        self.s01a01b = QFrame(self.s01a01)
        self.s01a01b.setObjectName(u"s01a01b")
        self.s01a01b.setMinimumSize(QSize(0, 150))
        self.s01a01b.setMaximumSize(QSize(16777215, 130))
        self.s01a01b.setFrameShape(QFrame.NoFrame)
        self.s01a01b.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.s01a01b)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(16, 0, 0, 0)
        self.s01a01bx = QFrame(self.s01a01b)
        self.s01a01bx.setObjectName(u"s01a01bx")
        self.s01a01bx.setFrameShape(QFrame.NoFrame)
        self.s01a01bx.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.s01a01bx)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.s01a01bx1 = QFrame(self.s01a01bx)
        self.s01a01bx1.setObjectName(u"s01a01bx1")
        self.s01a01bx1.setFrameShape(QFrame.NoFrame)
        self.s01a01bx1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.s01a01bx1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.sys_com = QLabel(self.s01a01bx1)
        self.sys_com.setObjectName(u"sys_com")
        self.sys_com.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_6.addWidget(self.sys_com)

        self.dev_com = QComboBox(self.s01a01bx1)
        self.dev_com.addItem("")
        self.dev_com.setObjectName(u"dev_com")
        self.dev_com.setMinimumSize(QSize(0, 24))
        self.dev_com.setMaximumSize(QSize(16777215, 24))
        self.dev_com.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(92, 97, 163);\n"
"	border-radius: 8px;\n"
"	color: rgb(203, 212, 255);\n"
"	padding: 1px 0px 1px 12px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"	background-color: rgb(62, 67, 112);\n"
"}")

        self.verticalLayout_6.addWidget(self.dev_com)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 2)

        self.verticalLayout_8.addWidget(self.s01a01bx1)

        self.s01a01bx2 = QFrame(self.s01a01bx)
        self.s01a01bx2.setObjectName(u"s01a01bx2")
        self.s01a01bx2.setFrameShape(QFrame.NoFrame)
        self.s01a01bx2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.s01a01bx2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sys_baud = QLabel(self.s01a01bx2)
        self.sys_baud.setObjectName(u"sys_baud")
        self.sys_baud.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_7.addWidget(self.sys_baud)

        self.dev_baud = QComboBox(self.s01a01bx2)
        self.dev_baud.addItem("")
        self.dev_baud.addItem("")
        self.dev_baud.addItem("")
        self.dev_baud.addItem("")
        self.dev_baud.addItem("")
        self.dev_baud.addItem("")
        self.dev_baud.setObjectName(u"dev_baud")
        self.dev_baud.setMinimumSize(QSize(0, 24))
        self.dev_baud.setMaximumSize(QSize(16777215, 24))
        self.dev_baud.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(92, 97, 163);\n"
"	border-radius: 8px;\n"
"	color: rgb(203, 212, 255);\n"
"	padding: 1px 0px 1px 12px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"	background-color: rgb(62, 67, 112);\n"
"}")
        self.dev_baud.setEditable(False)
        self.dev_baud.setFrame(True)

        self.verticalLayout_7.addWidget(self.dev_baud)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 2)

        self.verticalLayout_8.addWidget(self.s01a01bx2)


        self.verticalLayout_5.addWidget(self.s01a01bx)


        self.verticalLayout_2.addWidget(self.s01a01b)

        self.s01a01c = QFrame(self.s01a01)
        self.s01a01c.setObjectName(u"s01a01c")
        self.s01a01c.setMinimumSize(QSize(0, 0))
        self.s01a01c.setMaximumSize(QSize(16777215, 180))
        self.s01a01c.setFrameShape(QFrame.NoFrame)
        self.s01a01c.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.s01a01c)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(16, 0, 0, 0)
        self.bt_connect = QPushButton(self.s01a01c)
        self.bt_connect.setObjectName(u"bt_connect")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bt_connect.sizePolicy().hasHeightForWidth())
        self.bt_connect.setSizePolicy(sizePolicy1)
        self.bt_connect.setMinimumSize(QSize(0, 32))
        self.bt_connect.setMaximumSize(QSize(16777215, 32))
        self.bt_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_connect.setAutoFillBackground(False)
        self.bt_connect.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgba(114, 122, 205,255);\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(103, 111, 186);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(114, 122, 205,160);\n"
"}")
        self.bt_connect.setAutoDefault(True)
        self.bt_connect.setFlat(False)

        self.verticalLayout_9.addWidget(self.bt_connect)

        self.bt_disconnect = QPushButton(self.s01a01c)
        self.bt_disconnect.setObjectName(u"bt_disconnect")
        self.bt_disconnect.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.bt_disconnect.sizePolicy().hasHeightForWidth())
        self.bt_disconnect.setSizePolicy(sizePolicy1)
        self.bt_disconnect.setMinimumSize(QSize(0, 32))
        self.bt_disconnect.setMaximumSize(QSize(16777215, 32))
        self.bt_disconnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_disconnect.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.verticalLayout_9.addWidget(self.bt_disconnect)

        self.bt_refresh = QPushButton(self.s01a01c)
        self.bt_refresh.setObjectName(u"bt_refresh")
        sizePolicy1.setHeightForWidth(self.bt_refresh.sizePolicy().hasHeightForWidth())
        self.bt_refresh.setSizePolicy(sizePolicy1)
        self.bt_refresh.setMinimumSize(QSize(0, 32))
        self.bt_refresh.setMaximumSize(QSize(16777215, 32))
        self.bt_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_refresh.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.verticalLayout_9.addWidget(self.bt_refresh)

        self.bt_preferences = QPushButton(self.s01a01c)
        self.bt_preferences.setObjectName(u"bt_preferences")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bt_preferences.sizePolicy().hasHeightForWidth())
        self.bt_preferences.setSizePolicy(sizePolicy2)
        self.bt_preferences.setMinimumSize(QSize(0, 32))
        self.bt_preferences.setMaximumSize(QSize(16777215, 32))
        self.bt_preferences.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_preferences.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.verticalLayout_9.addWidget(self.bt_preferences)


        self.verticalLayout_2.addWidget(self.s01a01c)


        self.verticalLayout_4.addWidget(self.s01a01)

        self.s01a02 = QFrame(self.s01a)
        self.s01a02.setObjectName(u"s01a02")
        self.s01a02.setMinimumSize(QSize(0, 0))
        self.s01a02.setMaximumSize(QSize(16777215, 16777215))
        self.s01a02.setStyleSheet(u"background-color: none;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.s01a02.setFrameShape(QFrame.StyledPanel)
        self.s01a02.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.s01a02)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(32, 0, 32, 32)
        self.spacer_up = QFrame(self.s01a02)
        self.spacer_up.setObjectName(u"spacer_up")
        self.spacer_up.setFrameShape(QFrame.StyledPanel)
        self.spacer_up.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.spacer_up)

        self.frame_bt_chart = QFrame(self.s01a02)
        self.frame_bt_chart.setObjectName(u"frame_bt_chart")
        self.frame_bt_chart.setMinimumSize(QSize(0, 32))
        self.frame_bt_chart.setMaximumSize(QSize(16777215, 32))
        self.frame_bt_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_bt_chart.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_bt_chart)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.bt_clear_chart = QPushButton(self.frame_bt_chart)
        self.bt_clear_chart.setObjectName(u"bt_clear_chart")
        sizePolicy1.setHeightForWidth(self.bt_clear_chart.sizePolicy().hasHeightForWidth())
        self.bt_clear_chart.setSizePolicy(sizePolicy1)
        self.bt_clear_chart.setMinimumSize(QSize(0, 32))
        self.bt_clear_chart.setMaximumSize(QSize(16777215, 32))
        self.bt_clear_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_clear_chart.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.horizontalLayout_12.addWidget(self.bt_clear_chart)

        self.bt_pop_chart = QPushButton(self.frame_bt_chart)
        self.bt_pop_chart.setObjectName(u"bt_pop_chart")
        sizePolicy1.setHeightForWidth(self.bt_pop_chart.sizePolicy().hasHeightForWidth())
        self.bt_pop_chart.setSizePolicy(sizePolicy1)
        self.bt_pop_chart.setMinimumSize(QSize(0, 32))
        self.bt_pop_chart.setMaximumSize(QSize(16777215, 32))
        self.bt_pop_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pop_chart.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.horizontalLayout_12.addWidget(self.bt_pop_chart)


        self.verticalLayout_10.addWidget(self.frame_bt_chart)

        self.frame_bt_timer = QFrame(self.s01a02)
        self.frame_bt_timer.setObjectName(u"frame_bt_timer")
        self.frame_bt_timer.setMinimumSize(QSize(0, 32))
        self.frame_bt_timer.setMaximumSize(QSize(16777215, 32))
        self.frame_bt_timer.setFrameShape(QFrame.StyledPanel)
        self.frame_bt_timer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_bt_timer)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bt_timer_start = QPushButton(self.frame_bt_timer)
        self.bt_timer_start.setObjectName(u"bt_timer_start")
        sizePolicy1.setHeightForWidth(self.bt_timer_start.sizePolicy().hasHeightForWidth())
        self.bt_timer_start.setSizePolicy(sizePolicy1)
        self.bt_timer_start.setMinimumSize(QSize(0, 32))
        self.bt_timer_start.setMaximumSize(QSize(16777215, 32))
        self.bt_timer_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_timer_start.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.horizontalLayout_11.addWidget(self.bt_timer_start)

        self.bt_timer_pause = QPushButton(self.frame_bt_timer)
        self.bt_timer_pause.setObjectName(u"bt_timer_pause")
        sizePolicy1.setHeightForWidth(self.bt_timer_pause.sizePolicy().hasHeightForWidth())
        self.bt_timer_pause.setSizePolicy(sizePolicy1)
        self.bt_timer_pause.setMinimumSize(QSize(0, 32))
        self.bt_timer_pause.setMaximumSize(QSize(16777215, 32))
        self.bt_timer_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_timer_pause.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.horizontalLayout_11.addWidget(self.bt_timer_pause)

        self.bt_timer_reset = QPushButton(self.frame_bt_timer)
        self.bt_timer_reset.setObjectName(u"bt_timer_reset")
        sizePolicy1.setHeightForWidth(self.bt_timer_reset.sizePolicy().hasHeightForWidth())
        self.bt_timer_reset.setSizePolicy(sizePolicy1)
        self.bt_timer_reset.setMinimumSize(QSize(0, 32))
        self.bt_timer_reset.setMaximumSize(QSize(16777215, 32))
        self.bt_timer_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_timer_reset.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.horizontalLayout_11.addWidget(self.bt_timer_reset)


        self.verticalLayout_10.addWidget(self.frame_bt_timer)


        self.verticalLayout_4.addWidget(self.s01a02)


        self.horizontalLayout.addWidget(self.s01a)

        self.s01b = QFrame(self.s01)
        self.s01b.setObjectName(u"s01b")
        self.s01b.setStyleSheet(u"background-color: rgb(46, 49, 82);\n"
"border-top-right-radius: 28px;\n"
"border-bottom-right-radius: 28px;")
        self.s01b.setFrameShape(QFrame.NoFrame)
        self.s01b.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_35 = QVBoxLayout(self.s01b)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(32, 36, 32, 32)
        self.s01b01_2 = QFrame(self.s01b)
        self.s01b01_2.setObjectName(u"s01b01_2")
        self.s01b01_2.setStyleSheet(u"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.s01b01_2.setFrameShape(QFrame.StyledPanel)
        self.s01b01_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.s01b01_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.s01b01_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabBar::tab {\n"
"	background-color: rgb(62, 67, 112);\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"	background-color: rgb(92, 97, 163);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(114, 122, 205);\n"
"	color: rgb(255,255,255);\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_plot_view = QWidget()
        self.tab_plot_view.setObjectName(u"tab_plot_view")
        self.tab_plot_view.setStyleSheet(u"border-radius: 0px;")
        self.verticalLayout_13 = QVBoxLayout(self.tab_plot_view)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(8, 24, 8, 12)
        self.s01b00scroll = QScrollArea(self.tab_plot_view)
        self.s01b00scroll.setObjectName(u"s01b00scroll")
        self.s01b00scroll.setStyleSheet(u"QScrollBar {\n"
"	background-color: rgb(46, 49, 82);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(91, 96, 161);\n"
"	min-height: 32px;\n"
"	border-radius: 6px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(79, 83, 140);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(72, 75, 128);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: none;\n"
"	height: 15px;\n"
"	border-radius: 6px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(79, 83, 140);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(72, 75, 128);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: none;\n"
"	height: 15px;\n"
"	border-radius: 6px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color:"
                        " rgb(79, 83, 140);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(72, 75, 128);\n"
"}")
        self.s01b00scroll.setFrameShape(QFrame.NoFrame)
        self.s01b00scroll.setFrameShadow(QFrame.Plain)
        self.s01b00scroll.setWidgetResizable(True)
        self.s01b00content = QWidget()
        self.s01b00content.setObjectName(u"s01b00content")
        self.s01b00content.setGeometry(QRect(0, 0, 582, 1282))
        self.verticalLayout = QVBoxLayout(self.s01b00content)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 32, 0)
        self.s01b01 = QFrame(self.s01b00content)
        self.s01b01.setObjectName(u"s01b01")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.s01b01.sizePolicy().hasHeightForWidth())
        self.s01b01.setSizePolicy(sizePolicy3)
        self.s01b01.setMinimumSize(QSize(0, 250))
        self.s01b01.setMaximumSize(QSize(16777215, 16777215))
        self.s01b01.setFrameShape(QFrame.NoFrame)
        self.s01b01.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.s01b01)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.s01b_g1 = QFrame(self.s01b01)
        self.s01b_g1.setObjectName(u"s01b_g1")
        self.s01b_g1.setFrameShape(QFrame.NoFrame)
        self.s01b_g1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.s01b_g1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.chart_g1 = QChartView(self.s01b_g1)
        self.chart_g1.setObjectName(u"chart_g1")
        self.chart_g1.setStyleSheet(u"")
        self.chart_g1.setResizeAnchor(QGraphicsView.NoAnchor)

        self.verticalLayout_11.addWidget(self.chart_g1)


        self.horizontalLayout_2.addWidget(self.s01b_g1)

        self.s01b_g2 = QFrame(self.s01b01)
        self.s01b_g2.setObjectName(u"s01b_g2")
        self.s01b_g2.setFrameShape(QFrame.NoFrame)
        self.s01b_g2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.s01b_g2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.chart_g2 = QChartView(self.s01b_g2)
        self.chart_g2.setObjectName(u"chart_g2")

        self.verticalLayout_16.addWidget(self.chart_g2)


        self.horizontalLayout_2.addWidget(self.s01b_g2)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.s01b01)

        self.s01b02 = QFrame(self.s01b00content)
        self.s01b02.setObjectName(u"s01b02")
        self.s01b02.setMinimumSize(QSize(0, 250))
        self.s01b02.setFrameShape(QFrame.NoFrame)
        self.s01b02.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.s01b02)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.s01b_g3 = QFrame(self.s01b02)
        self.s01b_g3.setObjectName(u"s01b_g3")
        self.s01b_g3.setFrameShape(QFrame.NoFrame)
        self.s01b_g3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.s01b_g3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.chart_g3 = QChartView(self.s01b_g3)
        self.chart_g3.setObjectName(u"chart_g3")

        self.verticalLayout_15.addWidget(self.chart_g3)


        self.horizontalLayout_3.addWidget(self.s01b_g3)

        self.s01b_g4 = QFrame(self.s01b02)
        self.s01b_g4.setObjectName(u"s01b_g4")
        self.s01b_g4.setFrameShape(QFrame.NoFrame)
        self.s01b_g4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.s01b_g4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.chart_g4 = QChartView(self.s01b_g4)
        self.chart_g4.setObjectName(u"chart_g4")

        self.verticalLayout_14.addWidget(self.chart_g4)


        self.horizontalLayout_3.addWidget(self.s01b_g4)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout.addWidget(self.s01b02)

        self.s01b03 = QFrame(self.s01b00content)
        self.s01b03.setObjectName(u"s01b03")
        self.s01b03.setMinimumSize(QSize(0, 250))
        self.s01b03.setFrameShape(QFrame.NoFrame)
        self.s01b03.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.s01b03)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.s01b_g5 = QFrame(self.s01b03)
        self.s01b_g5.setObjectName(u"s01b_g5")
        self.s01b_g5.setFrameShape(QFrame.NoFrame)
        self.s01b_g5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.s01b_g5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.chart_g5 = QChartView(self.s01b_g5)
        self.chart_g5.setObjectName(u"chart_g5")

        self.verticalLayout_18.addWidget(self.chart_g5)


        self.horizontalLayout_4.addWidget(self.s01b_g5)

        self.s01b_g6 = QFrame(self.s01b03)
        self.s01b_g6.setObjectName(u"s01b_g6")
        self.s01b_g6.setFrameShape(QFrame.NoFrame)
        self.s01b_g6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.s01b_g6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.chart_g6 = QChartView(self.s01b_g6)
        self.chart_g6.setObjectName(u"chart_g6")

        self.verticalLayout_19.addWidget(self.chart_g6)


        self.horizontalLayout_4.addWidget(self.s01b_g6)

        self.s01b_g7 = QFrame(self.s01b03)
        self.s01b_g7.setObjectName(u"s01b_g7")
        self.s01b_g7.setFrameShape(QFrame.NoFrame)
        self.s01b_g7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.s01b_g7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.chart_g7 = QChartView(self.s01b_g7)
        self.chart_g7.setObjectName(u"chart_g7")

        self.verticalLayout_20.addWidget(self.chart_g7)


        self.horizontalLayout_4.addWidget(self.s01b_g7)


        self.verticalLayout.addWidget(self.s01b03)

        self.s01b04 = QFrame(self.s01b00content)
        self.s01b04.setObjectName(u"s01b04")
        self.s01b04.setMinimumSize(QSize(0, 250))
        self.s01b04.setFrameShape(QFrame.NoFrame)
        self.s01b04.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.s01b04)
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.s01b_g8 = QFrame(self.s01b04)
        self.s01b_g8.setObjectName(u"s01b_g8")
        self.s01b_g8.setFrameShape(QFrame.NoFrame)
        self.s01b_g8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.s01b_g8)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.chart_g8 = QChartView(self.s01b_g8)
        self.chart_g8.setObjectName(u"chart_g8")

        self.verticalLayout_24.addWidget(self.chart_g8)


        self.horizontalLayout_6.addWidget(self.s01b_g8)

        self.s01b_g9 = QFrame(self.s01b04)
        self.s01b_g9.setObjectName(u"s01b_g9")
        self.s01b_g9.setFrameShape(QFrame.NoFrame)
        self.s01b_g9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.s01b_g9)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.chart_g9 = QChartView(self.s01b_g9)
        self.chart_g9.setObjectName(u"chart_g9")

        self.verticalLayout_25.addWidget(self.chart_g9)


        self.horizontalLayout_6.addWidget(self.s01b_g9)

        self.s01b_g10 = QFrame(self.s01b04)
        self.s01b_g10.setObjectName(u"s01b_g10")
        self.s01b_g10.setFrameShape(QFrame.NoFrame)
        self.s01b_g10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.s01b_g10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.chart_g10 = QChartView(self.s01b_g10)
        self.chart_g10.setObjectName(u"chart_g10")

        self.verticalLayout_26.addWidget(self.chart_g10)


        self.horizontalLayout_6.addWidget(self.s01b_g10)


        self.verticalLayout.addWidget(self.s01b04)

        self.s01b05 = QFrame(self.s01b00content)
        self.s01b05.setObjectName(u"s01b05")
        self.s01b05.setMinimumSize(QSize(0, 250))
        self.s01b05.setFrameShape(QFrame.NoFrame)
        self.s01b05.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.s01b05)
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.s01b_g11 = QFrame(self.s01b05)
        self.s01b_g11.setObjectName(u"s01b_g11")
        self.s01b_g11.setFrameShape(QFrame.NoFrame)
        self.s01b_g11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.s01b_g11)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.chart_g11 = QChartView(self.s01b_g11)
        self.chart_g11.setObjectName(u"chart_g11")

        self.verticalLayout_27.addWidget(self.chart_g11)


        self.horizontalLayout_7.addWidget(self.s01b_g11)

        self.s01b_g12 = QFrame(self.s01b05)
        self.s01b_g12.setObjectName(u"s01b_g12")
        self.s01b_g12.setFrameShape(QFrame.NoFrame)
        self.s01b_g12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.s01b_g12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.chart_g12 = QChartView(self.s01b_g12)
        self.chart_g12.setObjectName(u"chart_g12")

        self.verticalLayout_28.addWidget(self.chart_g12)


        self.horizontalLayout_7.addWidget(self.s01b_g12)

        self.s01b_g13 = QFrame(self.s01b05)
        self.s01b_g13.setObjectName(u"s01b_g13")
        self.s01b_g13.setFrameShape(QFrame.NoFrame)
        self.s01b_g13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.s01b_g13)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.chart_g13 = QChartView(self.s01b_g13)
        self.chart_g13.setObjectName(u"chart_g13")

        self.verticalLayout_29.addWidget(self.chart_g13)


        self.horizontalLayout_7.addWidget(self.s01b_g13)


        self.verticalLayout.addWidget(self.s01b05)

        self.s01b00scroll.setWidget(self.s01b00content)

        self.verticalLayout_13.addWidget(self.s01b00scroll)

        self.tabWidget.addTab(self.tab_plot_view, "")
        self.tab_focus = QWidget()
        self.tab_focus.setObjectName(u"tab_focus")
        self.verticalLayout_22 = QVBoxLayout(self.tab_focus)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(8, 24, 8, 12)
        self.tff = QFrame(self.tab_focus)
        self.tff.setObjectName(u"tff")
        self.tff.setFrameShape(QFrame.NoFrame)
        self.tff.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.tff)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(8, 8, 8, 8)
        self.s01b_gfocus = QFrame(self.tff)
        self.s01b_gfocus.setObjectName(u"s01b_gfocus")
        self.s01b_gfocus.setFrameShape(QFrame.NoFrame)
        self.s01b_gfocus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.s01b_gfocus)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.chart_focus = QChartView(self.s01b_gfocus)
        self.chart_focus.setObjectName(u"chart_focus")
        self.chart_focus.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.chart_focus)


        self.verticalLayout_23.addWidget(self.s01b_gfocus)

        self.dev_focus = QComboBox(self.tff)
        self.dev_focus.addItem("")
        self.dev_focus.addItem("")
        self.dev_focus.addItem("")
        self.dev_focus.setObjectName(u"dev_focus")
        self.dev_focus.setMinimumSize(QSize(0, 32))
        self.dev_focus.setMaximumSize(QSize(16777215, 32))
        self.dev_focus.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(92, 97, 163);\n"
"	border-radius: 8px;\n"
"	color: rgb(203, 212, 255);\n"
"	padding: 1px 0px 1px 16px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"	background-color: rgb(46, 49, 82);\n"
"}")

        self.verticalLayout_23.addWidget(self.dev_focus)


        self.verticalLayout_22.addWidget(self.tff)

        self.tabWidget.addTab(self.tab_focus, "")
        self.tab_map = QWidget()
        self.tab_map.setObjectName(u"tab_map")
        self.verticalLayout_36 = QVBoxLayout(self.tab_map)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(8, 24, 8, 8)
        self.frame_mapbox = QFrame(self.tab_map)
        self.frame_mapbox.setObjectName(u"frame_mapbox")
        self.frame_mapbox.setStyleSheet(u"")
        self.frame_mapbox.setFrameShape(QFrame.StyledPanel)
        self.frame_mapbox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_mapbox)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.web_mapbox = QWebEngineView(self.frame_mapbox)
        self.web_mapbox.setObjectName(u"web_mapbox")

        self.horizontalLayout_13.addWidget(self.web_mapbox)


        self.verticalLayout_36.addWidget(self.frame_mapbox)

        self.frame_control = QFrame(self.tab_map)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(0, 100))
        self.frame_control.setMaximumSize(QSize(16777215, 100))
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)

        self.verticalLayout_36.addWidget(self.frame_control)

        self.tabWidget.addTab(self.tab_map, "")
        self.tab_formatted_view = QWidget()
        self.tab_formatted_view.setObjectName(u"tab_formatted_view")
        self.tab_formatted_view.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_formatted_view)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(8, 24, 8, 12)
        self.tfv01 = QFrame(self.tab_formatted_view)
        self.tfv01.setObjectName(u"tfv01")
        self.tfv01.setStyleSheet(u"background-color: none;")
        self.tfv01.setFrameShape(QFrame.NoFrame)
        self.tfv01.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.tfv01)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_1 = QLabel(self.tfv01)
        self.label_1.setObjectName(u"label_1")

        self.verticalLayout_31.addWidget(self.label_1)

        self.label_2 = QLabel(self.tfv01)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_31.addWidget(self.label_2)

        self.label_3 = QLabel(self.tfv01)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_31.addWidget(self.label_3)

        self.label_4 = QLabel(self.tfv01)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_31.addWidget(self.label_4)

        self.label_5 = QLabel(self.tfv01)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_31.addWidget(self.label_5)

        self.label_6 = QLabel(self.tfv01)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_31.addWidget(self.label_6)

        self.label_7 = QLabel(self.tfv01)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_31.addWidget(self.label_7)

        self.label_8 = QLabel(self.tfv01)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_31.addWidget(self.label_8)

        self.label_9 = QLabel(self.tfv01)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_31.addWidget(self.label_9)

        self.label_10 = QLabel(self.tfv01)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_31.addWidget(self.label_10)

        self.label_11 = QLabel(self.tfv01)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_31.addWidget(self.label_11)

        self.label_12 = QLabel(self.tfv01)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_31.addWidget(self.label_12)

        self.label_13 = QLabel(self.tfv01)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_31.addWidget(self.label_13)

        self.label_14 = QLabel(self.tfv01)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_31.addWidget(self.label_14)

        self.label_15 = QLabel(self.tfv01)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_31.addWidget(self.label_15)

        self.label_16 = QLabel(self.tfv01)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_31.addWidget(self.label_16)

        self.label_17 = QLabel(self.tfv01)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_31.addWidget(self.label_17)

        self.label_18 = QLabel(self.tfv01)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_31.addWidget(self.label_18)

        self.label_19 = QLabel(self.tfv01)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_31.addWidget(self.label_19)

        self.label_20 = QLabel(self.tfv01)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_31.addWidget(self.label_20)

        self.label_21 = QLabel(self.tfv01)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_31.addWidget(self.label_21)

        self.label_22 = QLabel(self.tfv01)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_31.addWidget(self.label_22)

        self.label_23 = QLabel(self.tfv01)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_31.addWidget(self.label_23)

        self.label_24 = QLabel(self.tfv01)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_31.addWidget(self.label_24)

        self.label_25 = QLabel(self.tfv01)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_31.addWidget(self.label_25)

        self.label_26 = QLabel(self.tfv01)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_31.addWidget(self.label_26)

        self.label_27 = QLabel(self.tfv01)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_31.addWidget(self.label_27)

        self.label_28 = QLabel(self.tfv01)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_31.addWidget(self.label_28)

        self.label_29 = QLabel(self.tfv01)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_31.addWidget(self.label_29)

        self.label_30 = QLabel(self.tfv01)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_31.addWidget(self.label_30)


        self.horizontalLayout_8.addWidget(self.tfv01)

        self.tfv02 = QFrame(self.tab_formatted_view)
        self.tfv02.setObjectName(u"tfv02")
        self.tfv02.setStyleSheet(u"background-color: none;")
        self.tfv02.setFrameShape(QFrame.NoFrame)
        self.tfv02.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.tfv02)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.val_1 = QLabel(self.tfv02)
        self.val_1.setObjectName(u"val_1")

        self.verticalLayout_32.addWidget(self.val_1)

        self.val_2 = QLabel(self.tfv02)
        self.val_2.setObjectName(u"val_2")

        self.verticalLayout_32.addWidget(self.val_2)

        self.val_3 = QLabel(self.tfv02)
        self.val_3.setObjectName(u"val_3")

        self.verticalLayout_32.addWidget(self.val_3)

        self.val_4 = QLabel(self.tfv02)
        self.val_4.setObjectName(u"val_4")

        self.verticalLayout_32.addWidget(self.val_4)

        self.val_5 = QLabel(self.tfv02)
        self.val_5.setObjectName(u"val_5")

        self.verticalLayout_32.addWidget(self.val_5)

        self.val_6 = QLabel(self.tfv02)
        self.val_6.setObjectName(u"val_6")

        self.verticalLayout_32.addWidget(self.val_6)

        self.val_7 = QLabel(self.tfv02)
        self.val_7.setObjectName(u"val_7")

        self.verticalLayout_32.addWidget(self.val_7)

        self.val_8 = QLabel(self.tfv02)
        self.val_8.setObjectName(u"val_8")

        self.verticalLayout_32.addWidget(self.val_8)

        self.val_9 = QLabel(self.tfv02)
        self.val_9.setObjectName(u"val_9")

        self.verticalLayout_32.addWidget(self.val_9)

        self.val_10 = QLabel(self.tfv02)
        self.val_10.setObjectName(u"val_10")

        self.verticalLayout_32.addWidget(self.val_10)

        self.val_11 = QLabel(self.tfv02)
        self.val_11.setObjectName(u"val_11")

        self.verticalLayout_32.addWidget(self.val_11)

        self.val_12 = QLabel(self.tfv02)
        self.val_12.setObjectName(u"val_12")

        self.verticalLayout_32.addWidget(self.val_12)

        self.val_13 = QLabel(self.tfv02)
        self.val_13.setObjectName(u"val_13")

        self.verticalLayout_32.addWidget(self.val_13)

        self.val_14 = QLabel(self.tfv02)
        self.val_14.setObjectName(u"val_14")

        self.verticalLayout_32.addWidget(self.val_14)

        self.val_15 = QLabel(self.tfv02)
        self.val_15.setObjectName(u"val_15")

        self.verticalLayout_32.addWidget(self.val_15)

        self.val_16 = QLabel(self.tfv02)
        self.val_16.setObjectName(u"val_16")

        self.verticalLayout_32.addWidget(self.val_16)

        self.val_17 = QLabel(self.tfv02)
        self.val_17.setObjectName(u"val_17")

        self.verticalLayout_32.addWidget(self.val_17)

        self.val_18 = QLabel(self.tfv02)
        self.val_18.setObjectName(u"val_18")

        self.verticalLayout_32.addWidget(self.val_18)

        self.val_19 = QLabel(self.tfv02)
        self.val_19.setObjectName(u"val_19")

        self.verticalLayout_32.addWidget(self.val_19)

        self.val_20 = QLabel(self.tfv02)
        self.val_20.setObjectName(u"val_20")

        self.verticalLayout_32.addWidget(self.val_20)

        self.val_21 = QLabel(self.tfv02)
        self.val_21.setObjectName(u"val_21")

        self.verticalLayout_32.addWidget(self.val_21)

        self.val_22 = QLabel(self.tfv02)
        self.val_22.setObjectName(u"val_22")

        self.verticalLayout_32.addWidget(self.val_22)

        self.val_23 = QLabel(self.tfv02)
        self.val_23.setObjectName(u"val_23")

        self.verticalLayout_32.addWidget(self.val_23)

        self.val_24 = QLabel(self.tfv02)
        self.val_24.setObjectName(u"val_24")

        self.verticalLayout_32.addWidget(self.val_24)

        self.val_25 = QLabel(self.tfv02)
        self.val_25.setObjectName(u"val_25")

        self.verticalLayout_32.addWidget(self.val_25)

        self.val_26 = QLabel(self.tfv02)
        self.val_26.setObjectName(u"val_26")

        self.verticalLayout_32.addWidget(self.val_26)

        self.val_27 = QLabel(self.tfv02)
        self.val_27.setObjectName(u"val_27")

        self.verticalLayout_32.addWidget(self.val_27)

        self.val_28 = QLabel(self.tfv02)
        self.val_28.setObjectName(u"val_28")

        self.verticalLayout_32.addWidget(self.val_28)

        self.val_29 = QLabel(self.tfv02)
        self.val_29.setObjectName(u"val_29")

        self.verticalLayout_32.addWidget(self.val_29)

        self.val_30 = QLabel(self.tfv02)
        self.val_30.setObjectName(u"val_30")

        self.verticalLayout_32.addWidget(self.val_30)


        self.horizontalLayout_8.addWidget(self.tfv02)

        self.tfv03 = QFrame(self.tab_formatted_view)
        self.tfv03.setObjectName(u"tfv03")
        self.tfv03.setStyleSheet(u"background-color: none;")
        self.tfv03.setFrameShape(QFrame.NoFrame)
        self.tfv03.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.tfv03)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.unit_1 = QLabel(self.tfv03)
        self.unit_1.setObjectName(u"unit_1")

        self.verticalLayout_33.addWidget(self.unit_1)

        self.unit_2 = QLabel(self.tfv03)
        self.unit_2.setObjectName(u"unit_2")

        self.verticalLayout_33.addWidget(self.unit_2)

        self.unit_3 = QLabel(self.tfv03)
        self.unit_3.setObjectName(u"unit_3")

        self.verticalLayout_33.addWidget(self.unit_3)

        self.unit_4 = QLabel(self.tfv03)
        self.unit_4.setObjectName(u"unit_4")

        self.verticalLayout_33.addWidget(self.unit_4)

        self.unit_5 = QLabel(self.tfv03)
        self.unit_5.setObjectName(u"unit_5")

        self.verticalLayout_33.addWidget(self.unit_5)

        self.unit_6 = QLabel(self.tfv03)
        self.unit_6.setObjectName(u"unit_6")

        self.verticalLayout_33.addWidget(self.unit_6)

        self.unit_7 = QLabel(self.tfv03)
        self.unit_7.setObjectName(u"unit_7")

        self.verticalLayout_33.addWidget(self.unit_7)

        self.unit_8 = QLabel(self.tfv03)
        self.unit_8.setObjectName(u"unit_8")

        self.verticalLayout_33.addWidget(self.unit_8)

        self.unit_9 = QLabel(self.tfv03)
        self.unit_9.setObjectName(u"unit_9")

        self.verticalLayout_33.addWidget(self.unit_9)

        self.unit_10 = QLabel(self.tfv03)
        self.unit_10.setObjectName(u"unit_10")

        self.verticalLayout_33.addWidget(self.unit_10)

        self.unit_11 = QLabel(self.tfv03)
        self.unit_11.setObjectName(u"unit_11")

        self.verticalLayout_33.addWidget(self.unit_11)

        self.unit_12 = QLabel(self.tfv03)
        self.unit_12.setObjectName(u"unit_12")

        self.verticalLayout_33.addWidget(self.unit_12)

        self.unit_13 = QLabel(self.tfv03)
        self.unit_13.setObjectName(u"unit_13")

        self.verticalLayout_33.addWidget(self.unit_13)

        self.unit_14 = QLabel(self.tfv03)
        self.unit_14.setObjectName(u"unit_14")

        self.verticalLayout_33.addWidget(self.unit_14)

        self.unit_15 = QLabel(self.tfv03)
        self.unit_15.setObjectName(u"unit_15")

        self.verticalLayout_33.addWidget(self.unit_15)

        self.unit_16 = QLabel(self.tfv03)
        self.unit_16.setObjectName(u"unit_16")

        self.verticalLayout_33.addWidget(self.unit_16)

        self.unit_17 = QLabel(self.tfv03)
        self.unit_17.setObjectName(u"unit_17")

        self.verticalLayout_33.addWidget(self.unit_17)

        self.unit_18 = QLabel(self.tfv03)
        self.unit_18.setObjectName(u"unit_18")

        self.verticalLayout_33.addWidget(self.unit_18)

        self.unit_19 = QLabel(self.tfv03)
        self.unit_19.setObjectName(u"unit_19")

        self.verticalLayout_33.addWidget(self.unit_19)

        self.unit_20 = QLabel(self.tfv03)
        self.unit_20.setObjectName(u"unit_20")

        self.verticalLayout_33.addWidget(self.unit_20)

        self.unit_21 = QLabel(self.tfv03)
        self.unit_21.setObjectName(u"unit_21")

        self.verticalLayout_33.addWidget(self.unit_21)

        self.unit_22 = QLabel(self.tfv03)
        self.unit_22.setObjectName(u"unit_22")

        self.verticalLayout_33.addWidget(self.unit_22)

        self.unit_23 = QLabel(self.tfv03)
        self.unit_23.setObjectName(u"unit_23")

        self.verticalLayout_33.addWidget(self.unit_23)

        self.unit_24 = QLabel(self.tfv03)
        self.unit_24.setObjectName(u"unit_24")

        self.verticalLayout_33.addWidget(self.unit_24)

        self.unit_25 = QLabel(self.tfv03)
        self.unit_25.setObjectName(u"unit_25")

        self.verticalLayout_33.addWidget(self.unit_25)

        self.unit_26 = QLabel(self.tfv03)
        self.unit_26.setObjectName(u"unit_26")

        self.verticalLayout_33.addWidget(self.unit_26)

        self.unit_27 = QLabel(self.tfv03)
        self.unit_27.setObjectName(u"unit_27")

        self.verticalLayout_33.addWidget(self.unit_27)

        self.unit_28 = QLabel(self.tfv03)
        self.unit_28.setObjectName(u"unit_28")

        self.verticalLayout_33.addWidget(self.unit_28)

        self.unit_29 = QLabel(self.tfv03)
        self.unit_29.setObjectName(u"unit_29")

        self.verticalLayout_33.addWidget(self.unit_29)

        self.unit_30 = QLabel(self.tfv03)
        self.unit_30.setObjectName(u"unit_30")

        self.verticalLayout_33.addWidget(self.unit_30)


        self.horizontalLayout_8.addWidget(self.tfv03)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 2)
        self.tabWidget.addTab(self.tab_formatted_view, "")
        self.tab_command = QWidget()
        self.tab_command.setObjectName(u"tab_command")
        self.verticalLayout_34 = QVBoxLayout(self.tab_command)
        self.verticalLayout_34.setSpacing(20)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(8, 24, 8, 12)
        self.bt_uplink1 = QPushButton(self.tab_command)
        self.bt_uplink1.setObjectName(u"bt_uplink1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.bt_uplink1.sizePolicy().hasHeightForWidth())
        self.bt_uplink1.setSizePolicy(sizePolicy4)
        self.bt_uplink1.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(18)
        self.bt_uplink1.setFont(font3)
        self.bt_uplink1.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_uplink1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.verticalLayout_34.addWidget(self.bt_uplink1)

        self.bt_uplink2 = QPushButton(self.tab_command)
        self.bt_uplink2.setObjectName(u"bt_uplink2")
        sizePolicy4.setHeightForWidth(self.bt_uplink2.sizePolicy().hasHeightForWidth())
        self.bt_uplink2.setSizePolicy(sizePolicy4)
        self.bt_uplink2.setFont(font3)
        self.bt_uplink2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_uplink2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.verticalLayout_34.addWidget(self.bt_uplink2)

        self.bt_uplink3 = QPushButton(self.tab_command)
        self.bt_uplink3.setObjectName(u"bt_uplink3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.bt_uplink3.sizePolicy().hasHeightForWidth())
        self.bt_uplink3.setSizePolicy(sizePolicy5)
        self.bt_uplink3.setFont(font3)
        self.bt_uplink3.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_uplink3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.verticalLayout_34.addWidget(self.bt_uplink3)

        self.bt_uplink4 = QPushButton(self.tab_command)
        self.bt_uplink4.setObjectName(u"bt_uplink4")
        sizePolicy4.setHeightForWidth(self.bt_uplink4.sizePolicy().hasHeightForWidth())
        self.bt_uplink4.setSizePolicy(sizePolicy4)
        self.bt_uplink4.setFont(font3)
        self.bt_uplink4.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_uplink4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.verticalLayout_34.addWidget(self.bt_uplink4)

        self.bt_uplink5 = QPushButton(self.tab_command)
        self.bt_uplink5.setObjectName(u"bt_uplink5")
        sizePolicy4.setHeightForWidth(self.bt_uplink5.sizePolicy().hasHeightForWidth())
        self.bt_uplink5.setSizePolicy(sizePolicy4)
        self.bt_uplink5.setFont(font3)
        self.bt_uplink5.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_uplink5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.verticalLayout_34.addWidget(self.bt_uplink5)

        self.bt_uplink6 = QPushButton(self.tab_command)
        self.bt_uplink6.setObjectName(u"bt_uplink6")
        sizePolicy4.setHeightForWidth(self.bt_uplink6.sizePolicy().hasHeightForWidth())
        self.bt_uplink6.setSizePolicy(sizePolicy4)
        self.bt_uplink6.setFont(font3)
        self.bt_uplink6.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_uplink6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.verticalLayout_34.addWidget(self.bt_uplink6)

        self.tabWidget.addTab(self.tab_command, "")
        self.tab_serial_monitor = QWidget()
        self.tab_serial_monitor.setObjectName(u"tab_serial_monitor")
        self.verticalLayout_17 = QVBoxLayout(self.tab_serial_monitor)
        self.verticalLayout_17.setSpacing(12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(8, 24, 8, 8)
        self.tsm_frame = QFrame(self.tab_serial_monitor)
        self.tsm_frame.setObjectName(u"tsm_frame")
        self.tsm_frame.setMinimumSize(QSize(0, 30))
        self.tsm_frame.setMaximumSize(QSize(16777215, 30))
        self.tsm_frame.setFrameShape(QFrame.NoFrame)
        self.tsm_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.tsm_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.line_serial_write = QLineEdit(self.tsm_frame)
        self.line_serial_write.setObjectName(u"line_serial_write")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.line_serial_write.sizePolicy().hasHeightForWidth())
        self.line_serial_write.setSizePolicy(sizePolicy6)
        self.line_serial_write.setStyleSheet(u"background-color: rgb(203, 212, 255);\n"
"color: rgb(46, 49, 82);\n"
"border-radius: 10px;")
        self.line_serial_write.setEchoMode(QLineEdit.Normal)
        self.line_serial_write.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.line_serial_write.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.line_serial_write)

        self.bt_serial_write = QPushButton(self.tsm_frame)
        self.bt_serial_write.setObjectName(u"bt_serial_write")
        sizePolicy1.setHeightForWidth(self.bt_serial_write.sizePolicy().hasHeightForWidth())
        self.bt_serial_write.setSizePolicy(sizePolicy1)
        self.bt_serial_write.setMinimumSize(QSize(64, 0))
        self.bt_serial_write.setMaximumSize(QSize(64, 16777215))
        self.bt_serial_write.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_serial_write.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(93, 99, 166,240);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(93, 99, 166,128);\n"
"}")

        self.horizontalLayout_5.addWidget(self.bt_serial_write)


        self.verticalLayout_17.addWidget(self.tsm_frame)

        self.line_serial_read = QTextEdit(self.tab_serial_monitor)
        self.line_serial_read.setObjectName(u"line_serial_read")
        self.line_serial_read.setStyleSheet(u"background-color: rgb(203, 212, 255);\n"
"color: rgb(46, 49, 82);\n"
"border-radius: 10px;")
        self.line_serial_read.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.line_serial_read)

        self.tabWidget.addTab(self.tab_serial_monitor, "")
        self.tab_debug = QWidget()
        self.tab_debug.setObjectName(u"tab_debug")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_debug)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(8, 24, 8, 12)
        self.frame_stat_left = QFrame(self.tab_debug)
        self.frame_stat_left.setObjectName(u"frame_stat_left")
        self.frame_stat_left.setStyleSheet(u"font-weight: bold;")
        self.frame_stat_left.setFrameShape(QFrame.StyledPanel)
        self.frame_stat_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_stat_left)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.stat = QLabel(self.frame_stat_left)
        self.stat.setObjectName(u"stat")

        self.verticalLayout_37.addWidget(self.stat)

        self.stat_2 = QLabel(self.frame_stat_left)
        self.stat_2.setObjectName(u"stat_2")

        self.verticalLayout_37.addWidget(self.stat_2)

        self.stat_3 = QLabel(self.frame_stat_left)
        self.stat_3.setObjectName(u"stat_3")

        self.verticalLayout_37.addWidget(self.stat_3)

        self.stat_4 = QLabel(self.frame_stat_left)
        self.stat_4.setObjectName(u"stat_4")

        self.verticalLayout_37.addWidget(self.stat_4)

        self.stat_5 = QLabel(self.frame_stat_left)
        self.stat_5.setObjectName(u"stat_5")

        self.verticalLayout_37.addWidget(self.stat_5)

        self.stat_6 = QLabel(self.frame_stat_left)
        self.stat_6.setObjectName(u"stat_6")

        self.verticalLayout_37.addWidget(self.stat_6)

        self.stat_7 = QLabel(self.frame_stat_left)
        self.stat_7.setObjectName(u"stat_7")

        self.verticalLayout_37.addWidget(self.stat_7)

        self.stat_8 = QLabel(self.frame_stat_left)
        self.stat_8.setObjectName(u"stat_8")

        self.verticalLayout_37.addWidget(self.stat_8)

        self.stat_9 = QLabel(self.frame_stat_left)
        self.stat_9.setObjectName(u"stat_9")

        self.verticalLayout_37.addWidget(self.stat_9)

        self.stat_10 = QLabel(self.frame_stat_left)
        self.stat_10.setObjectName(u"stat_10")

        self.verticalLayout_37.addWidget(self.stat_10)

        self.stat_11 = QLabel(self.frame_stat_left)
        self.stat_11.setObjectName(u"stat_11")

        self.verticalLayout_37.addWidget(self.stat_11)

        self.stat_12 = QLabel(self.frame_stat_left)
        self.stat_12.setObjectName(u"stat_12")

        self.verticalLayout_37.addWidget(self.stat_12)

        self.stat_13 = QLabel(self.frame_stat_left)
        self.stat_13.setObjectName(u"stat_13")

        self.verticalLayout_37.addWidget(self.stat_13)

        self.stat_14 = QLabel(self.frame_stat_left)
        self.stat_14.setObjectName(u"stat_14")

        self.verticalLayout_37.addWidget(self.stat_14)

        self.stat_15 = QLabel(self.frame_stat_left)
        self.stat_15.setObjectName(u"stat_15")

        self.verticalLayout_37.addWidget(self.stat_15)

        self.space_fr = QFrame(self.frame_stat_left)
        self.space_fr.setObjectName(u"space_fr")
        self.space_fr.setMinimumSize(QSize(0, 200))
        self.space_fr.setFrameShape(QFrame.StyledPanel)
        self.space_fr.setFrameShadow(QFrame.Raised)

        self.verticalLayout_37.addWidget(self.space_fr)


        self.horizontalLayout_14.addWidget(self.frame_stat_left)

        self.frame_stat_right = QFrame(self.tab_debug)
        self.frame_stat_right.setObjectName(u"frame_stat_right")
        self.frame_stat_right.setFrameShape(QFrame.StyledPanel)
        self.frame_stat_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_stat_right)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.stat2 = QLabel(self.frame_stat_right)
        self.stat2.setObjectName(u"stat2")

        self.verticalLayout_38.addWidget(self.stat2)

        self.stat2_2 = QLabel(self.frame_stat_right)
        self.stat2_2.setObjectName(u"stat2_2")

        self.verticalLayout_38.addWidget(self.stat2_2)

        self.stat2_3 = QLabel(self.frame_stat_right)
        self.stat2_3.setObjectName(u"stat2_3")

        self.verticalLayout_38.addWidget(self.stat2_3)

        self.stat2_4 = QLabel(self.frame_stat_right)
        self.stat2_4.setObjectName(u"stat2_4")

        self.verticalLayout_38.addWidget(self.stat2_4)

        self.stat2_5 = QLabel(self.frame_stat_right)
        self.stat2_5.setObjectName(u"stat2_5")

        self.verticalLayout_38.addWidget(self.stat2_5)

        self.stat2_6 = QLabel(self.frame_stat_right)
        self.stat2_6.setObjectName(u"stat2_6")

        self.verticalLayout_38.addWidget(self.stat2_6)

        self.stat2_7 = QLabel(self.frame_stat_right)
        self.stat2_7.setObjectName(u"stat2_7")

        self.verticalLayout_38.addWidget(self.stat2_7)

        self.stat2_8 = QLabel(self.frame_stat_right)
        self.stat2_8.setObjectName(u"stat2_8")

        self.verticalLayout_38.addWidget(self.stat2_8)

        self.stat2_9 = QLabel(self.frame_stat_right)
        self.stat2_9.setObjectName(u"stat2_9")

        self.verticalLayout_38.addWidget(self.stat2_9)

        self.stat2_10 = QLabel(self.frame_stat_right)
        self.stat2_10.setObjectName(u"stat2_10")

        self.verticalLayout_38.addWidget(self.stat2_10)

        self.stat2_11 = QLabel(self.frame_stat_right)
        self.stat2_11.setObjectName(u"stat2_11")

        self.verticalLayout_38.addWidget(self.stat2_11)

        self.stat2_12 = QLabel(self.frame_stat_right)
        self.stat2_12.setObjectName(u"stat2_12")

        self.verticalLayout_38.addWidget(self.stat2_12)

        self.stat2_13 = QLabel(self.frame_stat_right)
        self.stat2_13.setObjectName(u"stat2_13")

        self.verticalLayout_38.addWidget(self.stat2_13)

        self.stat2_14 = QLabel(self.frame_stat_right)
        self.stat2_14.setObjectName(u"stat2_14")

        self.verticalLayout_38.addWidget(self.stat2_14)

        self.stat2_15 = QLabel(self.frame_stat_right)
        self.stat2_15.setObjectName(u"stat2_15")

        self.verticalLayout_38.addWidget(self.stat2_15)

        self.space_fr_2 = QFrame(self.frame_stat_right)
        self.space_fr_2.setObjectName(u"space_fr_2")
        self.space_fr_2.setMinimumSize(QSize(0, 200))
        self.space_fr_2.setFrameShape(QFrame.StyledPanel)
        self.space_fr_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.space_fr_2)


        self.horizontalLayout_14.addWidget(self.frame_stat_right)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 2)
        self.tabWidget.addTab(self.tab_debug, "")

        self.verticalLayout_12.addWidget(self.tabWidget)


        self.verticalLayout_35.addWidget(self.s01b01_2)


        self.horizontalLayout.addWidget(self.s01b)


        self.verticalLayout_30.addWidget(self.s01)

        HomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeWindow)

        self.bt_connect.setDefault(True)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("HomeWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("HomeWindow", u"Save as...", None))
        self.actionRefresh.setText(QCoreApplication.translate("HomeWindow", u"Refresh", None))
        self.actionPreferences.setText(QCoreApplication.translate("HomeWindow", u"Preferences", None))
        self.actionAbout.setText(QCoreApplication.translate("HomeWindow", u"About", None))
        self.actionStart.setText(QCoreApplication.translate("HomeWindow", u"Start", None))
        self.actionPause.setText(QCoreApplication.translate("HomeWindow", u"Pause", None))
        self.actionStop.setText(QCoreApplication.translate("HomeWindow", u"Stop", None))
        self.actionReset.setText(QCoreApplication.translate("HomeWindow", u"Reset", None))
        self.bt_close.setText("")
        self.bt_minimize.setText("")
        self.bt_maximize.setText("")
        self.sys_title.setText(QCoreApplication.translate("HomeWindow", u"Project Hermetica", None))
        self.sys_clock.setText(QCoreApplication.translate("HomeWindow", u"11:53:1x", None))
        self.sys_stopwatch.setText(QCoreApplication.translate("HomeWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">11:53:12</span></p></body></html>", None))
        self.sys_com.setText(QCoreApplication.translate("HomeWindow", u"Device Port", None))
        self.dev_com.setItemText(0, QCoreApplication.translate("HomeWindow", u"Select Paired Device", None))

        self.sys_baud.setText(QCoreApplication.translate("HomeWindow", u"Baudrate", None))
        self.dev_baud.setItemText(0, QCoreApplication.translate("HomeWindow", u"9600", None))
        self.dev_baud.setItemText(1, QCoreApplication.translate("HomeWindow", u"4800", None))
        self.dev_baud.setItemText(2, QCoreApplication.translate("HomeWindow", u"19200", None))
        self.dev_baud.setItemText(3, QCoreApplication.translate("HomeWindow", u"38400", None))
        self.dev_baud.setItemText(4, QCoreApplication.translate("HomeWindow", u"57600", None))
        self.dev_baud.setItemText(5, QCoreApplication.translate("HomeWindow", u"115200", None))

        self.bt_connect.setText(QCoreApplication.translate("HomeWindow", u"Connect", None))
        self.bt_disconnect.setText(QCoreApplication.translate("HomeWindow", u"Disconnect", None))
        self.bt_refresh.setText(QCoreApplication.translate("HomeWindow", u"Refresh", None))
        self.bt_preferences.setText(QCoreApplication.translate("HomeWindow", u"Preferences", None))
        self.bt_clear_chart.setText(QCoreApplication.translate("HomeWindow", u"Clear Chart", None))
        self.bt_pop_chart.setText(QCoreApplication.translate("HomeWindow", u"Pop Chart", None))
        self.bt_timer_start.setText(QCoreApplication.translate("HomeWindow", u"Start", None))
        self.bt_timer_pause.setText(QCoreApplication.translate("HomeWindow", u"Pause", None))
        self.bt_timer_reset.setText(QCoreApplication.translate("HomeWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_plot_view), QCoreApplication.translate("HomeWindow", u"Plot View", None))
        self.dev_focus.setItemText(0, QCoreApplication.translate("HomeWindow", u"Altitude (m)", None))
        self.dev_focus.setItemText(1, QCoreApplication.translate("HomeWindow", u"Temperature (\u00b0C)", None))
        self.dev_focus.setItemText(2, QCoreApplication.translate("HomeWindow", u"Barometric Pressure (hPa)", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_focus), QCoreApplication.translate("HomeWindow", u"Focus View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_map), QCoreApplication.translate("HomeWindow", u"Map", None))
        self.label_1.setText(QCoreApplication.translate("HomeWindow", u"Lb1", None))
        self.label_2.setText(QCoreApplication.translate("HomeWindow", u"Lb2", None))
        self.label_3.setText(QCoreApplication.translate("HomeWindow", u"Lb3", None))
        self.label_4.setText(QCoreApplication.translate("HomeWindow", u"Lb4", None))
        self.label_5.setText(QCoreApplication.translate("HomeWindow", u"Lb5", None))
        self.label_6.setText(QCoreApplication.translate("HomeWindow", u"Lb6", None))
        self.label_7.setText(QCoreApplication.translate("HomeWindow", u"Lb7", None))
        self.label_8.setText(QCoreApplication.translate("HomeWindow", u"Lb8", None))
        self.label_9.setText(QCoreApplication.translate("HomeWindow", u"Lb9", None))
        self.label_10.setText(QCoreApplication.translate("HomeWindow", u"Lb10", None))
        self.label_11.setText(QCoreApplication.translate("HomeWindow", u"Lb11", None))
        self.label_12.setText(QCoreApplication.translate("HomeWindow", u"Lb12", None))
        self.label_13.setText(QCoreApplication.translate("HomeWindow", u"Lb13", None))
        self.label_14.setText(QCoreApplication.translate("HomeWindow", u"Lb14", None))
        self.label_15.setText(QCoreApplication.translate("HomeWindow", u"Lb15", None))
        self.label_16.setText(QCoreApplication.translate("HomeWindow", u"Lb16", None))
        self.label_17.setText(QCoreApplication.translate("HomeWindow", u"Lb17", None))
        self.label_18.setText(QCoreApplication.translate("HomeWindow", u"Lb18", None))
        self.label_19.setText(QCoreApplication.translate("HomeWindow", u"Lb19", None))
        self.label_20.setText(QCoreApplication.translate("HomeWindow", u"Lb20", None))
        self.label_21.setText(QCoreApplication.translate("HomeWindow", u"Lb21", None))
        self.label_22.setText(QCoreApplication.translate("HomeWindow", u"Lb22", None))
        self.label_23.setText(QCoreApplication.translate("HomeWindow", u"Lb23", None))
        self.label_24.setText(QCoreApplication.translate("HomeWindow", u"Lb24", None))
        self.label_25.setText(QCoreApplication.translate("HomeWindow", u"Lb25", None))
        self.label_26.setText(QCoreApplication.translate("HomeWindow", u"Lb26", None))
        self.label_27.setText(QCoreApplication.translate("HomeWindow", u"Lb27", None))
        self.label_28.setText(QCoreApplication.translate("HomeWindow", u"Lb28", None))
        self.label_29.setText(QCoreApplication.translate("HomeWindow", u"Lb29", None))
        self.label_30.setText(QCoreApplication.translate("HomeWindow", u"Lb30", None))
        self.val_1.setText(QCoreApplication.translate("HomeWindow", u"Lb1", None))
        self.val_2.setText(QCoreApplication.translate("HomeWindow", u"Lb2", None))
        self.val_3.setText(QCoreApplication.translate("HomeWindow", u"Lb3", None))
        self.val_4.setText(QCoreApplication.translate("HomeWindow", u"Lb4", None))
        self.val_5.setText(QCoreApplication.translate("HomeWindow", u"Lb5", None))
        self.val_6.setText(QCoreApplication.translate("HomeWindow", u"Lb6", None))
        self.val_7.setText(QCoreApplication.translate("HomeWindow", u"Lb7", None))
        self.val_8.setText(QCoreApplication.translate("HomeWindow", u"Lb8", None))
        self.val_9.setText(QCoreApplication.translate("HomeWindow", u"Lb9", None))
        self.val_10.setText(QCoreApplication.translate("HomeWindow", u"Lb10", None))
        self.val_11.setText(QCoreApplication.translate("HomeWindow", u"Lb11", None))
        self.val_12.setText(QCoreApplication.translate("HomeWindow", u"Lb12", None))
        self.val_13.setText(QCoreApplication.translate("HomeWindow", u"Lb13", None))
        self.val_14.setText(QCoreApplication.translate("HomeWindow", u"Lb14", None))
        self.val_15.setText(QCoreApplication.translate("HomeWindow", u"Lb15", None))
        self.val_16.setText(QCoreApplication.translate("HomeWindow", u"Lb16", None))
        self.val_17.setText(QCoreApplication.translate("HomeWindow", u"Lb17", None))
        self.val_18.setText(QCoreApplication.translate("HomeWindow", u"Lb18", None))
        self.val_19.setText(QCoreApplication.translate("HomeWindow", u"Lb19", None))
        self.val_20.setText(QCoreApplication.translate("HomeWindow", u"Lb20", None))
        self.val_21.setText(QCoreApplication.translate("HomeWindow", u"Lb21", None))
        self.val_22.setText(QCoreApplication.translate("HomeWindow", u"Lb22", None))
        self.val_23.setText(QCoreApplication.translate("HomeWindow", u"Lb23", None))
        self.val_24.setText(QCoreApplication.translate("HomeWindow", u"Lb24", None))
        self.val_25.setText(QCoreApplication.translate("HomeWindow", u"Lb25", None))
        self.val_26.setText(QCoreApplication.translate("HomeWindow", u"Lb26", None))
        self.val_27.setText(QCoreApplication.translate("HomeWindow", u"Lb27", None))
        self.val_28.setText(QCoreApplication.translate("HomeWindow", u"Lb28", None))
        self.val_29.setText(QCoreApplication.translate("HomeWindow", u"Lb29", None))
        self.val_30.setText(QCoreApplication.translate("HomeWindow", u"Lb30", None))
        self.unit_1.setText(QCoreApplication.translate("HomeWindow", u"Lb1", None))
        self.unit_2.setText(QCoreApplication.translate("HomeWindow", u"Lb2", None))
        self.unit_3.setText(QCoreApplication.translate("HomeWindow", u"Lb3", None))
        self.unit_4.setText(QCoreApplication.translate("HomeWindow", u"Lb4", None))
        self.unit_5.setText(QCoreApplication.translate("HomeWindow", u"Lb5", None))
        self.unit_6.setText(QCoreApplication.translate("HomeWindow", u"Lb6", None))
        self.unit_7.setText(QCoreApplication.translate("HomeWindow", u"Lb7", None))
        self.unit_8.setText(QCoreApplication.translate("HomeWindow", u"Lb8", None))
        self.unit_9.setText(QCoreApplication.translate("HomeWindow", u"Lb9", None))
        self.unit_10.setText(QCoreApplication.translate("HomeWindow", u"Lb10", None))
        self.unit_11.setText(QCoreApplication.translate("HomeWindow", u"Lb11", None))
        self.unit_12.setText(QCoreApplication.translate("HomeWindow", u"Lb12", None))
        self.unit_13.setText(QCoreApplication.translate("HomeWindow", u"Lb13", None))
        self.unit_14.setText(QCoreApplication.translate("HomeWindow", u"Lb14", None))
        self.unit_15.setText(QCoreApplication.translate("HomeWindow", u"Lb15", None))
        self.unit_16.setText(QCoreApplication.translate("HomeWindow", u"Lb16", None))
        self.unit_17.setText(QCoreApplication.translate("HomeWindow", u"Lb17", None))
        self.unit_18.setText(QCoreApplication.translate("HomeWindow", u"Lb18", None))
        self.unit_19.setText(QCoreApplication.translate("HomeWindow", u"Lb19", None))
        self.unit_20.setText(QCoreApplication.translate("HomeWindow", u"Lb20", None))
        self.unit_21.setText(QCoreApplication.translate("HomeWindow", u"Lb21", None))
        self.unit_22.setText(QCoreApplication.translate("HomeWindow", u"Lb22", None))
        self.unit_23.setText(QCoreApplication.translate("HomeWindow", u"Lb23", None))
        self.unit_24.setText(QCoreApplication.translate("HomeWindow", u"Lb24", None))
        self.unit_25.setText(QCoreApplication.translate("HomeWindow", u"Lb25", None))
        self.unit_26.setText(QCoreApplication.translate("HomeWindow", u"Lb26", None))
        self.unit_27.setText(QCoreApplication.translate("HomeWindow", u"Lb27", None))
        self.unit_28.setText(QCoreApplication.translate("HomeWindow", u"Lb28", None))
        self.unit_29.setText(QCoreApplication.translate("HomeWindow", u"Lb29", None))
        self.unit_30.setText(QCoreApplication.translate("HomeWindow", u"Lb30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_formatted_view), QCoreApplication.translate("HomeWindow", u"Format", None))
        self.bt_uplink1.setText(QCoreApplication.translate("HomeWindow", u"Command 1", None))
        self.bt_uplink2.setText(QCoreApplication.translate("HomeWindow", u"Command 2", None))
        self.bt_uplink3.setText(QCoreApplication.translate("HomeWindow", u"Command 3", None))
        self.bt_uplink4.setText(QCoreApplication.translate("HomeWindow", u"Command 4", None))
        self.bt_uplink5.setText(QCoreApplication.translate("HomeWindow", u"Command 5", None))
        self.bt_uplink6.setText(QCoreApplication.translate("HomeWindow", u"Command 6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_command), QCoreApplication.translate("HomeWindow", u"Command", None))
        self.line_serial_write.setText("")
        self.line_serial_write.setPlaceholderText(QCoreApplication.translate("HomeWindow", u"Type command here to send to the connected device", None))
        self.bt_serial_write.setText(QCoreApplication.translate("HomeWindow", u"Write", None))
        self.line_serial_read.setPlaceholderText(QCoreApplication.translate("HomeWindow", u"Raw input data from the connected device will appear here.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_serial_monitor), QCoreApplication.translate("HomeWindow", u"Serial Monitor", None))
        self.stat.setText(QCoreApplication.translate("HomeWindow", u"Platform Name", None))
        self.stat_2.setText(QCoreApplication.translate("HomeWindow", u"Platform Release", None))
        self.stat_3.setText(QCoreApplication.translate("HomeWindow", u"Platform Architecture", None))
        self.stat_4.setText(QCoreApplication.translate("HomeWindow", u"Platform Version (Detailed)", None))
        self.stat_5.setText(QCoreApplication.translate("HomeWindow", u"Platform Device Theme", None))
        self.stat_6.setText(QCoreApplication.translate("HomeWindow", u"Device Status", None))
        self.stat_7.setText(QCoreApplication.translate("HomeWindow", u"Connected Device Name", None))
        self.stat_8.setText(QCoreApplication.translate("HomeWindow", u"MQTT Status", None))
        self.stat_9.setText(QCoreApplication.translate("HomeWindow", u"Socket Status", None))
        self.stat_10.setText(QCoreApplication.translate("HomeWindow", u"Project Name", None))
        self.stat_11.setText(QCoreApplication.translate("HomeWindow", u"Number of Data", None))
        self.stat_12.setText(QCoreApplication.translate("HomeWindow", u"Number of Charts", None))
        self.stat_13.setText("")
        self.stat_14.setText("")
        self.stat_15.setText("")
        self.stat2.setText("")
        self.stat2_2.setText("")
        self.stat2_3.setText("")
        self.stat2_4.setText("")
        self.stat2_5.setText("")
        self.stat2_6.setText("")
        self.stat2_7.setText("")
        self.stat2_8.setText("")
        self.stat2_9.setText("")
        self.stat2_10.setText("")
        self.stat2_11.setText("")
        self.stat2_12.setText("")
        self.stat2_13.setText("")
        self.stat2_14.setText("")
        self.stat2_15.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_debug), QCoreApplication.translate("HomeWindow", u"Debug", None))
    # retranslateUi

