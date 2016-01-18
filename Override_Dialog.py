# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Override_Dialog.ui'
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

class Ui_Override_Dialog(object):
    def setupUi(self, Override_Dialog):
        Override_Dialog.setObjectName(_fromUtf8("Override_Dialog"))
        Override_Dialog.resize(407, 246)
        self.override_constraint_message_label = QtGui.QLabel(Override_Dialog)
        self.override_constraint_message_label.setGeometry(QtCore.QRect(30, 60, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.override_constraint_message_label.setFont(font)
        self.override_constraint_message_label.setWordWrap(True)
        self.override_constraint_message_label.setObjectName(_fromUtf8("override_constraint_message_label"))
        self.override_message_label_1 = QtGui.QLabel(Override_Dialog)
        self.override_message_label_1.setGeometry(QtCore.QRect(30, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.override_message_label_1.setFont(font)
        self.override_message_label_1.setObjectName(_fromUtf8("override_message_label_1"))
        self.override_message_label_2 = QtGui.QLabel(Override_Dialog)
        self.override_message_label_2.setGeometry(QtCore.QRect(30, 160, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.override_message_label_2.setFont(font)
        self.override_message_label_2.setObjectName(_fromUtf8("override_message_label_2"))
        self.override_yes_button = QtGui.QPushButton(Override_Dialog)
        self.override_yes_button.setGeometry(QtCore.QRect(30, 200, 85, 27))
        self.override_yes_button.setObjectName(_fromUtf8("override_yes_button"))
        self.override_no_button = QtGui.QPushButton(Override_Dialog)
        self.override_no_button.setGeometry(QtCore.QRect(290, 200, 85, 27))
        self.override_no_button.setObjectName(_fromUtf8("override_no_button"))

        self.retranslateUi(Override_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Override_Dialog)

    def retranslateUi(self, Override_Dialog):
        Override_Dialog.setWindowTitle(_translate("Override_Dialog", "Override", None))
        self.override_constraint_message_label.setText(_translate("Override_Dialog", "Override Message", None))
        self.override_message_label_1.setText(_translate("Override_Dialog", "Overridable conflict: ", None))
        self.override_message_label_2.setText(_translate("Override_Dialog", "Would you like to override?", None))
        self.override_yes_button.setText(_translate("Override_Dialog", "Yes", None))
        self.override_no_button.setText(_translate("Override_Dialog", "No", None))

