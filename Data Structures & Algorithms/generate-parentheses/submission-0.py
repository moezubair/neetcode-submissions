class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # output: valid parenthesis string of size 2*n 
        output = []
        stack = []

        # Generate all valid posibilities:

        def backtrack(open_brackets, closed_brackets):
            if len(stack) == 2*n:
                output.append("".join(stack))
                return
            
            if open_brackets < n:
                stack.append('(')
                backtrack(open_brackets+1, closed_brackets)
                stack.pop()
            if closed_brackets < open_brackets:
                stack.append(')')
                backtrack(open_brackets, closed_brackets+1)
                stack.pop()

        backtrack(0, 0)
        return output