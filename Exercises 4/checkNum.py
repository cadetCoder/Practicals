def checkNum():
    num = int(input("Please enter a number between 1 and 20: "))
    
    if num < 1:
        message = ("Too low")
    elif num > 20:
        message = ("Too high")
    else:
        message = ("In range")
    print(message)

checkNum()
