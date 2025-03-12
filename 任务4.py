def print_n(n):
    if not isinstance(n, int) or n <=1:
        print("请输入大于1的整数") 
        return
    for i in range(2, n):
        print(i)
try:
    n=int(input("输入大于1的整数："))
    print_n(n)
except ValueError:
    print("无效，请检查后重新输入")