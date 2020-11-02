def wyrazy_i_litery(zdanie):
    
    slowa = []
    aktualne_slowo = ""
    litery = dict()

    for znak in zdanie.lower():
        if (znak.isalnum()):
            
            aktualne_slowo += znak

            if (znak in litery):
                litery[znak] += 1
            else:
                litery[znak] = 1

        elif (len(aktualne_slowo) > 0):
            slowa.append(aktualne_slowo)
            aktualne_slowo = ""
        else:
            pass
        
    if (len(aktualne_slowo) > 0):
        slowa.append(aktualne_slowo)
        
    return (len(slowa), litery)

string_wejsciowy = input("Podaj string wejściowy: ")
(ile_wyrazow, statystyka_liter) = wyrazy_i_litery(string_wejsciowy)
print("Liczba wyrazów w podanym łańcuchu:", ile_wyrazow)
print("Statystyka liter:")
for litera in statystyka_liter:
    print(litera, ":", statystyka_liter[litera])