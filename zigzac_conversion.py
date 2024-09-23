class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        indx, d = 0,1
        for char in s:
            rows[indx].append(char)
            if indx == 0:
                d = 1
            elif indx == numRows - 1:
                d = -1
            indx += d
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)
    
solution = Solution()
result = solution.convert("abcdefgh", 3)
print(result)