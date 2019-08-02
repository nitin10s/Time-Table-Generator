from datetime import datetime, timedelta

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta
def fun(interval):
    new=[]
    dts1 = [dt.strftime('%H:%M') for dt in
           datetime_range(datetime(2016, 9, 1, 9), datetime(2016, 9, 1, 9+8),
           timedelta(minutes=interval))]
    return dts1


i = int(raw_input())
arr=fun(i)
for i in range(0,len(arr)-1):
    print arr[i],arr[i+1]
