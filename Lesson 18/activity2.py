import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    randomGenerator = random.random()
    deatFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, deatFormat))

    endtime = time.mktime(time.strptime(endDate,deatFormat))

    randomTime = startTime + randomGenerator *(endtime - startTime)

    randomDate = time.strftime(deatFormat, time.localtime(randomTime))

    return randomDate

print("Random date:", getRandomDate("1/1/2021", "1/1/2024"))