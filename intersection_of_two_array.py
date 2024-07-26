from typing_extensions import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
    
solution = Solution()
print(solution.intersection([4,5,3,2,5,5,],[2,2,2,5]))