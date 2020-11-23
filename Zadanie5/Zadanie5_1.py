class Bug:
    licznik = 0
    def __init__(self):
        self.id = Bug.licznik + 1
        Bug.licznik = Bug.licznik + 1
    
    def __del__(self):
        Bug.licznik = Bug.licznik - 1

    def __str__(self):
        return "Liczba bugów: " + str(Bug.licznik) +  ", Ten Bug ma identyfikator: " + str(self.id)

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])




