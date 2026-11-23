catyears = int(input("enter the age of your cat in cat years : "))
if catyears <= 2:   
    humanyears = catyears * 12
    print(humanyears)
else:
    humanyears = 24
    humanyears = humanyears + (catyears - 2)*6
    print(humanyears)