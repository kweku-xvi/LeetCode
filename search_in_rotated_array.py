class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1

# link to question, https://leetcode.com/problems/search-in-rotated-sorted-array/