class race:
    def set_name(self):
        self.name = input("Введите имя которое хотите написать")
    def __init__(self,name,race):
        self.__name = name
        self.__race = race
        question = input("Вы хотите изменить имя питомца? Yes/No: ")
        if "Yes" in question:
            self.set_name()
        else:
            print("Повезло питомцу:)")
    def get_name(self):
        return self.__name
   
dog = race("Murzik","sfinks")
        
class childs(race):   
    def mew(self):
        question = input("Хочешь мяукнуть?)): Yes/No: ")
        if "Yes" in question:
            print("Mewwwww ^_^")
        else:
            print("я твою мамку тарабанил")
        
child = childs("small", "penis")
child.mew()      
        
        
         