Grid1 = int(input("please enter no. of rows:"))
Grid2 = int(input("please enter no. of columns:"))
TicTac = False

def TicTacBox(row,col):
    
    if row <=41 and col <=100:
        TicTac = True
        for i in range(1,row+1):
            if i%2==1:
                for j in range(1,col+1):
                    if j%2==1:
                       if j != col:
                        print(" ",end='')
                       else:
                        print(' ')
                    else:
                       if j != col:
                        print("|",end ='')
                       else:
                        print("|")
            else:
                print("-"*(col+2))
    else:
        TicTac = False
        print("Box inputs out of bounds, Please enter row no. less than 42 and column no. less than 101")
    
    return TicTac        
TicTacBox(Grid1,Grid2)
##TicTacBox(5,6)


