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
            self.Data = {"Data":{'name':name,'V':'0.1','length':length,'width':width},'From':[]}
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
        with open(name,'r',encoding='utf-8-sig') as f:
            self.Data = json.loads(f.read())
            # print(self.Data)
            self.FromData = self.Data['From']
            self.DataData = self.Data['Data']
            # print(self.FromData, self.DataData)
class getFrom(object):   
    def __init__(self):
        self.FromData = json.loads(self)
        return self.FromData['From']

class getData(object):
    def __init__(self):
        self.DataData = json.loads(self)
        return self.DataData['Data']