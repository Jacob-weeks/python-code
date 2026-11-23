import random
yes = 1


target = 21
total1 = random.randint(1,11)
print("your first card is", total1)

while  yes == 1 and total1 < target:
    your_card = random.randint(1,11)
    print("your second card is ", your_card)
    total1 = total1 + your_card
    print("your total is ", total1)
    if total1 > target:
        print("you busted!")
        print("you lose")
        yes = 2
    else:
        yes = int(input("do you want to pull another card? 1 for yes, 2 for no: "))
    
    if yes != 2 :
        ai = random.randint(15, 21)
        diff1 = abs(target - total1)
        diff2 = abs(target - ai)
        
        if diff1 < diff2:
            closest = total1
            print("you win! your total is ", total1, "and the ai's total is ", ai)
        elif diff1 > diff2:
            closest = ai
            print("the AI wins! your total is ", total1, "and the ai's total is ", ai)
        elif total1 == ai:
            print("its a tie!")
