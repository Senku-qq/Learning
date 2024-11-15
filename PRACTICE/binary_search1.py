def binary_search(list, item):  #item = то число которое мы ищем
    list.sort()
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid] 
        if guess == item: # если нашли загаданное число возвращаем мид  
            return mid
        if guess > item: # если число больше чем то что мы ищем то 
            high = mid - 1
        if guess < item:
            low = mid + 1
    return None
        
    #item = то число которое мы ищем 
  


dict = [6,1,2,7,8,10 , 15 , 20 , 40 , 50 ,100 , 1000]
print(binary_search(dict, 1000))
