from random import randint
def shopfunc(nickname, balance, items):
    items = ["Клінок", "Щит", "Дрібничка", "Вудочка"]
    print(f'''
          
        Вітаємо в магазині, {nickname}!
      Твій баланс: {balance}
''')
    # global pricerand
    # pricerand = random.randint(10,50)
    # global pricerand1
    # pricerand1 = random.randint(10,50)
    # global pricerand2
    # pricerand2 = random.randint(10,50)
    # global pricerand3
    # pricerand3 = random.randint(10,50)
    # towars = {'Клінок': pricerand,'Щит': pricerand1,'Дрібничка': pricerand2, 'Вудочка': pricerand3}
    dict = {}
    global dict 
    
    for i in items:
        pricerand = randint(10,50)
        dict[i] = pricerand
    
    for key, val in dict.items():
        print(f"Товар {key} коштує {val}\n")
        print(dict.items)
(shopfunc("maks", 1, 1))