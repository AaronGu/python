import math
leap = 1
for m in list(range(101,201)):
    k = int(sqrt(m))
    for i in list(range(2,k+1)):
        if m % i == 0:
        leap = 0
        break
    if leap == 1:
        print ('%-4d' %m)
        h += 1
        if h % 10 == 0:
            print ''
    leap = 1
print ('The total is %d' %h)
