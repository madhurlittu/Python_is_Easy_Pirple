myUniqueList = []
myRejectList = []
AddValue = False
def addRejectValue(Var):
    #adding Rejected(Non unique or repeated values) Values to a separate List
    return myRejectList.append(Var)


def addItem(Var):
    if Var in myUniqueList:
        addRejectValue(Var)
        AddValue = False
        print("myRejectList:\t",myRejectList)
        return AddValue
    else:
        myUniqueList.append(Var)
        AddValue = True
        print("myUniqueList:\t",myUniqueList)
        return AddValue





addItem(2)
addItem(3.6789)
addItem("Lists")
addItem(2)
addItem(3.6789)
addItem("HomeworkAssignment #4")

