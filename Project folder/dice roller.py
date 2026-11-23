import random
your_roll = random.randint(1, 6)
print("------------------------------------------------------------------------------")
print("you rolled", your_roll)

VS_roll = random.randint(1, 6)
print("the AI rolled", VS_roll)
print("------------------------------------------------------------------------------")
if your_roll > VS_roll:
    print("\033[92myou win!\033[0m")
if your_roll < VS_roll:
    print("\033[91mthe AI wins!\033[0m")
elif your_roll == VS_roll:
    print("\033[93mits a tie!\033[0m")
print("------------------------------------------------------------------------------")