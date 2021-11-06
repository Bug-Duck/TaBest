from PyQt5.QtWidgets import (QAction, QApplication,QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem, QWidget)  # pip install PyQt5
import json
"""
此文件用于处理qt界面上的表格数据,
属于前段范畴,
不对文件产生影响
"""
class QReadOenpTbFile(object):
    '用于将暂存区数据显示到qt界面上'
    def __init__(self,TbData,QtableWidgetObject):
        QtableWidgetObject.setRowCount(TbData.DataData['width'])        #设置Qt界面表格的行与列
        QtableWidgetObject.setColumnCount(TbData.DataData['length'])

        #遍历每一个单元格并显示到qt界面上
        for row in range(0,TbData.DataData["width"]):
            for hor in range(0,TbData.DataData["length"]):
                NewItem = QTableWidgetItem(TbData.FromData[row][hor])
                QtableWidgetObject.setItem(row,hor,NewItem)
                
class QGetTableWidgetList(object):
    '用于将qt界面上的数据储存到暂存区'
    def __init__(self,TableObject):
        Data = []
        self.hor_num = TableObject.columnCount()#获取当前的列数
        self.row_num = TableObject.rowCount()#获取当前的列数
        for row in range(0,self.row_num):
            Data.append([])
            for hor in range(0,self.hor_num):
                AData = TableObject.item(row,hor).text()
                Data[row].append(AData)
        self.Data = Data

class QCloseTable(object):
    def __init__(self,TableObject):
        TableObject.setRowCount(0)
        TableObject.setColumnCount(0)