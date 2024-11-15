def sortirowka(a):
    new = []
    while a:
        min_number = a[0]
        for i in a:
            if i < min_number:
                min_number = i
        a.remove(min_number)
        new.append(min_number)
    print(f"Отсортированный список : {new}")
sortirowka([4,5,20,10,50]) 