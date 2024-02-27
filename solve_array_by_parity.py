class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        for num in odd:
            even.append(num)    
        return even
        
# link, https://leetcode.com/problems/sort-array-by-parity