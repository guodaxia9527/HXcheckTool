import sys
from PyQt5.QtWidgets import QApplication,QWidget,QTableWidgetItem,QMessageBox
from PyQt5.QtGui import QFont,QColor,QIcon
# 导入设计好的图形模块
import check
import 文本校对 as ck


if __name__=='__main__':
    data = ck.read_exceldata()
    print('数据库载入ok-->',data)
    app=QApplication(sys.argv)
    windowclass=check.Ui_Form()
    window=QWidget()
    windowclass.setupUi(window)

    def msg(self):
        reply = QMessageBox.warning(self,  # 使用infomation信息框
                                        "找不到数据库文件！",
                                        "请确保data.xlsx文件在本目录下\n程序退出！",
                                        QMessageBox.Yes )
        sys.exit(1)

    def isnull_msg(self):
        reply = QMessageBox.warning(self,  # 使用infomation信息框
                                        "查询值不能为空！",
                                        "请左侧输入要查询的规范编号或名称！",
                                        QMessageBox.Yes )



    def selectbox():
        selecttext=windowclass.comboBox.currentText()
        if selecttext=='主要信息':
            windowclass.tableWidget.setColumnHidden(1, True)
            windowclass.tableWidget.setColumnHidden(4, True)
            windowclass.tableWidget.setColumnHidden(5, True)
            windowclass.tableWidget.setColumnHidden(6, True)
        else:
            windowclass.tableWidget.setColumnHidden(1, False)
            windowclass.tableWidget.setColumnHidden(4, False)
            windowclass.tableWidget.setColumnHidden(5, False)
            windowclass.tableWidget.setColumnHidden(6, False)


    def setfont():
        font = QFont('微软雅黑', 10)
        font.setBold(True)  # 设置字体加粗
        windowclass.tableWidget.horizontalHeader().setFont(font)  # 设置表头字体
        # windowclass.tableWidget.horizontalHeader().setLineWidth(1)
        windowclass.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section { border-bottom: 1px solid gray; }")


    def clear_table():
        windowclass.tableWidget.setRowCount(0)
        # windowclass.tableWidget.clearContents()


    # 获取文本框内容
    def get_txtlist():
        l=[]
        t=windowclass.plainTextEdit.toPlainText()
        for i in t.split('\n'):
            if i!="":

                l.append(i)
        # print(l)
        return l

    def gotorun():
        # 查询前清空表格内容
        clear_table()
        # 获取时间
        tiaojantime = windowclass.dateEdit.date()
        res_list=[]
        txtlist=get_txtlist()
        if len(txtlist)<=0:
            # print('请右侧输入查询内容！')
            isnull_msg(window)
            return '终止'
        for i in txtlist:
            # print(i)
            l=ck.main_query(i,tiaojantime,data)
            if isinstance(l,list):
                l.insert(0,i)
            else:
                l=i+",,,,,"+l
            # print(l)
            res_list.append(l)
        # print('文本框载入处理结果-->',res_list)

        # 导出到Tableviw
        count=0
        for j in res_list:
            windowclass.tableWidget.insertRow(count)
            if isinstance(j, str):
                # print('没查到:',j)
                windowclass.tableWidget.setItem(count, 0, QTableWidgetItem(j.split(",,,,,")[0]))
                windowclass.tableWidget.setItem(count, 1, QTableWidgetItem(j.split(",,,,,")[1]))
                windowclass.tableWidget.item(count,0).setForeground(QColor(255, 0, 0))
                windowclass.tableWidget.item(count,1).setForeground(QColor(255,0,0))

            else:
                # print('查到了:',j)
                windowclass.tableWidget.setItem(count, 0, QTableWidgetItem(j[0]))     #查询内容
                windowclass.tableWidget.setItem(count, 1, QTableWidgetItem(j[1]))     #完整名称
                windowclass.tableWidget.setItem(count, 2, QTableWidgetItem(j[2]))     #废止状态
                windowclass.tableWidget.setItem(count, 3, QTableWidgetItem(j[3]))     #可用情况
                kyqk=windowclass.tableWidget.item(count, 3).text()
                if kyqk=="不可用，规范已废弃":
                    windowclass.tableWidget.item(count, 3).setBackground(QColor(255, 0, 0))
                windowclass.tableWidget.setItem(count, 4, QTableWidgetItem(j[4]))     #生效时间
                windowclass.tableWidget.setItem(count, 5, QTableWidgetItem(j[5]))     #代替情况
            count=count+1
        windowclass.tableWidget.resizeColumnsToContents()



    windowclass.pushButton_2.clicked.connect(gotorun)
    windowclass.pushButton.clicked.connect(clear_table)
    windowclass.comboBox.currentTextChanged.connect(selectbox)
    windowclass.dateEdit.dateChanged.connect(gotorun)
    windowclass.plainTextEdit.textChanged.connect(gotorun)
    # 数据库检查
    if data is None:
        # print('没找到数据库，确保data.xlsx文件在本exe目录下')
        msg(window)


    setfont()    # 设置表头格式
    selectbox()  # 显示combox内容
    window.setWindowTitle('华信文本设计依据校对工具2.0')
    app.setWindowIcon(QIcon(r'C:\Users\Administrator\PycharmProjects\untitled1\校对2.png'))
    window.show()
    sys.exit(app.exec_())

