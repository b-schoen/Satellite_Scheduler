# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Help_Dialog.ui'
#
# Created: Sun Jan 17 20:04:43 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 373)
        self.help_stackedWidget = QtGui.QStackedWidget(Dialog)
        self.help_stackedWidget.setGeometry(QtCore.QRect(10, 20, 381, 311))
        self.help_stackedWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.help_stackedWidget.setObjectName(_fromUtf8("help_stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.schedule_creator_help_label = QtGui.QLabel(self.page)
        self.schedule_creator_help_label.setGeometry(QtCore.QRect(0, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.schedule_creator_help_label.setFont(font)
        self.schedule_creator_help_label.setObjectName(_fromUtf8("schedule_creator_help_label"))
        self.schedule_creator_help_text_edit = QtGui.QTextEdit(self.page)
        self.schedule_creator_help_text_edit.setGeometry(QtCore.QRect(0, 40, 371, 271))
        self.schedule_creator_help_text_edit.setReadOnly(True)
        self.schedule_creator_help_text_edit.setObjectName(_fromUtf8("schedule_creator_help_text_edit"))
        self.help_stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.schedule_viewer_help_label = QtGui.QLabel(self.page_2)
        self.schedule_viewer_help_label.setGeometry(QtCore.QRect(0, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.schedule_viewer_help_label.setFont(font)
        self.schedule_viewer_help_label.setObjectName(_fromUtf8("schedule_viewer_help_label"))
        self.schedule_viewer_help_text_edit = QtGui.QTextEdit(self.page_2)
        self.schedule_viewer_help_text_edit.setGeometry(QtCore.QRect(0, 40, 371, 271))
        self.schedule_viewer_help_text_edit.setReadOnly(True)
        self.schedule_viewer_help_text_edit.setObjectName(_fromUtf8("schedule_viewer_help_text_edit"))
        self.help_stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.console_help_label_2 = QtGui.QLabel(self.page_3)
        self.console_help_label_2.setGeometry(QtCore.QRect(0, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.console_help_label_2.setFont(font)
        self.console_help_label_2.setObjectName(_fromUtf8("console_help_label_2"))
        self.console_help_text_edit = QtGui.QTextEdit(self.page_3)
        self.console_help_text_edit.setGeometry(QtCore.QRect(0, 40, 371, 271))
        self.console_help_text_edit.setReadOnly(True)
        self.console_help_text_edit.setObjectName(_fromUtf8("console_help_text_edit"))
        self.help_stackedWidget.addWidget(self.page_3)
        self.help_done_button = QtGui.QPushButton(Dialog)
        self.help_done_button.setGeometry(QtCore.QRect(300, 340, 85, 27))
        self.help_done_button.setObjectName(_fromUtf8("help_done_button"))
        self.help_next_button = QtGui.QPushButton(Dialog)
        self.help_next_button.setGeometry(QtCore.QRect(70, 340, 61, 27))
        self.help_next_button.setObjectName(_fromUtf8("help_next_button"))
        self.help_prev_button = QtGui.QPushButton(Dialog)
        self.help_prev_button.setGeometry(QtCore.QRect(10, 340, 61, 27))
        self.help_prev_button.setObjectName(_fromUtf8("help_prev_button"))

        self.retranslateUi(Dialog)
        self.help_stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Help", None))
        self.schedule_creator_help_label.setText(_translate("Dialog", "Schedule Creator", None))
        self.schedule_viewer_help_label.setText(_translate("Dialog", "Schedule Viewer", None))
        self.console_help_label_2.setText(_translate("Dialog", "Console", None))
        self.help_done_button.setText(_translate("Dialog", "Done", None))
        self.help_next_button.setText(_translate("Dialog", "Next", None))
        self.help_prev_button.setText(_translate("Dialog", "Prev", None))

