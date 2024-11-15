from collections import deque
#  class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
#     def __str__(self):
#         return f"{self.val},{self.left},{self.right}"

# class Tree_builder:
#     def __init__(self, root=None):
#         self.root = root
    
#     def insert(self, val, node=None):
#         if self.root is None:
#             self.root = Tree(val)
#             print(self.root)
#             return
        
#         if node == None:
#             node = self.root
            
#         if (val <= node.val):
#             if node.left == None: node.left = Tree(val)
#             else: self.insert(val, node.left)
        
#         elif (val >= node.val):
#             if node.right == None: node.right = Tree(val)
#             else: self.insert(val, node.right)

#     def display_Tree(self, node=None):
        
#         exit = False
        
#         if node == None:
#             node = self.root
        
#         if node.right is None: exit = True
#         else:
#             print(f"right = {node.right}")
#             self.display_Tree(node.right)
        
#         if node.left is None: exit = True
#         else:
#             print(f"left = {node.left}")
#             self.display_Tree(node.left)
        
#         if exit == True:
#             return
# Tom = Tree_builder()
# Tom.insert(5)
# Tom.insert(10)
# Tom.insert(4)
# Tom.insert(6)
# Tom.insert(3)

# Tom.display_Tree()
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, val):
    if root == None:
        return Tree(val)
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.left is None:
            curr.left = Tree(val)
            break
        else:
            queue.append(curr.left)
        if curr.right is None:
            curr.right = Tree(val)
            break
        else:
            queue.append(curr.right)
    return root
def searching(root,val):
    if root is None:
        return False
    if root.data == val:
        return True
    left_res = searching(root.left, val)
    right_res = searching(root.right, val)
    return left_res or right_res
def deleting(root, val):
    if root is None: return None
    
    queue = deque([root])
    target = None

    while queue:
        curr = queue.popleft()
        if curr.data == val:
            target = curr
            break
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    if target is None: return root
       
    last_node = None
    last_parent = None
    queue = deque([(root,None)])
    while queue:
        curr, parrent = queue.popleft()
        last_node = curr
        last_parent = parrent
        if curr.left:
            queue.append((curr.left, curr))
        if curr.right:
            queue.append((curr.right, curr))
    target.data = last_node.data
    if last_parent:
        if last_parent.left == last_node:
            last_parent.left = None
        else:
            last_parent.right = None
    else:
        return None
    return root
def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data , end=' ')
    in_order_dfs(node.right)

if __name__ == "__main__":
    root = Tree(5)
    root.left = Tree(4)
    root.right = Tree(7)
    root.left.left = Tree(3)
    val = 16
    searching
    if searching(root,val):
        print(f"^^^{val} is found in Tree^^^")
    else: 
        print(f"{val} is not found in Tree")
    print("In order BFS: ", end=' ')
    in_order_dfs(root)
    print()
    print("In order BFS after insert: ", end=' ')
    insert(root,100)
    in_order_dfs(root)
    val2 = 5
    print()
    if deleting(root, val2):
        print(f"{val2} has been deleted from Tree ")
        in_order_dfs(root)
    else:
        print(f"{val2} is not deleted from Tree")
        in_order_dfs(root)