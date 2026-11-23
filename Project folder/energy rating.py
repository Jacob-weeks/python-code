#colours
RESET = '\033[0m'
YELLOW = '\033[33m'
GREEN = '\033[32m'        #setting colours so i can have coloured text which may be easier to read for people with worse eyesight
RED = '\033[31m'          #as this will make it so that there isnt just a large block of black text
PURPLE = '\033[35m'
CYAN = '\033[36m'
BLUE = '\033[34m'

keepgoing = True
while keepgoing == True:           #it makes a loop so it doesnt have to be ran everytime it can just keep looping
    lumens = int(input(PURPLE + "what is the luminous flux of your lightbulb in lumens: " + RESET))   #asks the user for the bulbs lumens
    while lumens == 0:                                           #checks if the user has entered an acceptable number
        print(RED + "this value is not accepted please try again" + RESET)    #if not they have to reinput their lumens
        lumens = int(input(PURPLE + "enter the luminous flux of your lightbulb in lumens: " + RESET))

    print("----------------------------------------------------------------------------------------------------------------")

    power = int(input(CYAN + "enter the power consumption of the light bulb in kWh/1000 h: " + RESET))    #asks the user for the bulbs watts
    while power == 0:                              #checks if the user has entered an acceptable number
        print(RED + "this value is not accepted please try again" + RESET)    #if not they have to reinput their kWh / 1000 h
        power = int(input(CYAN + "enter the power consumption of the light bulb in kWh/1000 h: " + RESET))

    print("----------------------------------------------------------------------------------------------------------------")


    efficiency_ratio = lumens / power        #carries out the efficiency calculation and stores the result

    if efficiency_ratio > 209:
        print(GREEN + "your lightbulb has an efficiency rating of A " + RESET)

    elif efficiency_ratio > 184:
        print(GREEN + "your lightbulb has an efficiency rating of B " + RESET)

    elif efficiency_ratio > 159:
        print(YELLOW + "your lightbulb has an efficiency rating of C " + RESET)

    elif efficiency_ratio > 134:
        print(YELLOW + "your lightbulb has an efficiency rating of D " + RESET)     #this is where the efficiencies are rated
                                                                                    #they are also colour coded
    elif efficiency_ratio > 109:                                                    #red is bad, yellow is moderate, green is good
        print(YELLOW + "your lightbulb has an efficiency rating of E " + RESET)

    elif efficiency_ratio > 84:
        print(RED + "your lightbulb has an efficiency rating of F " + RESET)
        
    else:
        print(RED + "your lightbulb has an efficiency rating of G " + RESET)

    if efficiency_ratio > 184:
        print(GREEN ,"Ratio", efficiency_ratio , RESET)

    elif efficiency_ratio > 109:
        print(YELLOW ,"Ratio", efficiency_ratio , RESET)

    else:
        print(RED ,"Ratio", efficiency_ratio , RESET)
    
    print("----------------------------------------------------------------------------------------------------------------")

    decision = int(input(BLUE + "would you like to do another light bulb 1 = yes , 2 = no: " + RESET))     #allows user to exit the loop or continue
    if decision == 2:
        keepgoing = False

    print("----------------------------------------------------------------------------------------------------------------") 