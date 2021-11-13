"""
版本:0.1
开发者:箱子
时间:2021年11月6日
"""
import json

class NewTb(object):
    def __init__(self,name,length,width):
        """
        name:文件名
        mulu:文件存储目录
        length:表格的长
        width:表格的宽
        """
        with open(name,'w',encoding='utf-8-sig') as f:
            self.Data = {"Data":{'name':name,'V':'1.0','length':length,'width':width},'From':[]}
            #遍历并添加空字符串项
            for i in range(1,width+1):
                self.Data['From'].append([])
                for i2 in range(1,length+1):
                    self.Data['From'][i-1].append("")
            self.jsonData = json.dumps(self.Data)
            f.write(self.jsonData)

class OpenTb(object):
    def __init__(self,name):
        # with open(self.ex[0],'r') as f:
        #     print(f.read())
        self = open(name,'r',encoding='utf-8-sig')
        self.Data = json.loads(self.read())
        # print(self.Data)
        self.FromData = self.Data['From']
        self.FileData = self.Data['Data']
        # print(self.FromData, self.DataData)

    def getFrom(self):
        return self.FromData

    def getFileData(self):
        return self.FileData

    def writeCell(self,row,hor,text):
        self.FromData[row-1][hor-1] = text

    def FileClose(self):
        self.Data['From'] = self.FromData
        self.Data['Data'] = self.FileData
        self.close()
