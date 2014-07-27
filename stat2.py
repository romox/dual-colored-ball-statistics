# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file,by_name,index,row_count):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    data =  table.col_values(index) #某一行数据 
    data.pop(0)
    data = [x for x in data if x != '']
    return data[-row_count:]

def occurrences(string, sub, input_count):
    result = []
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
            if start-1+input_count < len(string):
                result.append(int(string[string.index(sub,start-1)+input_count]))
        else:
            return (count, result)


def main():

   while True:
           name = raw_input('请输入文件名：')
           name = name + '.xls'
           col_count = input('请输入列数: ')
           row_count = input('请输入行数: ')
           # print col_count
           data = excel_table_byname(file=name, by_name=u'Sheet1', index=col_count,row_count=row_count)

           data = [str(int(i)) for i in data]
           datastring = ''.join(data)
           
           input_count = input("请输入2或3或4: ")
           inputstring = ''
           if input_count == 2 or inputstring == 3 or inputstring == 4:
             inputstring = raw_input("请输入一个序列(3个0到9的数，以空格隔开): ")
           else:
             assert inputstring, '输入错误，请重新输入'

           print inputstring
           print datastring
           print len(datastring)

           count,result =  occurrences(datastring,inputstring,input_count)

           zero = one = two = three = four = five = six = seven = eight = nine = 0

           for x in result:
            if x == 0:
              zero += 1 
            elif x == 1:
              one += 1
            elif x == 2:
              two += 1
            elif x == 3:
              three += 1 
            elif x == 4:
              four += 1
            elif x == 5:
              five += 1
            elif x == 6:
              six += 1
            elif x == 7:
              seven += 1
            elif x == 8:
              eight += 1
            elif x == 9:
              nine += 1  


           counts = {'zero': zero, 'one': one, 'two': two, 'three': three,
                     'four': four, 'five': five, 'six': six, 'seven': seven,
                     'eight': eight, 'nine': nine}

           print counts
           firstline = '在第%d列中' + inputstring + '一共出现了%d次'
           print firstline % (col_count, count)
           print '0出现了%(zero)s次' % counts
           print '1出现了%(one)s次' % counts
           print '2出现了%(two)s次' % counts
           print '3出现了%(three)s次' % counts
           print '4出现了%(four)s次' % counts
           print '5出现了%(five)s次' % counts
           print '6出现了%(six)s次' % counts
           print '7出现了%(seven)s次' % counts
           print '8出现了%(eight)s次' % counts
           print '9出现了%(nine)s次' % counts

if __name__=="__main__":
    main()
