# 内核0.1初代版本开发

## 怎么做?

- 使用json数据来存储,文件扩展名为.tb
- 初代要求尽量简单,不添加颜色,字体和大小等功能
- 内核与应用使用两个不同的版本号,可以实现多内核版本兼容

## json格式

```json
`{`

  `"Data":{`

​    `"name":"***.tb",`

​    `"V":"0.1",`

​    `"length":3,`

​    `"width":2`

  `},`

  `"From":[`

​    `["data1","data2","data3"],`

​    `["data4","data5","data6"]`

  `]`

`}`
```

存储为一个二维数组,Data中的长和宽**不是索引**

## 函数使用方法

### NewTb(name,mulu,length,width)

用于新建.tb文件

name:名称,记得加上文件扩展名

mulu:创建的文件的存储目录

length,width:表格的行数和列数

### OpenTb(name)

用于打开.tb文件,注意,这里打开的是一整个json数据

#### OpenTb.getFrom()

获取表格详细,返回一个二维数组

```python
Data = OpenTb('***.tb')
From = Data.OpenTb.getFrom()
print(From)
```

此时将会看到表格的全部数据

#### OpenTb.getData()

获取详细信息

### WriteTb(h,l,Data)

写入某行某列

```python
#写入第三行第四列,写入一个1
Data = OpenTb('***.tb')
From = Data.OpenTb.getFrom()
From.WriteTb(3,4,'1')
```

