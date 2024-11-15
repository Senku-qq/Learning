n = 8  #length
name = "Maksim"

print("Here is a cake for you!!!\n")
for i in range(n):
    if i == 2: print("=  Happy      =", end="")
    if i == 4: print("= Birthday    =", end="")
    if i == 7: print(f"=  {name}     =")
    for j in range(n):
        if i == 0:
            print("i", end=" ")
        elif i % 2 == 0:
            pass
        else:
            print("=", end=" ")
    print()