stop = True
stop1 = True
print("welcome to the naughty and nice list")
nicelist = []
naughtylist = []
while stop == True:
    naughty = input("who do you want to add to the naughty list?: ")
    naughtylist.append(naughty)
    choice = input("press enter to add someone else to the naughty list or type 'done' to finish: ")
    if choice == 'done':
        stop = False

while stop1 == True:
    nice = input("who do you want to add to the nice list?: ")
    nicelist.append(nice)
    choice1 = input("press enter to add someone else to the nice list or type 'done' to finish: ")
    if choice1 == 'done':
        stop1 = False

print("Naughty List:", naughtylist)
print("Nice List:", nicelist)
