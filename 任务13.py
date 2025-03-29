def slice_with_step(mylist,start,step):
    return mylist[start::step]
L1=[11,2,33,4,5,6,7,8,9]
start=1
step=2
result=slice_with_step(L1,start,step)
print(result)