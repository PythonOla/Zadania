from functools import wraps

def pamiec(func):
    memo = {}
    @wraps(func)
    def wrapper(num):
        if not memo.has_key(num):
            memo[num] = func(num)
        return memo[num]
    return wrapper

@pamiec
def fibonacci(n):
    return n if 0<=n<=2 else fibonacci(n-1) + fibonacci(n-2)

for i in range(100):
    print(i, ": ", fibonacci(i))
        