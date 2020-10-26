ruler_length = int(input("Podaj długość miarki: "))
seg_len = 4

ruler_string = "|"

for i in range(0, ruler_length):
    ruler_string += (seg_len * '.' + "|")

ruler_string += '\n0'

for i in range(1, ruler_length + 1):
    number_length = len(str(i))
    spaces_count = seg_len + 1 - number_length
    ruler_string += spaces_count * " "
    ruler_string += str(i)

print(ruler_string)