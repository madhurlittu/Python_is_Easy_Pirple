EqualVar = False

def checkEquality(a,b,c):
    d,e,f = int(a),int(b),int(c)
    if (d == e) or (d == f) or (e == f):
        EqualVar = True
        print("Two or more numbers are equal")
        print(EqualVar)
    else:
        EqualVar = False
        print("None of them are equal")
        print(EqualVar)


checkEquality(1,2,3)
