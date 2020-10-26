stars = int(input("Ile gwiazdek? "))
while stars % 2 == 0:
    print("Podaj nieparzystą")
    stars = int(input("Ile gwiazdek? "))

currently_stars = stars
spaces_at_each_side = 0

while currently_stars > 0 :
    print(spaces_at_each_side * " " + currently_stars * "*" + spaces_at_each_side * " ")
    spaces_at_each_side += 1
    currently_stars -= 2


