class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool: 
        visit = set()
        fword = []

        def backtrack(i, j, index):
            if index == len(word):
                return True
            if i >= len(board) or j >= len(board[i]) or i < 0 or j < 0 or (i, j) in visit:
                return False
            
            if board[i][j] == word[index]:
                visit.add((i, j))
                fword.append(board[i][j])
                index += 1
            else:
                return False

            res = (
                backtrack(i+1, j, index) or
                backtrack(i-1, j, index) or
                backtrack(i, j+1, index) or
                backtrack(i, j-1, index)
            )
            fword.pop()
            visit.remove((i, j))
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i, j, 0):
                    return True
        return False