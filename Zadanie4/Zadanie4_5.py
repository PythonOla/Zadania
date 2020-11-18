#Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. 
#Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanie(L, left, right):
    if left >= right:
        return L
    else:
        variable = L[right]
        L[right] = L[left]
        L[left] = variable
        return odwracanie(L, left + 1, right - 1)

#print(odwracanie([1,2,3,4,5,6,7,8,9], 3, 7))