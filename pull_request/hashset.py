class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
            self.head = None

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        
        current = self.head
        while current.next:
            current = current.next
        else: current.next = Node(val)

    def display(self):
        if self.head:
            current = self.head
            while current:
                print(f"{current.val}->", end='')
                current = current.next
            print()    

    def remove(self, val):
        if self.head:
            # if head needs to be removed - point on new head
            if self.head.val == val:
                self.head = self.head.next
                return
            
            current = self.head
            # while node isn`t found and while not the end of a list
            while current and current.next.val != val:
                current = current.next
            # if node found -> remove
            if current.next:
                current.next = current.next.next

    def lenght(self):
        if self.root:
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next
            return count

    def reverse(self):
        if self.head:

            current = self.head
            prev = None

            while current:
                # temporary store next node to iterate
                next_node = current.next
                # reverse next
                current.next = prev
                prev = current
                # step
                current = next_node
            # point on the new head 
            self.head = prev

    def contains(self, val):
        if self.head:
            current = self.head
            while current:
                if current.val == val:
                    return True

    def clear(self):
        self.head = None


# end of linked list

# start of hashset
class HashSet:
    def __init__(self):
        pass