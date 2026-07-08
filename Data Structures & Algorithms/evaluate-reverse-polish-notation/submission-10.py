class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        vals = []
        for t in tokens:
            if t == '+':
                vals.append(vals.pop() + vals.pop() )
            elif t == '*':
                vals.append(vals.pop() * vals.pop() )

            elif t == '-':
                r,l = vals.pop(), vals.pop()
                vals.append(l - r)
            elif t == '/':
                r,l = vals.pop(), vals.pop()
                if l == 0 or r == 0:
                    ans = 0
                else:
                    ans = int (l / r )
                vals.append(int(ans))                  
            else:
                vals.append(int(t))
        return vals[0]
