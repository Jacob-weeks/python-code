a_count = 0
b_count = 0
c_count = 0

q1answer = input("how would you describe yourself? a) brave, b) loyal, or c) smart?")

if q1answer.lower() == "a":
    a_count += 1
elif q1answer.lower() == "b":
    b_count += 1
elif q1answer.lower() == "c":
    c_count += 1
else:
    print("sorry, i don't understand that response.")

q2answer = input("what is your favorite color? a) red, b) blue, or c) green?")

if q2answer.lower() == "a":
    a_count += 1
elif q2answer.lower() == "b":
    b_count += 1
elif q2answer.lower() == "c":
    c_count += 1
else:
    print("sorry, i don't understand that response.")

q3answer = input("what is your favorite animal? a) lion, b) dog, or c) owl?")
if q3answer.lower() == "a":
    a_count += 1
elif q3answer.lower() == "b":
    b_count += 1
elif q3answer.lower() == "c":
    c_count += 1
else:
    print("sorry, i don't understand that response.")

if a_count > b_count and a_count > c_count:
    print("you are harry potter")
elif b_count > a_count and b_count > c_count:
    print("you are ron weasley")
elif c_count > a_count and c_count > b_count:
    print("you are hermione granger")
else:
    print("you are a mix of all three characters")