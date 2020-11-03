def fun(N):

    as_binary_string = str(bin(N))
    as_binary_list = as_binary_string.split("1")
    
    as_binary_list.pop(0); #usunac "0b"
    if (as_binary_string[-1] == "0"):
        as_binary_list.pop() #usunac ostatni element jesli liczba konczy sie sekwencja zer

    if (len(as_binary_list) == 0):
        return 0
    else:
        return max(map(len, as_binary_list))

N = int(input("Podaj liczbe: "))
print(fun(N))

