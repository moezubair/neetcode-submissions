class Solution:
    # Input: a string of characters with brackets
    # Output: true if all are valid parenthesis 
    # Constraints? Empty string is it valid? yes


    def isValid(self, s: str) -> bool:
        brackets = {')': '(','}': '{', ']': '['}
        #Bruce Force
        stack = []

        for c in s:
            if c in brackets: #it means it is a closing bracket
                top = stack.pop() if stack else '#'
                if top != brackets[c]:
                    return False
            else :  # open bracket
                stack.append(c)
        return len(stack)==0