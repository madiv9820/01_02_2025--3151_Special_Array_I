from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Get the length of the input list 'nums'
        n = len(nums)
        
        # Iterate through the list starting from the second element
        for currentIndex in range(1, n):
            # Check if both current element and previous element are odd
            both_Elements_Odd = (nums[currentIndex] % 2 == 1) & (nums[currentIndex-1] % 2 == 1)
            
            # Check if both current element and previous element are even
            both_Elements_Even = (nums[currentIndex] % 2 == 0) & (nums[currentIndex-1] % 2 == 0)

            # If both elements are either both even or both odd, return False
            if both_Elements_Even or both_Elements_Odd:
                return False
        
        # If no consecutive odd or even pairs were found, return True
        return True