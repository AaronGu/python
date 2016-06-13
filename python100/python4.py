year = int(input("请输入年:\n"))
month = int(input("请输入月:\n"))
day = int(input("请输入日:\n"))
idx = 0

months =[0,31,59,90,120,151,181,212,243,273,304,334]
if 0 < month <= 12:
    months_sum = months[month -1]
else:
    print("输入错误！")
idx = months_sum + day
if str(type(year/4)) == str(type(1)):
    idx += 1
    print(str(year)+"年"+str(month)+"月"+str(day)+"日是第"+str(idx)+"天")
else:
    print(str(year)+"年"+str(month)+"月"+str(day)+"日是第"+str(idx)+"天")    