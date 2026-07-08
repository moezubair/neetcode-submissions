class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = ['+', '-', '*', '/']
        vals = []
        ans = 0
        visited = False
        for t in tokens:
            if t in ops:
                visited = True
                if t == '+':
                    r,l = vals.pop(), vals.pop()
                    ans = l + r                     
                    vals.append(int(ans))
                elif t == '*':
                    r,l = vals.pop(), vals.pop()
                    ans = l * r                                         
                    vals.append(int(ans))
                elif t == '-':
                    r,l = vals.pop(), vals.pop()
                    ans = l - r   
                    vals.append(int(ans))
                elif t == '/':
                    r,l = vals.pop(), vals.pop()
                    if l ==0 or r == 0:
                        ans = 0
                    else:
                        ans = int (l / r )
                    vals.append(int(ans))                  
            else:
                vals.append(int(t))

        return ans if visited else int(tokens[0])
