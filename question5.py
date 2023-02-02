def str(s):
    lower=0
    upper=0
    for i in s:
        if(i.islower()):
            lower+=1
        elif(i.isupper()):
            upper+=1
        else:
            pass
    print("No. of Upper-case characters:",upper)
    print("No. of Lower-case characters:",lower)
str('The quick Brow Fox')
