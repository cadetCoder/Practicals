def isLeapYear ():
    y = input("What is the year? ")
    y = int(y)
    
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        print ("True")
##        result = False
    else:
        print("False")
##        result = False
##    return result

isLeapYear()
