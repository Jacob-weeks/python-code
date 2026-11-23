heartrate = int(input("what was the heart rate during that activity?"))
starttime = int(input("what was the start time?"))
endtime = int(input("what was the end time?"))
totaltime = (endtime - starttime)
if totaltime < 30:
    print("this activity was at a low level of difficulty")
elif totaltime > 30 and heartrate > 150:
    print("this activity was at a high level of difficulty")
else:
    print("this activity was at a medium level of difficulty")