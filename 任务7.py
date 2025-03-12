a =  input("输入一列整数或浮点数，用逗号隔开:")
b = [float(num) if "." in num else int(num) for num in a.split(",")]
total = sum(b)
print("总和为：",total)