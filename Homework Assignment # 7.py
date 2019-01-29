Song = {'Composer':'A R Rehman','Year':'2009','Duration_in_Mins':'5.53'}
##
##for key,value in Song.items():
##    print(key+': '+str(value))

GuessSong = False    
def GuessSongAttrb():
    print("Guess the Song")
    Key = input('enter an Attribute of the Song:')
    Value = input('enter the value of the Attribute '+Key+': ')
    if Key in Song.keys() and Value in Song.values():
         print(" you Guessed it Right")
         print(Song.items())
         GuessSong = True
        
    else:
        print(" Wrong Guess Please try again")
        GuessSong = False
    return GuessSong


GuessSongAttrb()
