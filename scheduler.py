import schedule
import time
import sys
import os

def job():
    tot_sec=sys.argv[2]
    os.system("sudo rtcwake -m mem -s "+str(tot_sec))


total_min = int(sys.argv[1])+int(sys.argv[2])


schedule.every(int(sys.argv[1])).seconds.do(job)
print(total_min)

while True:
    schedule.run_pending()
    time.sleep(1)
