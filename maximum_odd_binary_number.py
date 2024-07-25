class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        if ones == 1: 
            return "0"*(len(s)-1) + '1' 
        return '1'*(ones-1) + (len(s)-ones)*'0' + '1'

solution = Solution()
print(solution.maximumOddBinaryNumber('0011'))