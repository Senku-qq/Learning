class Linked_list_Node():  #создаем объекты для ноды
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode
class Linked_List(): # создаем голову нашей ноды то есть начало 
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, data): # создаем саму ноду 
        node = Linked_list_Node(data)
        if self.head is None:
            self.head = node
            return 
        current_Node = self.head
        # чтобы вставить новый узел, мы должны найти конец списка
        # мы начинаем с головы и идем до тех пор, пока nextNode не будет None
        # когда мы его найдем, мы вставляем новый узел
        while True: 
            if current_Node.nextNode is None:  # если current_Node.nextNode - None, то это конец списка
                current_Node.nextNode = node   # вставляем новый узел
                break
            current_Node = current_Node.nextNode  # иначе, мы продолжаем идти по списку, пока не найдем None
    def removeNode(self):
        pass
    def printLinkedList(self):
        current_Node = self.head
        while current_Node is not None:
            print(current_Node.data, "-->", end=' ')
            current_Node = current_Node.nextNode
        print("None")

ll = Linked_List()
ll.printLinkedList()
ll.insert("5")
ll.printLinkedList()
ll.insert("10")
ll.printLinkedList()
ll.insert("55")
ll.printLinkedList()

# (ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}})
# head указывает на все остальное