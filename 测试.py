
import sys
from PyQt5.QtWidgets import QApplication,QWidget
# 导入设计好的图形模块
import untitled

if __name__=='__main__':
    # 创建一个应用进程，传入python环境变量作为参数
    app=QApplication(sys.argv)
    # 实例化界面类
    windowclass=untitled.Ui_Form()
    # 创建一个窗体对象
    window=QWidget()
    # 传入窗体对象给设置界面方法
    windowclass.setupUi(window)
    # 窗体展示
    window.show()
    # 死循环监控应用进程
    sys.exit(app.exec_())