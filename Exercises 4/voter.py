def voter():
    age = int(input("How old are you in whole years?: "))
    
    if age >= 18:
        message = "You are old enough to vote"
    else:
        message = "You are NOT old enough to vote"
    print(message)
    return message

voter()
