def noDuplicates(mylist):
    newList = []
    for element in mylist:
        if element not in newList:
##            newList = newList + [element]
            newList.append(element)
    return newList
