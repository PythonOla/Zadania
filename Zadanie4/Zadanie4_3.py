# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. 
# Znaleźć listę zawierającą sumy liczb z tych sekwencji. 
# Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18]. 


def to_sums(list_of_collections):
    result = []
    for elements in list_of_collections:
        result.append(sum(elements))
    return result

#print(to_sums([(1,2,3),[4,5,6], (100, -100, 100)]))

