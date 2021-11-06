import sys,os
import re
import json
from PyQt5.QtWidgets import (QAction, QApplication,QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem, QWidget)  # pip install PyQt5
sys.path.append("~\\UI")
sys.path.append('~\\operate')
import UI,kernel,UI_kernel
from operate import *

class MainWindow(QMainWindow, UI.Ui_MainWindow):
    #主窗口
    def __init__(self, parent=None):    
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.open.triggered.connect(self.read_ex)
        self.NewFile.triggered.connect(self.CallNewFileWindow)
        self.save.triggered.connect(self.Save)
        self.showMaximized()
        
        
    def read_ex(self):
        try:
            self.ex = QFileDialog.getOpenFileName(self,'选择表格文件','c://','TaBest files(*.tb)')
            self.Tb = kernel.OpenTb(self.ex[0])
            self.FileOpenNow = self.ex[0]
            self.tableWidget.setRowCount(self.Tb.DataData['width'])
            self.tableWidget.setColumnCount(self.Tb.DataData['length'])
            UI_kernel.QReadOenpTbFile(self.Tb,self.tableWidget)
        except:
            pass
        self.NowOpen = self.FileOpenNow

    def CallNewFileWindow(self):
        self.NewFileWin = NewFileWindow()
        self.NewFileWin.show()
        self.NewFileWin.Yes.clicked.connect(self.NewTableShow)
        # print(self.NewFileName)
        
    def NewTableShow(self):
        self.NewFileWin.close()
        self.NewFileName = QFileDialog.getSaveFileName(self,'保存','C:\\TaBestFile.tb','tb(*.tb)')
        kernel.NewTb(self.NewFileName[0],self.NewFileWin.hor.value(),self.NewFileWin.row.value())
        self.Tb = kernel.OpenTb(self.NewFileName[0])
        self.NowOpen = self.NewFileName[0]
        UI_kernel.QReadOenpTbFile(self.Tb,self.tableWidget)
    def Save(self):
        # NowData = UI_kernel.QGetTableWidgetList(self.tableWidget)
        # print(NowData)
        # # self.Tb.Data["From"] = NowData.Data
        # # # print(self.Tb.Data)
        # # self.NowjsonData = json.dumps(self.Tb.Data)
        # # with open(self.NowOpen,'w') as f:
        # #         NowJsonData = json.dumps(self.Tb.Data)
        # #         f.write(NowJsonData)
        Data = []
        self.hor_num = self.tableWidget.columnCount()#获取当前的列数
        self.row_num = self.tableWidget.rowCount()#获取当前的列数
        for row in range(0,self.row_num):
            Data.append([])
            for hor in range(0,self.hor_num):
                AData = self.tableWidget.itemAt(row,hor).text()
                print(AData)
                # Data[row].append(AData)
        # self.Data = Data
        # print(self.Data)


class NewFileWindow(QWidget, UI.Ui_NewFile):
    def __init__(self, parent=None):
        super(NewFileWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)  
    myWin = MainWindow()  
    myWin.show()  
    sys.exit(app.exec_())
