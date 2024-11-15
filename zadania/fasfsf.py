# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         new_z = ""
#         for counter in range(len(strs)-1):
#             for letter , next_word_letter in zip(strs[counter], strs[counter+1]):
#                 if  letter == next_word_letter:                 
#                     new_z += letter
                    

#         print(new_z)









#         self.strs = strs
#         z = strs[0]
#         counter = 1 
#         new_z = ""
#         new_zz = ""
#         for word in strs[1:-1]:  # одно слово
#             for letter in word:  # буква из слова
#                 if letter in z:  # если буква есть в первом слове
#                     new_z += letter
#         for counter in range(len(strs)-1):
#             for letter in (strs[counter+1]): # если буква есть в общих буквах
#                 if letter in new_z:
#                     new_zz += letter

#         # for word in strs[1:-1]:
#         #      for letter in word:
#         #          if letter in new_z and letter in z:
#         #             print(letter) 
#            self.strs = strs
#         z = strs[0]
#         new_z = ""
#         new_zz = ""
#         for word in strs[1:-1]:  # одно слово
#             for letter in word:  # буква из слова
#                 if letter in z:  # если буква есть в первом слове
#                     new_z += letter
#         for letter in strs[-1]: # если буква есть в общих буквах
#             if letter in new_z:
#                 new_zz += letter

#         return new_zz

#         return new_zz
      
                
# tom = Solution()
# strs1 = ["flower","flow","flight", "flowering"]
# tom.longestCommonPrefix(strs1)
text = ["flower","flow","flight"]
word = text[0]
dlina = len(word)
dlina -= 1
print(word[0:5])