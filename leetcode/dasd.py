class Solution(object):
    def isValid(self,s):
        print("1")
        stack = []
        return_ = True
        last = ""
        if len(s) == 0 or len(s) == 1:
            return False
        for i in s:
            if i in "([{":
                stack.append(i)
            if not stack:
                return False
            elif i in ")]}" and len(stack) != 0:
                last = stack.pop()
                print(last)
                print(stack)
                if last == "(" and i == ")":
                    continue
                if last == "[" and i == "]":
                    continue
                if last == "{" and i == "}":
                    continue
                return_ = False
                break
        if len(stack) == 0 and return_ == True:
            return True
        else:
            return False
tom = Solution()
tom.isValid("()[]{}")