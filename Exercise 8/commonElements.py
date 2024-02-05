def commonElements(xs,ys):
    newList = []
    for i in xs:
        if i in ys and i not in newList:
            newList.append(i)
    return newList
