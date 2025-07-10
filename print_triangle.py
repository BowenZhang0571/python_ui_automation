# print new file_name

rows=1
while(rows<=50):
    cols=1;
    while(cols<=50-rows):#控制空格数量
        print(" ",end='')
        cols+=1
        pass
    c=1
    while(c<=2*rows-1):#打印星号
        print("*",end='')
        c+=1
        pass
    print()
    rows+=1
    pass
