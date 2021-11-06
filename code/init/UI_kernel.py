from PyQt5.QtWidgets import (QAction, QApplication,QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem, QWidget)  # pip install PyQt5
import json
"""
此文件用于处理qt界面上的表格数据,
属于前段范畴,
不对文件产生影响
"""
class QReadOenpTbFile(object):
    def __init__(self,TbData,QtableWidgetObject):
        for row in range(0,TbData.DataData["width"]):
            for hor in range(0,TbData.DataData["length"]):
                NewItem = QTableWidgetItem(TbData.FromData[row][hor])
                QtableWidgetObject.setItem(row,hor,NewItem)
                
class QGetTableWidgetList(object):
    def __init__(self,TableObject):
        Data = []
        self.hor_num = TableObject.columnCount()#获取当前的列数
        self.row_num = TableObject.rowCount()#获取当前的列数
        for row in range(0,self.row_num):
            Data.append([])
            for hor in range(0,self.hor_num):
                AData = TableObject.itemAt(row,hor).text()
                Data[row].append(AData)
        self.Data = Data
