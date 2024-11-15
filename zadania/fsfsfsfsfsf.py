class Solution(object):
    def longestCommonPrefix(self, strs):
        self.strs = strs
        z = strs[0]
        counter = 1 
        new_z = ""
        new_zz = ""
        for word in strs[1:-1]:  # одно слово
            for letter in word:  # буква из слова
                if letter in z:  # если буква есть в первом слове
                    new_z += letter
        for counter in range(len(strs)-1):
            for letter in (strs[counter+1]): # если буква есть в общих буквах
                if letter in new_z:
                    new_zz += letter
        return new_zz
tom = Solution()
tom.longestCommonPrefix()