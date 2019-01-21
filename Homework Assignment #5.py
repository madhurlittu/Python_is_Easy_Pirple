primeFlg = False
def FizzBuzz():
    print("Printing No's from 1 to 100")
    for i in range(1,101):
        PrimeNoCheck(i)
        if i%3 == 0:
            if i%5 ==0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i%5 == 0:
            if i%3 == 0:
              continue
            else:  
              print("Buzz")
        else:
            print(i)

    return True

def PrimeNoCheck(num):
    if num > 1:
   # check for factors
     for i in range(2,num):
       if (num % i) == 0:
##           print(num,"is not a prime number")
##           print(i,"times",num//i,"is",num)
           break
     else:
       primeFlg = True  
       print("Prime,",end='')
         
FizzBuzz()


