# nums2 = [] # 0, 1 ,
#         nums3 = []
#         for i in (nums):# 0 1 1 
#             if i in nums2: 
#                 nums3.append(i)  # nums 0,1,2,2,3,3,4
#             else:
#                 nums2.append(i)
#         for i in nums3:
#             if i in nums:
#                 nums.remove(i)
#         k = len(nums)
#         print(k, nums)

# nums = [0,0,1,1,1,2,2,3,3,4] #0,1,1,1,2,2,3,3,4
# nums2 = [0] # 0, 1 ,
# for i in nums:# 0 1 1 
#     if i in nums2: 
#         nums.remove(i)  # nums 0,1,2,2,3,3,4
#     else:
#          nums2.append(i)
# k = len(nums)
# print(k, nums)
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# count = i = 0
# while i < len(nums):
#     if nums[i] == val:
#         nums.pop(i)
#         count += 1
#         continue
#     i += 1
# # print(nums)
# haystack2 = "butsadbut"
# needle1 = "sda"
# class Solution(object):
#     def strStr(self, haystack, needle):
#         if needle in haystack:
#             print(haystack.find(needle))
# #         print("-1") 
# # tom = Solution()
# # class Solution(object):
#    # binary search
#         high = len(nums)-1 #3
#         low = 0
#         while low <= high:
#             mid = (high + low) // 2 #1
#             quess = nums[mid]   
#             if quess == target:
#                 return mid
#             if quess < target: 
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         #finding where index would be if it not found in nums
#         find_index= 0  
#         if target > nums[-1]:
#             length = len(nums)-1
#             return length + 1  
#         if target not in nums:   
#             if target > 0:
#                 for i in nums[:]:
#                     find_index += 1
#                     if i < target:
#                         i += 1
#                         if i == target:
#                             return find_index 
#                     if i == target:
#                         return find_index 
#                     if i > target: 
#                         i -= 1 
#                         find_index -= 1 
#                         if i == target:
#                             return find_index
#             if target <= 0:
#                 for i in nums[:]: 
#                     find_index += 1
#                     if i < target:
#                         i += 1
#                         if i == target:
#                             return find_index 
#                     if i == target:
#                         return find_index
#                     if i > target: 
#                         i -= 1 
#                         find_index -= 1 
#                         if i == target:
#                             return find_index
            
#             if target == 0 and target < nums[0]:
#                 return find_index
#             if target < nums[0]:
#                 return 0
 
# # s = "   fly me   to   the moon  "
# # print(s.split())
# digits = [1,2,3]
# # solve = "".join(map(str,digits))
# # print(solve)
# int()
# n = 5 
# one , two = 1,1
 # for i in range(n - 1):
 #       temp = one
 #     one = one + two 
 #     two = temp
 #     print(one)
 # print(one)
# s = 0
# u = float
# x = 2.45

# i = 0 
# k = 0 
# f = 0
# for i in range(1, 8, 1):
#     f = 1
#     for k in range(1 , 2*i, 1): 
#         f *= k
#     u = 2 * pow(x,2*i-1)/(3*f)
#     s += u
# # print(f"Сумма равна : {s}")
# def countdown(i): 

#     print(i)
#     countdown(i-1)


# countdown(5)

# class BuildNode:
#     #class for builing nodes
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
#     #method to print nodes variables
#     def __str__(self):
#         return f"{self.val, self.left, self.right}"

# class Tree:
#     #class of binary tree
#     def __init__(self, root=None):
#         self.root = root

#     def insert(self, val, node=None):

#         #create root and exit
#         if self.root is None:
#             self.root = BuildNode(val)
#             print(self.root)
#             return
        
#         # if no current node -> current node is root
#         if node is None:
#             node = self.root


#         if (val < node.val):
#             if node.left is None: node.left =  BuildNode(val)
#             else:   self.insert(val, node.left)

#         elif (val >= node.val):
#             if node.right is None: node.right =  BuildNode(val)
#             else:   self.insert(val, node = node.right)

#     def display_tree(self, node=None):
        
#         exit = False

#         if node is None:
#             node = self.root
        
#         if node.right is None: exit = True
#         else: 
#             print(node.right)
#             self.display_tree(node.right)

#         if node.left is None: exit = True
#         else:
#             print(node.left)
#             self.display_tree(node.left)
        
#         if exit is True: return


# obj = Tree()
# obj.insert(5)
# obj.insert(10)
# obj.insert(4)

# obj.display_tree()


        