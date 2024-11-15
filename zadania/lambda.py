def dekorator(input_func):
    def output_func(args):
        print(f"Начальный список: {args}")
        input_func(args)
    return output_func
@dekorator
def chetnoe(a):
    new = []
    new2 = []
    for i in (a):
        if i % 2 == 0:
            new.append(i)
        else:
            new2.append(i)
    print(f"Четные числа: {new}")
    print(f"Нечетные числа: {new2}")

chetnoe([1,2,3,4,5,6,7,8,9,10])
