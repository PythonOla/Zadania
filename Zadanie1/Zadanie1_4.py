rows = int(input("Ile rzędów?: "))
cols = int(input("Ile kolumn?: "))

figure = "+"

for i in range(0, cols):
    figure += '---+'

for i in range(0, rows):
    figure += '\n|'
    for j in range(0, cols):
        figure += '   |'
    figure += '\n+'
    for i in range(0, cols):
        figure += '---+'


print(figure)