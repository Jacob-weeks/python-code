keyboard = int(input("enter the keyboard usage from this user: "))
completed = int(input("enter the completed task score from this user: "))
feedback = int(input("enter the feedback score from this user: "))
teamwork = int(input("enter the teamwork from this user: "))
quality =  int(input("enter the quality from this user: "))
total = keyboard + completed + feedback + teamwork + quality
weight = total / 100
print(weight)