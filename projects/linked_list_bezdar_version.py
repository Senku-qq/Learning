class Linked_List_Node():
    def __init__(self, data, nextNode=None): 
        self.data = data
        self.nextNode = nextNode
    
    # "3" ---> "5" -----> "10"
    #  v  
# Создание не подключенных нод 
node1 = Linked_List_Node("3") #3   | 
node2 = Linked_List_Node("5") #5   | aren't collected 
node3 = Linked_List_Node("10") #10 |
node4 = Linked_List_Node("55")

# подключение нод
node1.nextNode = node2 # node1 ----> node2 , "3" ----> "5"
node2.nextNode = node3 #node 2 ----> node 3 , "5" ---> "10"
node3.nextNode = node4 # node3 ----> node 4 , "10" ---> "55"

current_Node = node1 
#проверка какая нода к какой подключенна и получение данных, но сразу всех элементов сразу
while True:  
    if current_Node.nextNode is None: # если нода не подключенна к следующей, фактически конец ноды, то есть NodeTail
        print(current_Node.data, "--> None")
        print("Error\nNode doesn't have a link to next node")
        break
    print(current_Node.data, "-->", end=' ') # вывод данных из ноды 
    current_Node = current_Node.nextNode # переключение текущей ноды на следующую 
