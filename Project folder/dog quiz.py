a_count = 0
b_count = 0
c_count = 0

q1answer = input("how would you describe yourself? a)adventurous , b) gentle, or c) curious?")

if q1answer.lower() == "a":
    a_count += 1
elif q1answer.lower() == "b":
    b_count += 1
elif q1answer.lower() == "c":
    c_count += 1
else:
    print("sorry, i don't understand that response.")

q2answer = input("what is your favorite color? a) gold, b) white, or c) grey?")

if q2answer.lower() == "a":
    a_count += 1
elif q2answer.lower() == "b":
    b_count += 1
elif q2answer.lower() == "c":
    c_count += 1
else:
    print("sorry, i don't understand that response.")

q3answer = input("what is your favorite activity? a) playing fetch, b) going for walks, or c) cuddling? ")
if q3answer.lower() == "a":
    a_count += 1
elif q3answer.lower() == "b":
    b_count += 1
elif q3answer.lower() == "c":
    c_count += 1
else:
    print("sorry, i don't understand that response.")

if a_count > b_count and a_count > c_count:
    print("you like golden retrievers")
elif b_count > a_count and b_count > c_count:
    print("you like labradors")
elif c_count > a_count and c_count > b_count:
    print("you like huskies")
else:
    print("you like a mix of all breeds!")