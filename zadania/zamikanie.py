def zamik(n):
    return lambda number: n * number 
multi = zamik(5)
print(multi(5))