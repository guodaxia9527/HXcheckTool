# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChildUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setRowCount(20)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.horizontalLayout_2.addWidget(self.tableWidget_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "标准编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "标准名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "实施时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "废弃时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "标准状态"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "代替情况"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "备注"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "标准库"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "标准编号"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "标准名称"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "实施时间"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "废弃时间"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "标准状态"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "代替情况"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Form", "备注"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "自定义库"))
        self.pushButton_4.setText(_translate("Form", "导出Excel"))
