from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Get the length of the input list 'nums'
        n = len(nums)

        # Iterate through the list, checking consecutive elements
        for currentIndex in range(n-1):
            # Perform bitwise AND with 1 to check if the current element is odd or even
            # This isolates the least significant bit (LSB), which indicates odd (1) or even (0)
            currentElement_Bitwise = nums[currentIndex] & 1 

            # Similarly, perform bitwise AND with 1 to check if the next element is odd or even
            nextElement_Bitwise = nums[currentIndex+1] & 1

            # If both current and next elements have the same parity (both odd or both even),
            # the XOR result will be 0 (since both bits are identical).
            # In this case, return False as the array doesn't satisfy the special condition.
            if currentElement_Bitwise ^ nextElement_Bitwise == 0:
                return False
        
        # If no consecutive pair of both odd or both even elements was found, return True
        return True