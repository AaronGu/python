
n = int(input())
if n == 1:
    print ([0])
#if n == 2:
#    print ([0,1])
else:
    fibs = [0,1]
    for i in list(range(3,n)):
        fibs.append(fibs[i - 1] + fibs[i - 2]
    print(fibs)
    
