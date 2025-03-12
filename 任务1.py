a=1
b=1
for a in range(1,10):
    for b in range(1,a+1):
     print(f"{a}*{b}={a*b:1}", end=" ")
    print()