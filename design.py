# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileCheck(object):
    def setupUi(self, FileCheck):
        FileCheck.setObjectName("FileCheck")
        FileCheck.resize(1000, 650)
        FileCheck.setMinimumSize(QtCore.QSize(1000, 650))
        FileCheck.setMaximumSize(QtCore.QSize(1000, 650))
        self.textBrowser = QtWidgets.QTextBrowser(FileCheck)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 931, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(FileCheck)
        self.progressBar.setGeometry(QtCore.QRect(30, 590, 931, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.formLayoutWidget_2 = QtWidgets.QWidget(FileCheck)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 320, 934, 234))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.showbasef = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.showbasef.setMinimumSize(QtCore.QSize(725, 25))
        self.showbasef.setMaximumSize(QtCore.QSize(725, 25))
        self.showbasef.setObjectName("showbasef")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.showbasef)
        self.basef = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.basef.setMinimumSize(QtCore.QSize(50, 0))
        self.basef.setMaximumSize(QtCore.QSize(200, 25))
        self.basef.setObjectName("basef")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.basef)
        self.showcheckf = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.showcheckf.setMinimumSize(QtCore.QSize(725, 25))
        self.showcheckf.setMaximumSize(QtCore.QSize(725, 25))
        self.showcheckf.setObjectName("showcheckf")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.showcheckf)
        self.checkf = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.checkf.setMaximumSize(QtCore.QSize(200, 25))
        self.checkf.setObjectName("checkf")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkf)
        self.label1 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label1.setObjectName("label1")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.keyid = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.keyid.setMinimumSize(QtCore.QSize(0, 25))
        self.keyid.setMaximumSize(QtCore.QSize(16777215, 25))
        self.keyid.setObjectName("keyid")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.keyid)
        self.label2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label2.setObjectName("label2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.checkid = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.checkid.setMinimumSize(QtCore.QSize(725, 25))
        self.checkid.setObjectName("checkid")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkid)
        self.showoutf = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.showoutf.setMinimumSize(QtCore.QSize(725, 25))
        self.showoutf.setObjectName("showoutf")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.showoutf)
        self.outf = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.outf.setMinimumSize(QtCore.QSize(200, 25))
        self.outf.setMaximumSize(QtCore.QSize(200, 25))
        self.outf.setObjectName("outf")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.outf)
        self.startf = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.startf.setObjectName("startf")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.startf)

        self.retranslateUi(FileCheck)
        QtCore.QMetaObject.connectSlotsByName(FileCheck)

    def retranslateUi(self, FileCheck):
        _translate = QtCore.QCoreApplication.translate
        FileCheck.setWindowTitle(_translate("FileCheck", "Form"))
        self.textBrowser.setHtml(_translate("FileCheck", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FileCheck</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2019/5/18</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">该工具能够快速校对两个数据文档，并返回一个校对文件。</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* 输入说明</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- 原始文件：即需要与之对比的文件，一般为原始数据文件,CSV格式</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- 校对文件：即待校对文件，一般为提取的数据文件</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- 主键：即原始文件和校对文件都拥有的唯一标志ID</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- 校对键：即需要校对的数据条目名称，输入格式为&quot;校对键1;校对键2;...;校对键n&quot;，各个校对键之间务必以英文字符&quot;;&quot;隔开</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- 输出文件路径：即保存校对文件的合法路径</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* 注意</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- 主键和校对键名称必须同时存在于原始文件和校对文件之中，否则会报错</p></body></html>"))
        self.basef.setText(_translate("FileCheck", "原始文件"))
        self.checkf.setText(_translate("FileCheck", "校对文件"))
        self.label1.setText(_translate("FileCheck", "主键"))
        self.label2.setText(_translate("FileCheck", "校对键"))
        self.outf.setText(_translate("FileCheck", "输出文件路径"))
        self.startf.setText(_translate("FileCheck", "校对开始"))


