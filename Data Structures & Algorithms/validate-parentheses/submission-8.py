class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        directory = {')' : '(', ']' : '[', '}' : '{'}
        for char in s:
            if char in directory:
                if stack and stack[-1] == directory[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False

            
        
        