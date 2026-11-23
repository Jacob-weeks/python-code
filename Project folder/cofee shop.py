#The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

price = 0
coffee = input("What type of coffee would you like?").title()
if coffee =="Espresso":
   price = price + 2.50
elif coffee =="Americano":
   price = price + 3
elif coffee =="Latte":
   price = price + 2.50
elif coffee == "cappuccino":
    price = price + 3
elif coffee == "macchiato":
    price = price + 2.50
elif coffee == "mocha":
    price = price + 3.50
elif coffee == "flat white":
    price = price + 2.50

size = input("would you like M, L, XL").upper
if size == "M":
    price = price + 0
elif size == "L":
    price = price + 1
elif size == "XL":
    price = price + 1.50


eatortake = input("would you like to eat in / [e], or takeaway / [t]")
if eatortake == "e":
    price = price + 0
elif eatortake == "t":
    price = price + 1
#Complete the code here...
print("----------------------------")
print("Total Cost: £" + str(price))