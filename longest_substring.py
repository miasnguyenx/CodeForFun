class Solution:
    def lengthOfLongestSubstringCharmap(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        return maxLength
    def lengthOfLongestSubstringCharset(self, s:str) -> int:
        charSet = set()
        maxLength = 0
        left = 0
        n = len(s)
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return maxLength
solution = Solution()
solution.lengthOfLongestSubstringCharmap("tmtmzuxt")
solution.lengthOfLongestSubstringCharset("tmtmzuxt")
