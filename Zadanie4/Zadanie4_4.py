
#Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). 
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()]
DIGITS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman2int(roman_literal):
    
    last = None 
    current = 9999 # anything more than max digit will do 
    total = 0

    for character in roman_literal:
        last = current
        current = DIGITS[character]
        if last < current:
            total -= 2 * last
        total += current

    return total       

#print(roman2int('MCMXCVII'))