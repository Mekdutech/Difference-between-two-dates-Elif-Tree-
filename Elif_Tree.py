
import time

date1 = str(input("Please enter first date in this format dd/mm/yyyy:"))
a,b,c = date1.split("/")
date2=str(input("Please enter end date in this format dd/mm/yyyy:"))
d,e,f=date2.split("/")

a=int(a)
b=int(b)
c,d=int(c),int(d)
e,f=int(e),int(f)
if b==1:
    days1=a+(c*365)
elif b==2:
    days1=a+31+(c*365)
elif b==3:
    days1=a+31+28+(c*365)
elif b==4:
    days1=a+31+28+31+(c*365)
elif b==5:
    days1=a+31+28+31+30+(c*365)
elif b==6:
    days1=a+31+28+31+30+31+(c*365)
elif b==7:
    days1=a+31+28+31+30+31+30+(c*365)
elif b==8:
    days1=a+31+28+31+30+31+30+31+(c*365)
elif b==9:
    days1=a+31+28+31+30+31+30+31+30+(c*365)
elif b==10:
    days1=a+31+28+31+30+31+30+31+30+31+(c*365)
elif b==11:
    days1=a+31+28+31+30+31+30+31+30+31+30+(c*365)
else:
    days1=a+31+28+31+30+31+30+31+30+31+30+31+(c*365)
if e==1:
    days2=d+(f*365)
elif e==2:
    days2=d+31+(f*365)
elif e==3:
    days2=d+31+28+(f*365)
elif e==4:
    days2=d+31+28+31+(f*365)
elif e==5:
    days2=d+31+28+31+30+(f*365)
elif e==6:
    days2=d+31+28+31+30+31+(f*365)
elif e==7:
    days2=d+31+28+31+30+31+30+(f*365)
elif e==8:
    days2=d+31+28+31+30+31+30+31+(f*365)
elif e==9:
    days2=d+31+28+31+30+31+30+31+30+(f*365)
elif e==10:
    days2=d+31+28+31+30+31+30+31+30+31+(f*365)
elif e==11:
    days2=d+31+28+31+30+31+30+31+30+31+30+(f*365)
else:
    days2=d+31+28+31+30+31+30+31+30+31+30+31+(f*365)

days = abs(days1-days2)

print ("The difference between the dates is ", days, "days,  ")


