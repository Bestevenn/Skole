import datetime
import time

dato1 = datetime.datetime.now()
dato2 = datetime()


t = datetime.timedelta(days=dato1)
s = datetime.timedelta(days=dato2)

ans = t-s 
print(ans)