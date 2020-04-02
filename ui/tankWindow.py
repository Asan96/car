# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tankWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tankWindow(object):
    def setupUi(self, tankWindow):
        tankWindow.setObjectName("tankWindow")
        tankWindow.resize(1000, 720)
        tankWindow.setMinimumSize(QtCore.QSize(1000, 720))
        tankWindow.setMaximumSize(QtCore.QSize(1000, 720))
        self.widget = QtWidgets.QWidget(tankWindow)
        self.widget.setMinimumSize(QtCore.QSize(1000, 720))
        self.widget.setMaximumSize(QtCore.QSize(1000, 720))
        self.widget.setMouseTracking(True)
        self.widget.setObjectName("widget")
        self.tabMenuWidget = QtWidgets.QTabWidget(self.widget)
        self.tabMenuWidget.setGeometry(QtCore.QRect(0, -1, 1000, 693))
        self.tabMenuWidget.setBaseSize(QtCore.QSize(1021, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.tabMenuWidget.setFont(font)
        self.tabMenuWidget.setStyleSheet("color:#2F4056;\n"
"border-top-color: rgb(255, 85, 127);\n"
"")
        self.tabMenuWidget.setIconSize(QtCore.QSize(24, 24))
        self.tabMenuWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabMenuWidget.setObjectName("tabMenuWidget")
        self.tab_control = QtWidgets.QWidget()
        self.tab_control.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.tab_control.setFont(font)
        self.tab_control.setStyleSheet("")
        self.tab_control.setObjectName("tab_control")
        self.avoid = QtWidgets.QCheckBox(self.tab_control)
        self.avoid.setGeometry(QtCore.QRect(70, 600, 81, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.avoid.setFont(font)
        self.avoid.setObjectName("avoid")
        self.label_2 = QtWidgets.QLabel(self.tab_control)
        self.label_2.setGeometry(QtCore.QRect(230, 560, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-family:\'微软雅黑\';font-size:17px;font-weight:500;")
        self.label_2.setObjectName("label_2")
        self.car_backward = QtWidgets.QPushButton(self.tab_control)
        self.car_backward.setGeometry(QtCore.QRect(760, 210, 60, 60))
        self.car_backward.setStyleSheet("QPushButton{background-color:rgb(255,255,255);color:rgb(243, 243, 243);border-radius:5px;font-size:14px;font-weight:500;font-family:\'微软雅黑\';}")
        self.car_backward.setText("")
        self.car_backward.setIconSize(QtCore.QSize(64, 64))
        self.car_backward.setObjectName("car_backward")
        self.keyboard_control = QtWidgets.QCheckBox(self.tab_control)
        self.keyboard_control.setGeometry(QtCore.QRect(630, 600, 81, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.keyboard_control.setFont(font)
        self.keyboard_control.setObjectName("keyboard_control")
        self.travel = QtWidgets.QCheckBox(self.tab_control)
        self.travel.setGeometry(QtCore.QRect(240, 600, 81, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.travel.setFont(font)
        self.travel.setObjectName("travel")
        self.car_rotate = QtWidgets.QPushButton(self.tab_control)
        self.car_rotate.setGeometry(QtCore.QRect(900, 110, 60, 60))
        self.car_rotate.setStyleSheet("QPushButton{background-color:white;color:rgb(243, 243, 243);border-radius:5px;font-size:14px;font-weight:500;font-family:\'微软雅黑\';}")
        self.car_rotate.setText("")
        self.car_rotate.setIconSize(QtCore.QSize(64, 64))
        self.car_rotate.setObjectName("car_rotate")
        self.car_right = QtWidgets.QPushButton(self.tab_control)
        self.car_right.setGeometry(QtCore.QRect(700, 160, 60, 60))
        self.car_right.setWhatsThis("")
        self.car_right.setStyleSheet("QPushButton{background-color:rgb(255,255,255);color:rgb(243, 243, 243);border-radius:5px;font-size:14px;font-weight:500;font-family:\'微软雅黑\';}")
        self.car_right.setText("")
        self.car_right.setIconSize(QtCore.QSize(64, 64))
        self.car_right.setObjectName("car_right")
        self.label_4 = QtWidgets.QLabel(self.tab_control)
        self.label_4.setGeometry(QtCore.QRect(800, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(85, 170, 255);font-family:\'微软雅黑\';font-weight:bold;")
        self.label_4.setObjectName("label_4")
        self.car_cam_left = QtWidgets.QPushButton(self.tab_control)
        self.car_cam_left.setGeometry(QtCore.QRect(870, 410, 60, 60))
        self.car_cam_left.setStyleSheet("QPushButton{background-color:white;color:#F3F3F3;border-top-right-radius:5px;border-bottom-right-radius:5px;font-size:14px;font-weight:500;font-family:\'微软雅黑\';}")
        self.car_cam_left.setText("")
        self.car_cam_left.setIconSize(QtCore.QSize(64, 64))
        self.car_cam_left.setObjectName("car_cam_left")
        self.car_forward = QtWidgets.QPushButton(self.tab_control)
        self.car_forward.setGeometry(QtCore.QRect(760, 110, 60, 60))
        self.car_forward.setWhatsThis("")
        self.car_forward.setStyleSheet("QPushButton{background-color:rgb(255,255,255);color:rgb(243, 243, 243);border-radius:5px;font-size:14px;font-weight:500;font-family:\'微软雅黑\';}")
        self.car_forward.setText("")
        self.car_forward.setIconSize(QtCore.QSize(64, 64))
        self.car_forward.setObjectName("car_forward")
        self.car_cam_down = QtWidgets.QPushButton(self.tab_control)
        self.car_cam_down.setGeometry(QtCore.QRect(810, 360, 60, 60))
        self.car_cam_down.setStyleSheet("QPushButton{background-color:white;color:#F3F3F3;border-top-left-radius:5px;border-top-right-radius:5px;font-size:14px;font-weight:500;font-family:\'微软雅黑\';}")
        self.car_cam_down.setText("")
        self.car_cam_down.setIconSize(QtCore.QSize(64, 64))
        self.car_cam_down.setObjectName("car_cam_down")
        self.label = QtWidgets.QLabel(self.tab_control)
        self.label.setGeometry(QtCore.QRect(60, 560, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.label.setFont(font)
        self.label.setStyleSheet("font-family:\'微软雅黑\';font-size:17px;font-weight:500;")
        self.label.setObjectName("label")
        self.car_stop = QtWidgets.QPushButton(self.tab_control)
        self.car_stop.setGeometry(QtCore.QRect(900, 210, 60, 60))
        self.car_stop.setStyleSheet("QPushButton{background-color:white;color:rgb(243, 243, 243);border-radius:5px;font-size:14px;font-weight:500;font-family:\'微软雅黑\';}")
        self.car_stop.setText("")
        self.car_stop.setIconSize(QtCore.QSize(64, 64))
        self.car_stop.setObjectName("car_stop")
        self.car_cam_up = QtWidgets.QPushButton(self.tab_control)
        self.car_cam_up.setGeometry(QtCore.QRect(810, 460, 60, 60))
        self.car_cam_up.setStyleSheet("QPushButton{background-color:white;color:#F3F3F3;border-bottom-left-radius:5px;border-bottom-right-radius:5px;font-size:14px;font-weight:500;font-family:\'微软雅黑\';}")
        self.car_cam_up.setText("")
        self.car_cam_up.setIconSize(QtCore.QSize(64, 64))
        self.car_cam_up.setObjectName("car_cam_up")
        self.label_3 = QtWidgets.QLabel(self.tab_control)
        self.label_3.setGeometry(QtCore.QRect(620, 560, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-family:\'微软雅黑\';font-size:17px;font-weight:500;")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab_control)
        self.label_5.setGeometry(QtCore.QRect(790, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(85, 170, 255);font-family:\'微软雅黑\';font-weight:bold;")
        self.label_5.setObjectName("label_5")
        self.car_cam_right = QtWidgets.QPushButton(self.tab_control)
        self.car_cam_right.setGeometry(QtCore.QRect(750, 410, 60, 60))
        self.car_cam_right.setStyleSheet("QPushButton{background-color:white;color:#F3F3F3;border-top-left-radius:5px;border-bottom-left-radius:5px;font-size:14px;font-weight:500;font-family:\'微软雅黑\';}")
        self.car_cam_right.setText("")
        self.car_cam_right.setIconSize(QtCore.QSize(64, 64))
        self.car_cam_right.setObjectName("car_cam_right")
        self.car_left = QtWidgets.QPushButton(self.tab_control)
        self.car_left.setGeometry(QtCore.QRect(820, 160, 60, 60))
        self.car_left.setStyleSheet("QPushButton{background-color:rgb(255,255,255);color:rgb(243, 243, 243);border-radius:5px;font-size:14px;font-weight:500;font-family:\'微软雅黑\';}")
        self.car_left.setText("")
        self.car_left.setIconSize(QtCore.QSize(64, 64))
        self.car_left.setObjectName("car_left")
        self.label_9 = QtWidgets.QLabel(self.tab_control)
        self.label_9.setGeometry(QtCore.QRect(420, 560, 101, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font-family:\'微软雅黑\';font-size:17px;font-weight:500;")
        self.label_9.setObjectName("label_9")
        self.camera_switch = QtWidgets.QCheckBox(self.tab_control)
        self.camera_switch.setGeometry(QtCore.QRect(440, 600, 81, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.camera_switch.setFont(font)
        self.camera_switch.setObjectName("camera_switch")
        self.origin_camera = QtWidgets.QLabel(self.tab_control)
        self.origin_camera.setGeometry(QtCore.QRect(30, 50, 640, 480))
        self.origin_camera.setStyleSheet("background-color:white;")
        self.origin_camera.setText("")
        self.origin_camera.setObjectName("origin_camera")
        self.label_11 = QtWidgets.QLabel(self.tab_control)
        self.label_11.setGeometry(QtCore.QRect(810, 560, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font-family:\'微软雅黑\';font-size:17px;font-weight:500;")
        self.label_11.setObjectName("label_11")
        self.follow = QtWidgets.QCheckBox(self.tab_control)
        self.follow.setGeometry(QtCore.QRect(820, 600, 81, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.follow.setFont(font)
        self.follow.setStyleSheet("")
        self.follow.setIconSize(QtCore.QSize(48, 48))
        self.follow.setObjectName("follow")
        self.tabMenuWidget.addTab(self.tab_control, "")
        self.tab_voice = QtWidgets.QWidget()
        self.tab_voice.setStyleSheet("")
        self.tab_voice.setObjectName("tab_voice")
        self.voice_control = QtWidgets.QPushButton(self.tab_voice)
        self.voice_control.setGeometry(QtCore.QRect(820, 80, 81, 41))
        self.voice_control.setStyleSheet("QPushButton{font-family:\'微软雅黑\';font-size:14px;background-color:rgb(99, 180, 255);border-radius:5px;color:#F8F8F8}\n"
"QPushButton:hover{background-color:#009688}")
        self.voice_control.setObjectName("voice_control")
        self.voice_text_composite = QtWidgets.QPushButton(self.tab_voice)
        self.voice_text_composite.setGeometry(QtCore.QRect(780, 150, 81, 41))
        self.voice_text_composite.setStyleSheet("QPushButton{font-family:\'微软雅黑\';font-size:14px;background-color:rgb(99, 180, 255);border-top-right-radius:5px;border-bottom-right-radius:5px;color:#F8F8F8}\n"
"QPushButton:hover{background-color:#009688}")
        self.voice_text_composite.setObjectName("voice_text_composite")
        self.voice_text_chat = QtWidgets.QPushButton(self.tab_voice)
        self.voice_text_chat.setGeometry(QtCore.QRect(780, 480, 81, 41))
        self.voice_text_chat.setStyleSheet("QPushButton{font-family:\'微软雅黑\';font-size:14px;background-color:rgb(99, 180, 255);border-bottom-right-radius:5px;color:#F8F8F8;}\n"
"QPushButton:hover{background-color:#009688}")
        self.voice_text_chat.setObjectName("voice_text_chat")
        self.label_6 = QtWidgets.QLabel(self.tab_voice)
        self.label_6.setGeometry(QtCore.QRect(150, 40, 501, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-family:\'微软雅黑\';")
        self.label_6.setObjectName("label_6")
        self.input_composite_text = QtWidgets.QLineEdit(self.tab_voice)
        self.input_composite_text.setGeometry(QtCore.QRect(150, 150, 631, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.input_composite_text.setFont(font)
        self.input_composite_text.setStyleSheet("font-family:\'微软雅黑\';")
        self.input_composite_text.setObjectName("input_composite_text")
        self.voice_chat = QtWidgets.QPushButton(self.tab_voice)
        self.voice_chat.setGeometry(QtCore.QRect(690, 40, 81, 41))
        self.voice_chat.setStyleSheet("QPushButton{font-family:\'微软雅黑\';font-size:14px;background-color:rgb(99, 180, 255);border-radius:5px;color:#F8F8F8;}\n"
"QPushButton:hover{background-color:#009688}")
        self.voice_chat.setObjectName("voice_chat")
        self.voice_chat_list = QtWidgets.QTextBrowser(self.tab_voice)
        self.voice_chat_list.setGeometry(QtCore.QRect(150, 230, 711, 251))
        self.voice_chat_list.setStyleSheet("text-align:center;font-size:15px;padding-left:150px;line-height:40px;\n"
"background-color:white;font-family:\'微软雅黑\';")
        self.voice_chat_list.setObjectName("voice_chat_list")
        self.input_send_text = QtWidgets.QLineEdit(self.tab_voice)
        self.input_send_text.setGeometry(QtCore.QRect(150, 480, 631, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.input_send_text.setFont(font)
        self.input_send_text.setStyleSheet("font-family:\'微软雅黑\';")
        self.input_send_text.setObjectName("input_send_text")
        self.label_7 = QtWidgets.QLabel(self.tab_voice)
        self.label_7.setGeometry(QtCore.QRect(150, 80, 651, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font-family:\'微软雅黑\';")
        self.label_7.setObjectName("label_7")
        self.voice_audio_start = QtWidgets.QPushButton(self.tab_voice)
        self.voice_audio_start.setGeometry(QtCore.QRect(560, 550, 81, 41))
        self.voice_audio_start.setStyleSheet("QPushButton{font-family:\'微软雅黑\';font-size:14px;background-color:rgb(99, 180, 255);border-radius:5px;color:#F8F8F8}\n"
"QPushButton:hover{background-color:#009688}")
        self.voice_audio_start.setObjectName("voice_audio_start")
        self.label_8 = QtWidgets.QLabel(self.tab_voice)
        self.label_8.setGeometry(QtCore.QRect(150, 550, 391, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font-family:\'微软雅黑\';")
        self.label_8.setObjectName("label_8")
        self.voice_audio_stop = QtWidgets.QPushButton(self.tab_voice)
        self.voice_audio_stop.setGeometry(QtCore.QRect(670, 550, 81, 41))
        self.voice_audio_stop.setStyleSheet("QPushButton{font-family:\'微软雅黑\';font-size:14px;background-color:#FF0000;border-radius:5px;color:#F8F8F8}\n"
"QPushButton:hover{background-color:#FF5722}")
        self.voice_audio_stop.setObjectName("voice_audio_stop")
        self.voice_audio_play = QtWidgets.QPushButton(self.tab_voice)
        self.voice_audio_play.setGeometry(QtCore.QRect(780, 550, 81, 41))
        self.voice_audio_play.setStyleSheet("QPushButton{font-family:\'微软雅黑\';font-size:14px;background-color:rgb(24, 157, 50);border-radius:5px;color:#F8F8F8}\n"
"QPushButton:hover{background-color:#5FB878}")
        self.voice_audio_play.setObjectName("voice_audio_play")
        self.tabMenuWidget.addTab(self.tab_voice, "")
        self.tab_video = QtWidgets.QWidget()
        self.tab_video.setObjectName("tab_video")
        self.camera_origin = QtWidgets.QPushButton(self.tab_video)
        self.camera_origin.setGeometry(QtCore.QRect(170, 550, 160, 31))
        self.camera_origin.setStyleSheet("QPushButton:hover{background-color:#009688;color:#F8F8F8} \n"
"QPushButton{background-color:#1E9FFF;border-bottom-left-radius:5px;color:#F2F2F2;border-right:1px solid #F8F8F8;font-family:\'微软雅黑\';font-size:14px;border-top:1px solid #F8F8F8;}")
        self.camera_origin.setObjectName("camera_origin")
        self.camera_face = QtWidgets.QPushButton(self.tab_video)
        self.camera_face.setGeometry(QtCore.QRect(330, 550, 160, 31))
        self.camera_face.setStyleSheet("QPushButton:hover{background-color:#009688;color:#F8F8F8} \n"
"QPushButton{background-color:#1E9FFF;color:#F2F2F2;border-radius:0px;border-right:1px solid #F8F8F8;font-family:\'微软雅黑\';font-size:14px;border-top:1px solid #F8F8F8;}")
        self.camera_face.setObjectName("camera_face")
        self.camera_eyes = QtWidgets.QPushButton(self.tab_video)
        self.camera_eyes.setGeometry(QtCore.QRect(490, 550, 160, 31))
        self.camera_eyes.setStyleSheet("QPushButton:hover{background-color:#009688;color:#F8F8F8} \n"
"QPushButton{background-color:#1E9FFF;border-radius:0px;color:#F2F2F2;border-right:1px solid #F8F8F8;font-family:\'微软雅黑\';font-size:14px;border-top:1px solid #F8F8F8;}")
        self.camera_eyes.setObjectName("camera_eyes")
        self.camera_close = QtWidgets.QPushButton(self.tab_video)
        self.camera_close.setGeometry(QtCore.QRect(650, 550, 160, 31))
        self.camera_close.setStyleSheet("QPushButton:hover{background-color:#009688;color:#F8F8F8} \n"
"QPushButton{background-color:#1E9FFF;border-bottom-right-radius:5px;color:#F2F2F2;font-family:\'微软雅黑\';font-size:14px;border-top:1px solid #F8F8F8;}")
        self.camera_close.setObjectName("camera_close")
        self.video_pannel = QtWidgets.QLabel(self.tab_video)
        self.video_pannel.setGeometry(QtCore.QRect(170, 70, 640, 480))
        self.video_pannel.setStyleSheet("background-color:white;")
        self.video_pannel.setText("")
        self.video_pannel.setObjectName("video_pannel")
        self.tabMenuWidget.addTab(self.tab_video, "")
        self.tab_code = QtWidgets.QWidget()
        self.tab_code.setObjectName("tab_code")
        self.btnRunLocal = QtWidgets.QPushButton(self.tab_code)
        self.btnRunLocal.setGeometry(QtCore.QRect(700, 450, 100, 31))
        self.btnRunLocal.setStyleSheet("QPushButton:hover{background-color:rgb(0, 156, 0);color:#F8F8F8} \n"
"QPushButton{background-color:rgb(88, 177, 0);color:#F2F2F2;border:0;border-right:1px solid #DDDDDD;font-family:\'微软雅黑\';font-size:14px;}")
        self.btnRunLocal.setObjectName("btnRunLocal")
        self.btnRunStop = QtWidgets.QPushButton(self.tab_code)
        self.btnRunStop.setGeometry(QtCore.QRect(900, 450, 100, 31))
        self.btnRunStop.setStyleSheet("QPushButton:hover{background-color:rgb(255, 0, 0);color:#F8F8F8} \n"
"QPushButton{background-color:rgb(255, 48, 68);color:#F2F2F2;border:0;font-family:\'微软雅黑\';font-size:14px;}")
        self.btnRunStop.setObjectName("btnRunStop")
        self.btnCodeImport = QtWidgets.QPushButton(self.tab_code)
        self.btnCodeImport.setGeometry(QtCore.QRect(500, 450, 100, 31))
        self.btnCodeImport.setStyleSheet("QPushButton:hover{background-color:rgb(85, 170, 0);color:#F8F8F8} \n"
"QPushButton{background-color:rgb(85, 170, 127);color:#F2F2F2;border:0;border-right:1px solid #DDDDDD;font-family:\'微软雅黑\';font-size:14px;}\n"
"")
        self.btnCodeImport.setObjectName("btnCodeImport")
        self.btnCodeSave = QtWidgets.QPushButton(self.tab_code)
        self.btnCodeSave.setGeometry(QtCore.QRect(600, 450, 100, 31))
        self.btnCodeSave.setStyleSheet("QPushButton:hover{background-color:rgb(85, 170, 0);color:#F8F8F8} \n"
"QPushButton{background-color:rgb(85, 170, 127);color:#F2F2F2;border:0;border-right:1px solid #DDDDDD;font-family:\'微软雅黑\';font-size:14px;}")
        self.btnCodeSave.setObjectName("btnCodeSave")
        self.btnRunDevice = QtWidgets.QPushButton(self.tab_code)
        self.btnRunDevice.setGeometry(QtCore.QRect(800, 450, 100, 31))
        self.btnRunDevice.setStyleSheet("QPushButton:hover{background-color:rgb(0, 156, 0);color:#F8F8F8} \n"
"QPushButton{background-color:rgb(88, 177, 0);color:#F2F2F2;border:0;border-right:1px solid #DDDDDD;font-family:\'微软雅黑\';font-size:14px;}")
        self.btnRunDevice.setObjectName("btnRunDevice")
        self.label_10 = QtWidgets.QLabel(self.tab_code)
        self.label_10.setGeometry(QtCore.QRect(10, 460, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.CodeWidget = QtWidgets.QWidget(self.tab_code)
        self.CodeWidget.setGeometry(QtCore.QRect(-10, -10, 1021, 471))
        self.CodeWidget.setObjectName("CodeWidget")
        self.CodeConsoleText = QtWidgets.QTextBrowser(self.tab_code)
        self.CodeConsoleText.setGeometry(QtCore.QRect(0, 480, 1001, 181))
        self.CodeConsoleText.setMinimumSize(QtCore.QSize(1001, 181))
        self.CodeConsoleText.setMaximumSize(QtCore.QSize(1001, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.CodeConsoleText.setFont(font)
        self.CodeConsoleText.setStyleSheet("padding-left:20px;background-color:white;")
        self.CodeConsoleText.setObjectName("CodeConsoleText")
        self.tabMenuWidget.addTab(self.tab_code, "")
        tankWindow.setCentralWidget(self.widget)
        self.toolBar = QtWidgets.QToolBar(tankWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMaximumSize(QtCore.QSize(1000, 40))
        self.toolBar.setStyleSheet("background-color:rgb(255, 255, 255);color:rgb(66, 66, 66);border-bottom:none;")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setObjectName("toolBar")
        tankWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtWidgets.QAction(tankWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionChange = QtWidgets.QAction(tankWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.actionChange.setFont(font)
        self.actionChange.setObjectName("actionChange")
        self.actionInfo = QtWidgets.QAction(tankWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.actionInfo.setFont(font)
        self.actionInfo.setObjectName("actionInfo")
        self.actionLogin = QtWidgets.QAction(tankWindow)
        self.actionLogin.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.actionLogin.setFont(font)
        self.actionLogin.setShortcut("")
        self.actionLogin.setObjectName("actionLogin")
        self.actionText = QtWidgets.QAction(tankWindow)
        self.actionText.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionText.setFont(font)
        self.actionText.setObjectName("actionText")
        self.actionStatus = QtWidgets.QAction(tankWindow)
        self.actionStatus.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionStatus.setFont(font)
        self.actionStatus.setObjectName("actionStatus")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLogin)
        self.toolBar.addAction(self.actionChange)
        self.toolBar.addAction(self.actionInfo)
        self.toolBar.addAction(self.actionText)
        self.toolBar.addAction(self.actionStatus)

        self.retranslateUi(tankWindow)
        self.tabMenuWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(tankWindow)

    def retranslateUi(self, tankWindow):
        _translate = QtCore.QCoreApplication.translate
        tankWindow.setWindowTitle(_translate("tankWindow", "人工智能履带坦克"))
        self.avoid.setText(_translate("tankWindow", "开启"))
        self.label_2.setText(_translate("tankWindow", "循迹模式"))
        self.car_backward.setToolTip(_translate("tankWindow", "向后（D）"))
        self.keyboard_control.setText(_translate("tankWindow", "开启"))
        self.travel.setText(_translate("tankWindow", "开启"))
        self.car_rotate.setToolTip(_translate("tankWindow", "旋转（Q）"))
        self.car_right.setToolTip(_translate("tankWindow", "向左（A）"))
        self.label_4.setText(_translate("tankWindow", "行动控制"))
        self.car_cam_left.setToolTip(_translate("tankWindow", "向右"))
        self.car_forward.setToolTip(_translate("tankWindow", "前进(W)"))
        self.car_cam_down.setToolTip(_translate("tankWindow", "向上"))
        self.label.setText(_translate("tankWindow", "避障模式"))
        self.car_stop.setToolTip(_translate("tankWindow", "停止（E）"))
        self.car_cam_up.setToolTip(_translate("tankWindow", "向下"))
        self.label_3.setText(_translate("tankWindow", "键盘控制"))
        self.label_5.setText(_translate("tankWindow", "摄像头控制"))
        self.car_cam_right.setToolTip(_translate("tankWindow", "向左"))
        self.car_left.setToolTip(_translate("tankWindow", "向右（D）"))
        self.label_9.setText(_translate("tankWindow", "摄像头画面"))
        self.camera_switch.setText(_translate("tankWindow", "开启"))
        self.label_11.setText(_translate("tankWindow", "物体跟随"))
        self.follow.setText(_translate("tankWindow", "开启"))
        self.follow.setShortcut(_translate("tankWindow", "Ctrl+S"))
        self.tabMenuWidget.setTabText(self.tabMenuWidget.indexOf(self.tab_control), _translate("tankWindow", "运动控制"))
        self.voice_control.setText(_translate("tankWindow", "语音控制"))
        self.voice_text_composite.setText(_translate("tankWindow", "语音合成"))
        self.voice_text_chat.setText(_translate("tankWindow", "文字对话"))
        self.label_6.setText(_translate("tankWindow", "语音对话：唤醒词为佩奇佩奇，唤醒成功后听到提示音进行语音对话。"))
        self.input_composite_text.setPlaceholderText(_translate("tankWindow", "   语音合成会将输入的文字合成语音并播放，请输入文字..."))
        self.voice_chat.setText(_translate("tankWindow", "语音对话"))
        self.input_send_text.setPlaceholderText(_translate("tankWindow", "   请输入聊天文字内容..."))
        self.label_7.setText(_translate("tankWindow", "语音控制：唤醒词为佩奇佩奇，唤醒成功后说前进、后退、左转、右转、旋转等进行控制。"))
        self.voice_audio_start.setText(_translate("tankWindow", "录音"))
        self.label_8.setText(_translate("tankWindow", "录音播放：使用车载麦克阵列及音箱进行录音及播放。"))
        self.voice_audio_stop.setText(_translate("tankWindow", "停止录音"))
        self.voice_audio_play.setText(_translate("tankWindow", "播放"))
        self.tabMenuWidget.setTabText(self.tabMenuWidget.indexOf(self.tab_voice), _translate("tankWindow", "语音技术"))
        self.camera_origin.setText(_translate("tankWindow", "原始画面"))
        self.camera_face.setText(_translate("tankWindow", "人脸识别"))
        self.camera_eyes.setText(_translate("tankWindow", "眼部识别"))
        self.camera_close.setText(_translate("tankWindow", "关闭"))
        self.tabMenuWidget.setTabText(self.tabMenuWidget.indexOf(self.tab_video), _translate("tankWindow", "视频处理"))
        self.btnRunLocal.setText(_translate("tankWindow", "本地运行"))
        self.btnRunStop.setText(_translate("tankWindow", "停止"))
        self.btnCodeImport.setText(_translate("tankWindow", "导入"))
        self.btnCodeSave.setText(_translate("tankWindow", "保存"))
        self.btnRunDevice.setText(_translate("tankWindow", "设备运行"))
        self.label_10.setText(_translate("tankWindow", "输出结果："))
        self.tabMenuWidget.setTabText(self.tabMenuWidget.indexOf(self.tab_code), _translate("tankWindow", "代码编辑"))
        self.toolBar.setWindowTitle(_translate("tankWindow", "toolBar"))
        self.actionExit.setText(_translate("tankWindow", "退出"))
        self.actionExit.setIconText(_translate("tankWindow", " 退出"))
        self.actionChange.setText(_translate("tankWindow", "主菜单"))
        self.actionChange.setIconText(_translate("tankWindow", " 主菜单"))
        self.actionInfo.setText(_translate("tankWindow", "使用说明"))
        self.actionInfo.setIconText(_translate("tankWindow", " 使用说明"))
        self.actionLogin.setText(_translate("tankWindow", "登录"))
        self.actionLogin.setIconText(_translate("tankWindow", " 登录"))
        self.actionText.setText(_translate("tankWindow", "设备号："))
        self.actionText.setIconText(_translate("tankWindow", "设备号："))
        self.actionText.setToolTip(_translate("tankWindow", "设备号："))
        self.actionStatus.setText(_translate("tankWindow", "未连接"))
        self.actionStatus.setIconText(_translate("tankWindow", " 未连接"))
