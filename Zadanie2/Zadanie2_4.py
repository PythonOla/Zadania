def get_all_points_not_equal_to_n(n, x, y, z):
    return [
            [i,j,k]
            for i in range(0, x + 1)
            for j in range(0, y + 1)
            for k in range(0, z + 1)
            if i + j + k != n
            ]

x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
z = int(input("Podaj z: "))
n = int(input("Podaj n: "))

print(get_all_points_not_equal_to_n(n,x,y,z))
