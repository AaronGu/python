import math
for n in list(range(100,1000)):
    i = n // 100
    j = n // 10 % 10
    k = n % 10
    #print(str(i)+"  "+str(j)+"  "+str(k))
    if n == (i ** 3 + j ** 3 + k ** 3):
        print (n) 

