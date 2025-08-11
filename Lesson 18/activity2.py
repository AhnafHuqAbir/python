import random
import time

def randomGanaretor(starttime, endtime):
    print(f"Generating random deat between {starttime} and {endtime}")
    rendomGenerator = random.random()
    deatFormet = '%m/%d/%y'

    starttime = time.mktime(time.strptime(starttime, deatFormet))
    endtime = time.mktime(time.strptime(endtime, deatFormet))

    random_time = starttime + randomGanaretor * (endtime - starttime)

    random_date = time.strftime(deatFormet, time.localtime(random_time))
print(f'Random_date: {randomGanaretor("01/01/2020", "12/31/2020")}')