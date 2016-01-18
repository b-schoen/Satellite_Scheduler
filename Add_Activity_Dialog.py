# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Activity_Dialog.ui'
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

class Ui_Add_Activity_Dialog(object):
    def setupUi(self, Add_Activity_Dialog):
        Add_Activity_Dialog.setObjectName(_fromUtf8("Add_Activity_Dialog"))
        Add_Activity_Dialog.resize(400, 288)
        self.parameters_line_edit = QtGui.QLineEdit(Add_Activity_Dialog)
        self.parameters_line_edit.setGeometry(QtCore.QRect(120, 190, 271, 27))
        self.parameters_line_edit.setObjectName(_fromUtf8("parameters_line_edit"))
        self.start_time_spin_box = QtGui.QDoubleSpinBox(Add_Activity_Dialog)
        self.start_time_spin_box.setGeometry(QtCore.QRect(120, 110, 62, 27))
        self.start_time_spin_box.setObjectName(_fromUtf8("start_time_spin_box"))
        self.stop_time_spin_box = QtGui.QDoubleSpinBox(Add_Activity_Dialog)
        self.stop_time_spin_box.setGeometry(QtCore.QRect(120, 150, 62, 27))
        self.stop_time_spin_box.setObjectName(_fromUtf8("stop_time_spin_box"))
        self.start_time_label = QtGui.QLabel(Add_Activity_Dialog)
        self.start_time_label.setGeometry(QtCore.QRect(10, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_time_label.setFont(font)
        self.start_time_label.setObjectName(_fromUtf8("start_time_label"))
        self.stop_time_label = QtGui.QLabel(Add_Activity_Dialog)
        self.stop_time_label.setGeometry(QtCore.QRect(10, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stop_time_label.setFont(font)
        self.stop_time_label.setObjectName(_fromUtf8("stop_time_label"))
        self.parameters_label = QtGui.QLabel(Add_Activity_Dialog)
        self.parameters_label.setGeometry(QtCore.QRect(10, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.parameters_label.setFont(font)
        self.parameters_label.setObjectName(_fromUtf8("parameters_label"))
        self.main_activity_dialog_label = QtGui.QLabel(Add_Activity_Dialog)
        self.main_activity_dialog_label.setGeometry(QtCore.QRect(10, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.main_activity_dialog_label.setFont(font)
        self.main_activity_dialog_label.setObjectName(_fromUtf8("main_activity_dialog_label"))
        self.activity_view_constraints_button = QtGui.QPushButton(Add_Activity_Dialog)
        self.activity_view_constraints_button.setGeometry(QtCore.QRect(10, 240, 111, 27))
        self.activity_view_constraints_button.setObjectName(_fromUtf8("activity_view_constraints_button"))
        self.close_button = QtGui.QPushButton(Add_Activity_Dialog)
        self.close_button.setGeometry(QtCore.QRect(190, 240, 81, 27))
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.add_activity_button = QtGui.QPushButton(Add_Activity_Dialog)
        self.add_activity_button.setGeometry(QtCore.QRect(280, 240, 111, 27))
        self.add_activity_button.setObjectName(_fromUtf8("add_activity_button"))
        self.thing_label = QtGui.QLabel(Add_Activity_Dialog)
        self.thing_label.setGeometry(QtCore.QRect(10, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thing_label.setFont(font)
        self.thing_label.setObjectName(_fromUtf8("thing_label"))
        self.thing_combo_box = QtGui.QComboBox(Add_Activity_Dialog)
        self.thing_combo_box.setGeometry(QtCore.QRect(120, 70, 131, 25))
        self.thing_combo_box.setObjectName(_fromUtf8("thing_combo_box"))
        self.thing_combo_box.addItem(_fromUtf8(""))
        self.thing_combo_box.addItem(_fromUtf8(""))
        self.thing_combo_box.addItem(_fromUtf8(""))
        self.thing_combo_box.addItem(_fromUtf8(""))
        self.thing_combo_box.addItem(_fromUtf8(""))

        self.retranslateUi(Add_Activity_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Add_Activity_Dialog)

    def retranslateUi(self, Add_Activity_Dialog):
        Add_Activity_Dialog.setWindowTitle(_translate("Add_Activity_Dialog", "Activity", None))
        self.start_time_label.setText(_translate("Add_Activity_Dialog", "Start Time", None))
        self.stop_time_label.setText(_translate("Add_Activity_Dialog", "Stop Time", None))
        self.parameters_label.setText(_translate("Add_Activity_Dialog", "Parameters", None))
        self.main_activity_dialog_label.setText(_translate("Add_Activity_Dialog", "Add Activity", None))
        self.activity_view_constraints_button.setText(_translate("Add_Activity_Dialog", "View Constraints", None))
        self.close_button.setText(_translate("Add_Activity_Dialog", "Cancel", None))
        self.add_activity_button.setText(_translate("Add_Activity_Dialog", "Add Activity", None))
        self.thing_label.setText(_translate("Add_Activity_Dialog", "Thing", None))
        self.thing_combo_box.setItemText(0, _translate("Add_Activity_Dialog", "Thing 1", None))
        self.thing_combo_box.setItemText(1, _translate("Add_Activity_Dialog", "Thing 2", None))
        self.thing_combo_box.setItemText(2, _translate("Add_Activity_Dialog", "Thing 3", None))
        self.thing_combo_box.setItemText(3, _translate("Add_Activity_Dialog", "Thing 4", None))
        self.thing_combo_box.setItemText(4, _translate("Add_Activity_Dialog", "Thing 5", None))

