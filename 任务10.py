a=input("输入一串有相同数字的数，用逗号隔开")
b=a.split(',')
c=list(set(b))
print("去重后：",",".join(c))