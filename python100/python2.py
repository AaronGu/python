
i = int(input("jlr:"))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in [0,1,2,3,4,5]:
    if i > arr[idx]:
        r += ((i-arr[idx])*rat[idx])
        print ((i-arr[idx])*rat[idx])
        i = arr[idx]
print (r)