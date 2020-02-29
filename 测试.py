import sys
from PyQt5.QtCore import QCoreApplication
# 导入设计好的图形模块


if __name__=='__main__':
    # 创建一个应用进程，传入python环境变量作为参数
    app=QApplication(sys.argv)
    # 实例化界面类

    # 创建一个窗体对象
    window=QWidget()
    # 传入窗体对象给设置界面方法
    window.setWindowTitle('okok')
    window.resize(400,300)
    # 窗体展示
    window.show()
    # 死循环监控应用进程
    sys.exit(app.exec_())