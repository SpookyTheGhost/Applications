from datetime import datetime, timedelta
from time import sleep
curr = datetime.now()
print(curr)
nextTime = curr + timedelta(seconds=3)
nextTime = nextTime.replace(microsecond=0)
print(nextTime)

while(1):
    sleep(1) # simulate chip clock move forward a unit
    curr = datetime.now()
    curr = curr.replace(microsecond=0)
    print(curr.time())
    print("waiting...")
    if (curr == nextTime):
        print("match")
        break
