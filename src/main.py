import pyautogui
import keyboard
import time
from window import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class RunThread(QtCore.QThread):
    finished = QtCore.pyqtSignal()  # 用于发出任务完成的信号

    def __init__(self, parent=None):
        super(RunThread, self).__init__(parent)
        self.running_flag = True
        self.datatime = 60
        self.datapage = 4

    def run(self):
        num = 2
        while self.running_flag:
            time.sleep(self.datatime)
            pyautogui.hotkey('ctrl', str(num))
            time.sleep(0.5)
            pyautogui.hotkey('F5')
            num += 1
            if num == self.datapage + 1:
                num = 1

        self.finished.emit()  # 发出任务完成信号

class myapp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Run1)
        self.pushButton_2.clicked.connect(self.Stop1)
        self.datatime = 60
        self.datapage = 4
        self.running_flag = False
        self.run_thread = RunThread()

        self.run_thread.finished.connect(self.on_thread_finished, QtCore.Qt.QueuedConnection)  # 使用Qt.QueuedConnection连接信号

    def Run1(self):
        self.running_flag = True
        self.datatime = int(self.lineEdit.text())
        self.datapage = int(self.comboBox.currentText())

        if self.datatime > 0 and self.datapage > 0:
            self.run_thread.running_flag = True
            self.run_thread.datatime = self.datatime
            self.run_thread.datapage = self.datapage
            self.run_thread.start()
        else:
            # 添加警告对话框
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("请输入有效的数据时间和数据页数。")
            msg.setWindowTitle("警告")
            msg.exec()

    def Stop1(self):
        self.run_thread.running_flag = False

    def on_thread_finished(self):
        self.running_flag = False
        # 在此处可以执行一些完成后的操作

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = myapp()
    mainWindow.show()
    sys.exit(app.exec_())
