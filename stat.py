# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'file.xls',index=20,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    data =  table.col_values(index) #某一行数据 
    data.pop(0)
    data = [x for x in data if x != '']
    return data

def occurrences(string, sub):
    result = []
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
            if start-1+4 < len(string):
                result.append(int(string[string.index(sub,start-1)+4]))
        else:
            return (count, result)


def main():

   col = input('请输入列数: ')
   # print col
   data = excel_table_byname(index=col)

   data = [str(int(i)) for i in data]
   datastring = ''.join(data)

   var1,var2,var3,var4 = raw_input("请输入一个序列(4个0到2的数，以空格隔开): ").split()
   inputstring = var1+var2+var3+var4

   # print inputstring
   # print datastring
   # print len(datastring)

   count,result =  occurrences(datastring,inputstring)

   zero = one = two = 0

   for x in result:
    if x == 0:
      zero += 1 
    if x == 1:
      one += 1
    if x == 2:
      two += 1

   counts = {'zero': zero, 'one': one, 'two': two}

   # print counts
   firstline = '在第%d列中' + inputstring + '一共出现了%d次'
   print firstline % (col, count)
   print '0出现了%(zero)s次' % counts
   print '1出现了%(one)s次' % counts
   print '2出现了%(two)s次' % counts

if __name__=="__main__":
    main()