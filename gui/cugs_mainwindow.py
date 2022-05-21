# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cugs_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 800)
        MainWindow.setMinimumSize(QSize(960, 800))
        MainWindow.setStyleSheet(u"")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 0)
        self.fr_cen_1 = QFrame(self.centralwidget)
        self.fr_cen_1.setObjectName(u"fr_cen_1")
        self.fr_cen_1.setMaximumSize(QSize(16777215, 160))
        self.fr_cen_1.setFrameShape(QFrame.StyledPanel)
        self.fr_cen_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_cen_1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_Cmd = QTabWidget(self.fr_cen_1)
        self.tabWidget_Cmd.setObjectName(u"tabWidget_Cmd")
        self.tabWidget_Cmd.setTabPosition(QTabWidget.North)
        self.tab_serial = QWidget()
        self.tab_serial.setObjectName(u"tab_serial")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_serial)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fr_data_capture_2 = QFrame(self.tab_serial)
        self.fr_data_capture_2.setObjectName(u"fr_data_capture_2")
        self.fr_data_capture_2.setMaximumSize(QSize(650, 16777215))
        self.fr_data_capture_2.setFrameShape(QFrame.StyledPanel)
        self.fr_data_capture_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.fr_data_capture_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.fr_d_c_cmd_2 = QFrame(self.fr_data_capture_2)
        self.fr_d_c_cmd_2.setObjectName(u"fr_d_c_cmd_2")
        self.fr_d_c_cmd_2.setMinimumSize(QSize(650, 0))
        self.fr_d_c_cmd_2.setMaximumSize(QSize(650, 16777215))
        self.fr_d_c_cmd_2.setFrameShape(QFrame.StyledPanel)
        self.fr_d_c_cmd_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.fr_d_c_cmd_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.fr_serial_sel = QFrame(self.fr_d_c_cmd_2)
        self.fr_serial_sel.setObjectName(u"fr_serial_sel")
        self.fr_serial_sel.setMinimumSize(QSize(350, 0))
        self.fr_serial_sel.setMaximumSize(QSize(350, 16777215))
        self.fr_serial_sel.setFrameShape(QFrame.StyledPanel)
        self.fr_serial_sel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.fr_serial_sel)
        self.verticalLayout_27.setSpacing(4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(20, 0, 20, 0)
        self.label = QLabel(self.fr_serial_sel)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_27.addWidget(self.label)

        self.combo_serial = QComboBox(self.fr_serial_sel)
        self.combo_serial.setObjectName(u"combo_serial")

        self.verticalLayout_27.addWidget(self.combo_serial)

        self.label_2 = QLabel(self.fr_serial_sel)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setFont(font)

        self.verticalLayout_27.addWidget(self.label_2)

        self.combo_baud = QComboBox(self.fr_serial_sel)
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.setObjectName(u"combo_baud")

        self.verticalLayout_27.addWidget(self.combo_baud)


        self.horizontalLayout_6.addWidget(self.fr_serial_sel)

        self.fr_serial_btn = QFrame(self.fr_d_c_cmd_2)
        self.fr_serial_btn.setObjectName(u"fr_serial_btn")
        self.fr_serial_btn.setMinimumSize(QSize(0, 0))
        self.fr_serial_btn.setMaximumSize(QSize(16777215, 16777215))
        self.fr_serial_btn.setFrameShape(QFrame.StyledPanel)
        self.fr_serial_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.fr_serial_btn)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 10, 20, 10)
        self.btn_serial_connect = QPushButton(self.fr_serial_btn)
        self.btn_serial_connect.setObjectName(u"btn_serial_connect")
        self.btn_serial_connect.setMinimumSize(QSize(120, 40))
        self.btn_serial_connect.setMaximumSize(QSize(99999, 40))
        self.btn_serial_connect.setFont(font)
        self.btn_serial_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_serial_connect.setCheckable(False)
        self.btn_serial_connect.setChecked(False)
        self.btn_serial_connect.setAutoDefault(True)

        self.verticalLayout_13.addWidget(self.btn_serial_connect)

        self.fr_bot_btn = QFrame(self.fr_serial_btn)
        self.fr_bot_btn.setObjectName(u"fr_bot_btn")
        self.fr_bot_btn.setFrameShape(QFrame.StyledPanel)
        self.fr_bot_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.fr_bot_btn)
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_serial_refresh = QPushButton(self.fr_bot_btn)
        self.btn_serial_refresh.setObjectName(u"btn_serial_refresh")
        self.btn_serial_refresh.setMinimumSize(QSize(120, 40))
        self.btn_serial_refresh.setMaximumSize(QSize(240, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_serial_refresh.setFont(font1)
        self.btn_serial_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_serial_refresh.setCheckable(False)
        self.btn_serial_refresh.setChecked(False)

        self.horizontalLayout_7.addWidget(self.btn_serial_refresh)

        self.btn_serial_disconnect = QPushButton(self.fr_bot_btn)
        self.btn_serial_disconnect.setObjectName(u"btn_serial_disconnect")
        self.btn_serial_disconnect.setMinimumSize(QSize(120, 40))
        self.btn_serial_disconnect.setMaximumSize(QSize(240, 40))
        self.btn_serial_disconnect.setFont(font)
        self.btn_serial_disconnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_serial_disconnect.setStyleSheet(u"color: rgb(222, 0, 0);")
        self.btn_serial_disconnect.setCheckable(False)
        self.btn_serial_disconnect.setChecked(False)

        self.horizontalLayout_7.addWidget(self.btn_serial_disconnect)


        self.verticalLayout_13.addWidget(self.fr_bot_btn)


        self.horizontalLayout_6.addWidget(self.fr_serial_btn)

        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 6)

        self.verticalLayout_8.addWidget(self.fr_d_c_cmd_2)

        self.fr_d_c_name_2 = QFrame(self.fr_data_capture_2)
        self.fr_d_c_name_2.setObjectName(u"fr_d_c_name_2")
        self.fr_d_c_name_2.setMaximumSize(QSize(16777215, 20))
        self.fr_d_c_name_2.setFrameShape(QFrame.StyledPanel)
        self.fr_d_c_name_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.fr_d_c_name_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lb_fr_d_c_2 = QLabel(self.fr_d_c_name_2)
        self.lb_fr_d_c_2.setObjectName(u"lb_fr_d_c_2")
        self.lb_fr_d_c_2.setFont(font1)
        self.lb_fr_d_c_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lb_fr_d_c_2)


        self.verticalLayout_8.addWidget(self.fr_d_c_name_2)


        self.horizontalLayout_3.addWidget(self.fr_data_capture_2)

        self.fr_image_data_2 = QFrame(self.tab_serial)
        self.fr_image_data_2.setObjectName(u"fr_image_data_2")
        self.fr_image_data_2.setFrameShape(QFrame.StyledPanel)
        self.fr_image_data_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.fr_image_data_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.fr_i_d_cmd_2 = QFrame(self.fr_image_data_2)
        self.fr_i_d_cmd_2.setObjectName(u"fr_i_d_cmd_2")
        self.fr_i_d_cmd_2.setFrameShape(QFrame.StyledPanel)
        self.fr_i_d_cmd_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.fr_i_d_cmd_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.text_serial_info = QPlainTextEdit(self.fr_i_d_cmd_2)
        self.text_serial_info.setObjectName(u"text_serial_info")

        self.horizontalLayout_8.addWidget(self.text_serial_info)


        self.verticalLayout_10.addWidget(self.fr_i_d_cmd_2)

        self.fr_i_d_name_2 = QFrame(self.fr_image_data_2)
        self.fr_i_d_name_2.setObjectName(u"fr_i_d_name_2")
        self.fr_i_d_name_2.setMaximumSize(QSize(16777215, 20))
        self.fr_i_d_name_2.setFrameShape(QFrame.StyledPanel)
        self.fr_i_d_name_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.fr_i_d_name_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lb_fr_i_d_2 = QLabel(self.fr_i_d_name_2)
        self.lb_fr_i_d_2.setObjectName(u"lb_fr_i_d_2")
        self.lb_fr_i_d_2.setFont(font1)
        self.lb_fr_i_d_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lb_fr_i_d_2)


        self.verticalLayout_10.addWidget(self.fr_i_d_name_2)


        self.horizontalLayout_3.addWidget(self.fr_image_data_2)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.tabWidget_Cmd.addTab(self.tab_serial, "")
        self.tab_data = QWidget()
        self.tab_data.setObjectName(u"tab_data")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_data)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr_mission_control = QFrame(self.tab_data)
        self.fr_mission_control.setObjectName(u"fr_mission_control")
        self.fr_mission_control.setFrameShape(QFrame.StyledPanel)
        self.fr_mission_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_mission_control)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr_m_c_cmd = QFrame(self.fr_mission_control)
        self.fr_m_c_cmd.setObjectName(u"fr_m_c_cmd")
        self.fr_m_c_cmd.setFrameShape(QFrame.StyledPanel)
        self.fr_m_c_cmd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fr_m_c_cmd)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.fr_cb_write = QFrame(self.fr_m_c_cmd)
        self.fr_cb_write.setObjectName(u"fr_cb_write")
        self.fr_cb_write.setFrameShape(QFrame.StyledPanel)
        self.fr_cb_write.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.fr_cb_write)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.cb_write_log = QCheckBox(self.fr_cb_write)
        self.cb_write_log.setObjectName(u"cb_write_log")
        font2 = QFont()
        font2.setPointSize(12)
        self.cb_write_log.setFont(font2)
        self.cb_write_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_write_log.setChecked(True)

        self.verticalLayout_12.addWidget(self.cb_write_log)

        self.cb_write_kml = QCheckBox(self.fr_cb_write)
        self.cb_write_kml.setObjectName(u"cb_write_kml")
        self.cb_write_kml.setFont(font2)
        self.cb_write_kml.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_write_kml.setChecked(True)

        self.verticalLayout_12.addWidget(self.cb_write_kml)


        self.horizontalLayout_4.addWidget(self.fr_cb_write)

        self.btn_start_mission = QPushButton(self.fr_m_c_cmd)
        self.btn_start_mission.setObjectName(u"btn_start_mission")
        self.btn_start_mission.setMinimumSize(QSize(90, 90))
        self.btn_start_mission.setMaximumSize(QSize(120, 90))
        self.btn_start_mission.setFont(font)
        self.btn_start_mission.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_mission.setCheckable(True)
        self.btn_start_mission.setChecked(False)

        self.horizontalLayout_4.addWidget(self.btn_start_mission)


        self.verticalLayout_2.addWidget(self.fr_m_c_cmd)

        self.fr_m_c_name = QFrame(self.fr_mission_control)
        self.fr_m_c_name.setObjectName(u"fr_m_c_name")
        self.fr_m_c_name.setMaximumSize(QSize(16777215, 20))
        self.fr_m_c_name.setFrameShape(QFrame.StyledPanel)
        self.fr_m_c_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fr_m_c_name)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_fr_m_c = QLabel(self.fr_m_c_name)
        self.lb_fr_m_c.setObjectName(u"lb_fr_m_c")
        self.lb_fr_m_c.setFont(font1)
        self.lb_fr_m_c.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_fr_m_c)


        self.verticalLayout_2.addWidget(self.fr_m_c_name)


        self.horizontalLayout_2.addWidget(self.fr_mission_control)

        self.fr_data_capture = QFrame(self.tab_data)
        self.fr_data_capture.setObjectName(u"fr_data_capture")
        self.fr_data_capture.setFrameShape(QFrame.StyledPanel)
        self.fr_data_capture.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.fr_data_capture)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.fr_d_c_cmd = QFrame(self.fr_data_capture)
        self.fr_d_c_cmd.setObjectName(u"fr_d_c_cmd")
        self.fr_d_c_cmd.setFrameShape(QFrame.StyledPanel)
        self.fr_d_c_cmd.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.fr_d_c_cmd)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.btn_csv_live = QPushButton(self.fr_d_c_cmd)
        self.btn_csv_live.setObjectName(u"btn_csv_live")
        self.btn_csv_live.setMinimumSize(QSize(100, 40))
        self.btn_csv_live.setMaximumSize(QSize(300, 40))
        self.btn_csv_live.setFont(font)
        self.btn_csv_live.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_csv_live.setCheckable(False)
        self.btn_csv_live.setChecked(False)
        self.btn_csv_live.setFlat(False)

        self.gridLayout.addWidget(self.btn_csv_live, 0, 0, 1, 1)

        self.btn_start_pause_data = QPushButton(self.fr_d_c_cmd)
        self.btn_start_pause_data.setObjectName(u"btn_start_pause_data")
        self.btn_start_pause_data.setMinimumSize(QSize(100, 40))
        self.btn_start_pause_data.setMaximumSize(QSize(300, 40))
        self.btn_start_pause_data.setFont(font)
        self.btn_start_pause_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_pause_data.setCheckable(True)
        self.btn_start_pause_data.setChecked(False)

        self.gridLayout.addWidget(self.btn_start_pause_data, 0, 1, 1, 1)

        self.btn_chart_pop = QPushButton(self.fr_d_c_cmd)
        self.btn_chart_pop.setObjectName(u"btn_chart_pop")
        self.btn_chart_pop.setMinimumSize(QSize(100, 40))
        self.btn_chart_pop.setMaximumSize(QSize(300, 40))
        self.btn_chart_pop.setFont(font)
        self.btn_chart_pop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chart_pop.setCheckable(False)
        self.btn_chart_pop.setChecked(False)

        self.gridLayout.addWidget(self.btn_chart_pop, 1, 0, 1, 1)

        self.btn_chart_clear = QPushButton(self.fr_d_c_cmd)
        self.btn_chart_clear.setObjectName(u"btn_chart_clear")
        self.btn_chart_clear.setMinimumSize(QSize(100, 40))
        self.btn_chart_clear.setMaximumSize(QSize(300, 40))
        self.btn_chart_clear.setFont(font)
        self.btn_chart_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chart_clear.setStyleSheet(u"color: rgb(222, 0, 0);")
        self.btn_chart_clear.setCheckable(False)
        self.btn_chart_clear.setChecked(False)

        self.gridLayout.addWidget(self.btn_chart_clear, 1, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.fr_d_c_cmd)

        self.fr_d_c_name = QFrame(self.fr_data_capture)
        self.fr_d_c_name.setObjectName(u"fr_d_c_name")
        self.fr_d_c_name.setMaximumSize(QSize(16777215, 20))
        self.fr_d_c_name.setFrameShape(QFrame.StyledPanel)
        self.fr_d_c_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_d_c_name)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_fr_d_c = QLabel(self.fr_d_c_name)
        self.lb_fr_d_c.setObjectName(u"lb_fr_d_c")
        self.lb_fr_d_c.setFont(font1)
        self.lb_fr_d_c.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_fr_d_c)


        self.verticalLayout_5.addWidget(self.fr_d_c_name)


        self.horizontalLayout_2.addWidget(self.fr_data_capture)

        self.fr_image_data = QFrame(self.tab_data)
        self.fr_image_data.setObjectName(u"fr_image_data")
        self.fr_image_data.setFrameShape(QFrame.StyledPanel)
        self.fr_image_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.fr_image_data)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.fr_i_d_cmd = QFrame(self.fr_image_data)
        self.fr_i_d_cmd.setObjectName(u"fr_i_d_cmd")
        self.fr_i_d_cmd.setFrameShape(QFrame.StyledPanel)
        self.fr_i_d_cmd.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.fr_i_d_cmd)

        self.fr_i_d_name = QFrame(self.fr_image_data)
        self.fr_i_d_name.setObjectName(u"fr_i_d_name")
        self.fr_i_d_name.setMaximumSize(QSize(16777215, 20))
        self.fr_i_d_name.setFrameShape(QFrame.StyledPanel)
        self.fr_i_d_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.fr_i_d_name)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lb_fr_i_d = QLabel(self.fr_i_d_name)
        self.lb_fr_i_d.setObjectName(u"lb_fr_i_d")
        self.lb_fr_i_d.setFont(font1)
        self.lb_fr_i_d.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lb_fr_i_d)


        self.verticalLayout_7.addWidget(self.fr_i_d_name)


        self.horizontalLayout_2.addWidget(self.fr_image_data)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.tabWidget_Cmd.addTab(self.tab_data, "")
        self.tab_state = QWidget()
        self.tab_state.setObjectName(u"tab_state")
        self.tabWidget_Cmd.addTab(self.tab_state, "")
        self.tab_uplink = QWidget()
        self.tab_uplink.setObjectName(u"tab_uplink")
        self.tabWidget_Cmd.addTab(self.tab_uplink, "")
        self.tab_graphics = QWidget()
        self.tab_graphics.setObjectName(u"tab_graphics")
        self.verticalLayout_28 = QVBoxLayout(self.tab_graphics)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.fr_d_c_cmd_3 = QFrame(self.tab_graphics)
        self.fr_d_c_cmd_3.setObjectName(u"fr_d_c_cmd_3")
        self.fr_d_c_cmd_3.setFrameShape(QFrame.StyledPanel)
        self.fr_d_c_cmd_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.fr_d_c_cmd_3)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.fr_graphics_cmd = QFrame(self.fr_d_c_cmd_3)
        self.fr_graphics_cmd.setObjectName(u"fr_graphics_cmd")
        self.fr_graphics_cmd.setFrameShape(QFrame.StyledPanel)
        self.fr_graphics_cmd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.fr_graphics_cmd)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, 10, 20, 10)

        self.horizontalLayout_13.addWidget(self.fr_graphics_cmd)

        self.horizontalLayout_13.setStretch(0, 6)

        self.verticalLayout_28.addWidget(self.fr_d_c_cmd_3)

        self.tabWidget_Cmd.addTab(self.tab_graphics, "")
        self.tab_sim = QWidget()
        self.tab_sim.setObjectName(u"tab_sim")
        self.tabWidget_Cmd.addTab(self.tab_sim, "")
        self.tab_sys = QWidget()
        self.tab_sys.setObjectName(u"tab_sys")
        self.tabWidget_Cmd.addTab(self.tab_sys, "")

        self.horizontalLayout.addWidget(self.tabWidget_Cmd)


        self.verticalLayout.addWidget(self.fr_cen_1)

        self.fr_cen_2 = QFrame(self.centralwidget)
        self.fr_cen_2.setObjectName(u"fr_cen_2")
        self.fr_cen_2.setFrameShape(QFrame.StyledPanel)
        self.fr_cen_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.fr_cen_2)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.fr_cen_2_1 = QFrame(self.fr_cen_2)
        self.fr_cen_2_1.setObjectName(u"fr_cen_2_1")
        self.fr_cen_2_1.setFrameShape(QFrame.StyledPanel)
        self.fr_cen_2_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.fr_cen_2_1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.fr_main_chart = QFrame(self.fr_cen_2_1)
        self.fr_main_chart.setObjectName(u"fr_main_chart")
        self.fr_main_chart.setFrameShape(QFrame.StyledPanel)
        self.fr_main_chart.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.fr_main_chart)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, 0, 0)
        self.fr_main1 = QFrame(self.fr_main_chart)
        self.fr_main1.setObjectName(u"fr_main1")
        self.fr_main1.setFrameShape(QFrame.StyledPanel)
        self.fr_main1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.fr_main1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.mpl_c1 = QWidget(self.fr_main1)
        self.mpl_c1.setObjectName(u"mpl_c1")

        self.verticalLayout_16.addWidget(self.mpl_c1)

        self.lb_main1 = QLabel(self.fr_main1)
        self.lb_main1.setObjectName(u"lb_main1")
        self.lb_main1.setMinimumSize(QSize(0, 20))
        self.lb_main1.setMaximumSize(QSize(16777215, 20))
        self.lb_main1.setFont(font1)
        self.lb_main1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.lb_main1)


        self.horizontalLayout_12.addWidget(self.fr_main1)

        self.fr_main2 = QFrame(self.fr_main_chart)
        self.fr_main2.setObjectName(u"fr_main2")
        self.fr_main2.setFrameShape(QFrame.StyledPanel)
        self.fr_main2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.fr_main2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.mpl_c2 = QWidget(self.fr_main2)
        self.mpl_c2.setObjectName(u"mpl_c2")

        self.verticalLayout_17.addWidget(self.mpl_c2)

        self.lb_main2 = QLabel(self.fr_main2)
        self.lb_main2.setObjectName(u"lb_main2")
        self.lb_main2.setMinimumSize(QSize(0, 20))
        self.lb_main2.setMaximumSize(QSize(16777215, 20))
        self.lb_main2.setFont(font1)
        self.lb_main2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.lb_main2)


        self.horizontalLayout_12.addWidget(self.fr_main2)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_15.addWidget(self.fr_main_chart)

        self.fr_sub_chart = QFrame(self.fr_cen_2_1)
        self.fr_sub_chart.setObjectName(u"fr_sub_chart")
        self.fr_sub_chart.setFrameShape(QFrame.StyledPanel)
        self.fr_sub_chart.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.fr_sub_chart)
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.fr_sub1 = QFrame(self.fr_sub_chart)
        self.fr_sub1.setObjectName(u"fr_sub1")
        self.fr_sub1.setFrameShape(QFrame.StyledPanel)
        self.fr_sub1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.fr_sub1)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.mpl_c3 = QWidget(self.fr_sub1)
        self.mpl_c3.setObjectName(u"mpl_c3")

        self.verticalLayout_18.addWidget(self.mpl_c3)

        self.lb_sub1 = QLabel(self.fr_sub1)
        self.lb_sub1.setObjectName(u"lb_sub1")
        self.lb_sub1.setMinimumSize(QSize(0, 20))
        self.lb_sub1.setMaximumSize(QSize(16777215, 20))
        self.lb_sub1.setFont(font1)
        self.lb_sub1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.lb_sub1)


        self.horizontalLayout_11.addWidget(self.fr_sub1)

        self.fr_sub2 = QFrame(self.fr_sub_chart)
        self.fr_sub2.setObjectName(u"fr_sub2")
        self.fr_sub2.setFrameShape(QFrame.StyledPanel)
        self.fr_sub2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.fr_sub2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.mpl_c4 = QWidget(self.fr_sub2)
        self.mpl_c4.setObjectName(u"mpl_c4")

        self.verticalLayout_19.addWidget(self.mpl_c4)

        self.lb_sub2 = QLabel(self.fr_sub2)
        self.lb_sub2.setObjectName(u"lb_sub2")
        self.lb_sub2.setMinimumSize(QSize(0, 20))
        self.lb_sub2.setMaximumSize(QSize(16777215, 20))
        self.lb_sub2.setFont(font1)
        self.lb_sub2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.lb_sub2)


        self.horizontalLayout_11.addWidget(self.fr_sub2)

        self.fr_sub3 = QFrame(self.fr_sub_chart)
        self.fr_sub3.setObjectName(u"fr_sub3")
        self.fr_sub3.setFrameShape(QFrame.StyledPanel)
        self.fr_sub3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.fr_sub3)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.mpl_c5 = QWidget(self.fr_sub3)
        self.mpl_c5.setObjectName(u"mpl_c5")

        self.verticalLayout_20.addWidget(self.mpl_c5)

        self.lb_sub3 = QLabel(self.fr_sub3)
        self.lb_sub3.setObjectName(u"lb_sub3")
        self.lb_sub3.setMinimumSize(QSize(0, 20))
        self.lb_sub3.setMaximumSize(QSize(16777215, 20))
        self.lb_sub3.setFont(font1)
        self.lb_sub3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.lb_sub3)


        self.horizontalLayout_11.addWidget(self.fr_sub3)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 1)

        self.verticalLayout_15.addWidget(self.fr_sub_chart)

        self.fr_sub_diagram = QFrame(self.fr_cen_2_1)
        self.fr_sub_diagram.setObjectName(u"fr_sub_diagram")
        self.fr_sub_diagram.setFrameShape(QFrame.StyledPanel)
        self.fr_sub_diagram.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.fr_sub_diagram)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.fr_sub1_2 = QFrame(self.fr_sub_diagram)
        self.fr_sub1_2.setObjectName(u"fr_sub1_2")
        self.fr_sub1_2.setFrameShape(QFrame.StyledPanel)
        self.fr_sub1_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.fr_sub1_2)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.mpl_c6 = QWidget(self.fr_sub1_2)
        self.mpl_c6.setObjectName(u"mpl_c6")

        self.verticalLayout_23.addWidget(self.mpl_c6)

        self.lb_sub4 = QLabel(self.fr_sub1_2)
        self.lb_sub4.setObjectName(u"lb_sub4")
        self.lb_sub4.setMinimumSize(QSize(0, 20))
        self.lb_sub4.setMaximumSize(QSize(16777215, 20))
        self.lb_sub4.setFont(font1)
        self.lb_sub4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.lb_sub4)


        self.horizontalLayout_10.addWidget(self.fr_sub1_2)

        self.fr_sub2_2 = QFrame(self.fr_sub_diagram)
        self.fr_sub2_2.setObjectName(u"fr_sub2_2")
        self.fr_sub2_2.setFrameShape(QFrame.StyledPanel)
        self.fr_sub2_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.fr_sub2_2)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.mpl_c7 = QWidget(self.fr_sub2_2)
        self.mpl_c7.setObjectName(u"mpl_c7")

        self.verticalLayout_25.addWidget(self.mpl_c7)

        self.lb_sub6 = QLabel(self.fr_sub2_2)
        self.lb_sub6.setObjectName(u"lb_sub6")
        self.lb_sub6.setMinimumSize(QSize(0, 20))
        self.lb_sub6.setMaximumSize(QSize(16777215, 20))
        self.lb_sub6.setFont(font1)
        self.lb_sub6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.lb_sub6)


        self.horizontalLayout_10.addWidget(self.fr_sub2_2)

        self.fr_sub3_2 = QFrame(self.fr_sub_diagram)
        self.fr_sub3_2.setObjectName(u"fr_sub3_2")
        self.fr_sub3_2.setFrameShape(QFrame.StyledPanel)
        self.fr_sub3_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.fr_sub3_2)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.mpl_c8 = QWidget(self.fr_sub3_2)
        self.mpl_c8.setObjectName(u"mpl_c8")

        self.verticalLayout_26.addWidget(self.mpl_c8)

        self.lb_sub7 = QLabel(self.fr_sub3_2)
        self.lb_sub7.setObjectName(u"lb_sub7")
        self.lb_sub7.setMinimumSize(QSize(0, 20))
        self.lb_sub7.setMaximumSize(QSize(16777215, 20))
        self.lb_sub7.setFont(font1)
        self.lb_sub7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.lb_sub7)


        self.horizontalLayout_10.addWidget(self.fr_sub3_2)

        self.fr_sub3_3 = QFrame(self.fr_sub_diagram)
        self.fr_sub3_3.setObjectName(u"fr_sub3_3")
        self.fr_sub3_3.setFrameShape(QFrame.StyledPanel)
        self.fr_sub3_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.fr_sub3_3)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.mpl_c9 = QWidget(self.fr_sub3_3)
        self.mpl_c9.setObjectName(u"mpl_c9")

        self.verticalLayout_24.addWidget(self.mpl_c9)

        self.lb_sub5 = QLabel(self.fr_sub3_3)
        self.lb_sub5.setObjectName(u"lb_sub5")
        self.lb_sub5.setMinimumSize(QSize(0, 20))
        self.lb_sub5.setMaximumSize(QSize(16777215, 20))
        self.lb_sub5.setFont(font1)
        self.lb_sub5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.lb_sub5)


        self.horizontalLayout_10.addWidget(self.fr_sub3_3)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 1)
        self.horizontalLayout_10.setStretch(3, 1)

        self.verticalLayout_15.addWidget(self.fr_sub_diagram)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 1)
        self.verticalLayout_15.setStretch(2, 1)

        self.horizontalLayout_9.addWidget(self.fr_cen_2_1)

        self.fr_cen_2_3 = QFrame(self.fr_cen_2)
        self.fr_cen_2_3.setObjectName(u"fr_cen_2_3")
        self.fr_cen_2_3.setFrameShape(QFrame.StyledPanel)
        self.fr_cen_2_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.fr_cen_2_3)
        self.verticalLayout_14.setSpacing(4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 8, 0)
        self.lb_kv_table = QLabel(self.fr_cen_2_3)
        self.lb_kv_table.setObjectName(u"lb_kv_table")
        self.lb_kv_table.setMinimumSize(QSize(0, 20))
        self.lb_kv_table.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.lb_kv_table.setFont(font3)

        self.verticalLayout_14.addWidget(self.lb_kv_table)

        self.table_kv_payload = QTableWidget(self.fr_cen_2_3)
        if (self.table_kv_payload.columnCount() < 2):
            self.table_kv_payload.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_kv_payload.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_kv_payload.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.table_kv_payload.rowCount() < 2):
            self.table_kv_payload.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_kv_payload.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_kv_payload.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_kv_payload.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_kv_payload.setItem(1, 0, __qtablewidgetitem5)
        self.table_kv_payload.setObjectName(u"table_kv_payload")
        self.table_kv_payload.setStyleSheet(u"font: 11pt \"Consolas\";")
        self.table_kv_payload.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_kv_payload.setShowGrid(True)
        self.table_kv_payload.setGridStyle(Qt.SolidLine)
        self.table_kv_payload.horizontalHeader().setMinimumSectionSize(75)
        self.table_kv_payload.horizontalHeader().setDefaultSectionSize(120)
        self.table_kv_payload.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.table_kv_payload)

        self.tabWidget_Monitor = QTabWidget(self.fr_cen_2_3)
        self.tabWidget_Monitor.setObjectName(u"tabWidget_Monitor")
        self.tab_serial_mon = QWidget()
        self.tab_serial_mon.setObjectName(u"tab_serial_mon")
        self.verticalLayout_21 = QVBoxLayout(self.tab_serial_mon)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.text_serial_mon = QPlainTextEdit(self.tab_serial_mon)
        self.text_serial_mon.setObjectName(u"text_serial_mon")
        self.text_serial_mon.setStyleSheet(u"font: 9pt \"Consolas\";")

        self.verticalLayout_21.addWidget(self.text_serial_mon)

        self.btn_serial_mon_clear = QPushButton(self.tab_serial_mon)
        self.btn_serial_mon_clear.setObjectName(u"btn_serial_mon_clear")
        self.btn_serial_mon_clear.setMinimumSize(QSize(100, 20))
        self.btn_serial_mon_clear.setMaximumSize(QSize(16777215, 20))
        self.btn_serial_mon_clear.setFont(font)
        self.btn_serial_mon_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_serial_mon_clear.setStyleSheet(u"color: rgb(222, 0, 0);")
        self.btn_serial_mon_clear.setCheckable(False)
        self.btn_serial_mon_clear.setChecked(False)

        self.verticalLayout_21.addWidget(self.btn_serial_mon_clear)

        self.tabWidget_Monitor.addTab(self.tab_serial_mon, "")
        self.tab_sys_log = QWidget()
        self.tab_sys_log.setObjectName(u"tab_sys_log")
        self.verticalLayout_22 = QVBoxLayout(self.tab_sys_log)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.text_sys_log = QPlainTextEdit(self.tab_sys_log)
        self.text_sys_log.setObjectName(u"text_sys_log")
        self.text_sys_log.setStyleSheet(u"font: 9pt \"Consolas\";")

        self.verticalLayout_22.addWidget(self.text_sys_log)

        self.tabWidget_Monitor.addTab(self.tab_sys_log, "")

        self.verticalLayout_14.addWidget(self.tabWidget_Monitor)


        self.horizontalLayout_9.addWidget(self.fr_cen_2_3)

        self.horizontalLayout_9.setStretch(0, 6)
        self.horizontalLayout_9.setStretch(1, 2)

        self.verticalLayout.addWidget(self.fr_cen_2)

        self.fr_cen_3 = QFrame(self.centralwidget)
        self.fr_cen_3.setObjectName(u"fr_cen_3")
        self.fr_cen_3.setMinimumSize(QSize(0, 40))
        self.fr_cen_3.setMaximumSize(QSize(16777215, 40))
        self.fr_cen_3.setFrameShape(QFrame.StyledPanel)
        self.fr_cen_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.fr_cen_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_footer = QLabel(self.fr_cen_3)
        self.lb_footer.setObjectName(u"lb_footer")
        self.lb_footer.setFont(font2)
        self.lb_footer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lb_footer)

        self.lb_exit_code = QLabel(self.fr_cen_3)
        self.lb_exit_code.setObjectName(u"lb_exit_code")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.lb_exit_code.setFont(font4)
        self.lb_exit_code.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_exit_code)

        self.lb_exit_id = QLabel(self.fr_cen_3)
        self.lb_exit_id.setObjectName(u"lb_exit_id")
        self.lb_exit_id.setFont(font2)
        self.lb_exit_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_exit_id)


        self.verticalLayout.addWidget(self.fr_cen_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menuSettings.addAction(self.actionPreferences)

        self.retranslateUi(MainWindow)

        self.tabWidget_Cmd.setCurrentIndex(0)
        self.btn_serial_connect.setDefault(True)
        self.btn_csv_live.setDefault(False)
        self.tabWidget_Monitor.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About CUGS", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Device Serial Port", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Baud Rate", None))
        self.combo_baud.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combo_baud.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.combo_baud.setItemText(2, QCoreApplication.translate("MainWindow", u"2400", None))
        self.combo_baud.setItemText(3, QCoreApplication.translate("MainWindow", u"4800", None))
        self.combo_baud.setItemText(4, QCoreApplication.translate("MainWindow", u"19200", None))
        self.combo_baud.setItemText(5, QCoreApplication.translate("MainWindow", u"38400", None))
        self.combo_baud.setItemText(6, QCoreApplication.translate("MainWindow", u"57600", None))

        self.btn_serial_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.btn_serial_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.btn_serial_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.lb_fr_d_c_2.setText(QCoreApplication.translate("MainWindow", u"Serial Device Selection", None))
        self.text_serial_info.setPlainText(QCoreApplication.translate("MainWindow", u"Serial Information Area!", None))
        self.lb_fr_i_d_2.setText(QCoreApplication.translate("MainWindow", u"Serial Information", None))
        self.tabWidget_Cmd.setTabText(self.tabWidget_Cmd.indexOf(self.tab_serial), QCoreApplication.translate("MainWindow", u"Serial Port Connection", None))
        self.cb_write_log.setText(QCoreApplication.translate("MainWindow", u"Write Mission Log CSV", None))
        self.cb_write_kml.setText(QCoreApplication.translate("MainWindow", u"Write Google Earth KML", None))
        self.btn_start_mission.setText(QCoreApplication.translate("MainWindow", u"Start Mission", None))
        self.lb_fr_m_c.setText(QCoreApplication.translate("MainWindow", u"Mission Control", None))
        self.btn_csv_live.setText(QCoreApplication.translate("MainWindow", u"Live CSV", None))
        self.btn_start_pause_data.setText(QCoreApplication.translate("MainWindow", u"Pause Data", None))
        self.btn_chart_pop.setText(QCoreApplication.translate("MainWindow", u"Pop Chart", None))
        self.btn_chart_clear.setText(QCoreApplication.translate("MainWindow", u"Clear Chart", None))
        self.lb_fr_d_c.setText(QCoreApplication.translate("MainWindow", u"Data Capture Control", None))
        self.lb_fr_i_d.setText(QCoreApplication.translate("MainWindow", u"Image Data (Coming soon!)", None))
        self.tabWidget_Cmd.setTabText(self.tabWidget_Cmd.indexOf(self.tab_data), QCoreApplication.translate("MainWindow", u"Data Acquisition", None))
        self.tabWidget_Cmd.setTabText(self.tabWidget_Cmd.indexOf(self.tab_state), QCoreApplication.translate("MainWindow", u"State", None))
        self.tabWidget_Cmd.setTabText(self.tabWidget_Cmd.indexOf(self.tab_uplink), QCoreApplication.translate("MainWindow", u"Uplink Command", None))
        self.tabWidget_Cmd.setTabText(self.tabWidget_Cmd.indexOf(self.tab_graphics), QCoreApplication.translate("MainWindow", u"Graphics Settings", None))
        self.tabWidget_Cmd.setTabText(self.tabWidget_Cmd.indexOf(self.tab_sim), QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.tabWidget_Cmd.setTabText(self.tabWidget_Cmd.indexOf(self.tab_sys), QCoreApplication.translate("MainWindow", u"System", None))
        self.lb_main1.setText(QCoreApplication.translate("MainWindow", u"MAIN1 CHART LABEL", None))
        self.lb_main2.setText(QCoreApplication.translate("MainWindow", u"MAIN2 CHART LABEL", None))
        self.lb_sub1.setText(QCoreApplication.translate("MainWindow", u"SUB1 CHART LABEL", None))
        self.lb_sub2.setText(QCoreApplication.translate("MainWindow", u"SUB2 CHART LABEL", None))
        self.lb_sub3.setText(QCoreApplication.translate("MainWindow", u"SUB3 CHART LABEL", None))
        self.lb_sub4.setText(QCoreApplication.translate("MainWindow", u"SUB4 CHART LABEL", None))
        self.lb_sub6.setText(QCoreApplication.translate("MainWindow", u"SUB6 CHART LABEL", None))
        self.lb_sub7.setText(QCoreApplication.translate("MainWindow", u"SUB7 CHART LABEL", None))
        self.lb_sub5.setText(QCoreApplication.translate("MainWindow", u"SUB5 CHART LABEL", None))
        self.lb_kv_table.setText(QCoreApplication.translate("MainWindow", u"Data Payload Key-Value Pairs Table", None))
        ___qtablewidgetitem = self.table_kv_payload.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Key", None));
        ___qtablewidgetitem1 = self.table_kv_payload.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem2 = self.table_kv_payload.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem3 = self.table_kv_payload.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.table_kv_payload.isSortingEnabled()
        self.table_kv_payload.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.table_kv_payload.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"TEAM_ID", None));
        ___qtablewidgetitem5 = self.table_kv_payload.item(1, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PACKET", None));
        self.table_kv_payload.setSortingEnabled(__sortingEnabled)

        self.text_serial_mon.setPlainText(QCoreApplication.translate("MainWindow", u"Serial Monitor Area!", None))
        self.btn_serial_mon_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget_Monitor.setTabText(self.tabWidget_Monitor.indexOf(self.tab_serial_mon), QCoreApplication.translate("MainWindow", u"Serial Monitor", None))
        self.text_sys_log.setPlainText(QCoreApplication.translate("MainWindow", u"System Log Area!", None))
        self.tabWidget_Monitor.setTabText(self.tabWidget_Monitor.indexOf(self.tab_sys_log), QCoreApplication.translate("MainWindow", u"System Log", None))
        self.lb_footer.setText(QCoreApplication.translate("MainWindow", u"    CUGS V1: Ground Station Software Interface. Vivatsathorn Thitasirivit, 2022", None))
        self.lb_exit_code.setText(QCoreApplication.translate("MainWindow", u"Exit Code   ", None))
        self.lb_exit_id.setText(QCoreApplication.translate("MainWindow", u"Exit Code", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

