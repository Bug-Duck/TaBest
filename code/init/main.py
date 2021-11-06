import sys,os
import re
import json
from PyQt5.QtWidgets import (QAction, QApplication,QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem, QWidget)  # pip install PyQt5
sys.path.append("~\\UI")
sys.path.append('~\\operate')
import UI,TBDD,UI_kernel
from operate import *

class MainWindow(QMainWindow, UI.Ui_MainWindow):
    #主窗口
    def __init__(self, parent=None):    
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.open.triggered.connect(self.read_ex)
        self.NewFile.triggered.connect(self.CallNewFileWindow)
        self.save.triggered.connect(self.Save)
        
        
    def read_ex(self):
        try:
            self.ex = QFileDialog.getOpenFileName(self,'选择表格文件','c://','TaBest files(*.tb)')  #让用户选择需要打开的文件
            self.Tb = TBDD.OpenTb(self.ex[0])                                                      #打开文件
            self.FileOpenNow = self.ex[0]                                                          #读取现在正在打开的文件路径
            self.tableWidget.setRowCount(self.Tb.DataData['width'])
            self.tableWidget.setColumnCount(self.Tb.DataData['length'])
            UI_kernel.QReadOenpTbFile(self.Tb,self.tableWidget)                                    #将数据显示到前端qt界面上
        except:
            pass
        self.NowOpen = self.FileOpenNow

    def CallNewFileWindow(self):
        self.NewFileWin = NewFileWindow()                       #初始化新建文件窗口
        self.NewFileWin.show()                                  #显示窗口
        self.NewFileWin.Yes.clicked.connect(self.NewTableShow)  #将底部"确定"按钮绑定槽函数
        # print(self.NewFileName)
        
    def NewTableShow(self):
        self.NewFileWin.close()                                                                     #关闭窗口
        self.NewFileName = QFileDialog.getSaveFileName(self,'保存','C:\\TaBestFile.tb','tb(*.tb)')  #让用户选择存储路径
        TBDD.NewTb(self.NewFileName[0],self.NewFileWin.hor.value(),self.NewFileWin.row.value())     #新建TB文件
        self.Tb = TBDD.OpenTb(self.NewFileName[0])                                                  #打开tb文件至暂存区(暂存区指self.Tb)
        self.NowOpen = self.NewFileName[0]                                                          #读取现在正在打开的文件路径
        UI_kernel.QReadOenpTbFile(self.Tb,self.tableWidget)                                         #将数据显示到前端qt界面上

    def Save(self):
        NowData = UI_kernel.QGetTableWidgetList(self.tableWidget)   #将前端表格上的数据同步到暂存区
        # print(NowData)
        self.Tb.Data["From"] = NowData.Data                         #与上一行(忽略注释)同理
        # print(self.Tb.Data)
        self.NowjsonData = json.dumps(self.Tb.Data)                 #将暂存区数据转化为json文本
        with open(self.NowOpen,'w',encoding='utf-8-sig') as f:      #写入
                NowJsonData = json.dumps(self.Tb.Data)
                f.write(NowJsonData)
        # Data = []
        # self.hor_num = self.tableWidget.columnCount()#获取当前的列数
        # self.row_num = self.tableWidget.rowCount()#获取当前的列数
        # for row in range(0,self.row_num):
        #     Data.append([])
        #     for hor in range(0,self.hor_num):
        #         AData = self.tableWidget.item(row,hor).text()
        #         # print(AData)
        #         Data[row].append(AData)
        # self.Data = Data
        # # print(self.Data)


class NewFileWindow(QWidget, UI.Ui_NewFile):
    "此窗口为新建文件窗口"
    def __init__(self, parent=None):
        super(NewFileWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)  
    myWin = MainWindow()  
    myWin.show()  
    sys.exit(app.exec_())
