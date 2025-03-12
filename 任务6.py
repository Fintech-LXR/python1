a =  input("输入一列数，用逗号隔开:")
b = [int(num) for num in a.split(",")]
c = [num for num in b if num % 2 == 0]
print("列表中偶数有：",c)