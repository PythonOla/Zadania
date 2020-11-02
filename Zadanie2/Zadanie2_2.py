def rok_przestepny():
    rok = 0
    while (rok > 100000 or rok < 1900):
        rok = int(input("Podaj rok z przedziału 1900 - 100 000: "))
    
    if (rok % 4 != 0):
        return False
    elif (rok % 100 != 0):
        return True
    elif (rok % 400 != 0):
        return False
    else:
        return True

print(rok_przestepny())