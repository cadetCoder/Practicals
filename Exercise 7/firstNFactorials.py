def firstNFactorials (n) :
    factorials = []
    for i in range (1,n+1) :
        factorials.append(factorials(i))
    return factorials
