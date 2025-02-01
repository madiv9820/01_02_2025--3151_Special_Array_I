- ## Approach 02:- Bitwise Operations
    - ### Intuition:
        The goal is to determine whether the array is "special". An array is considered special if **no two consecutive elements** have the same parity (both odd or both even). We will examine each consecutive pair of elements in the array, and if any pair has the same parity, the array is not special. Otherwise, the array is special.

        To check the parity of an integer, we can use bitwise operations. Specifically, the least significant bit (LSB) of a number will tell us if it's odd or even:
        - Odd numbers have a LSB of `1`.
        - Even numbers have a LSB of `0`.

        By comparing the parity of consecutive elements using bitwise operations, we can determine whether the array satisfies the special condition.

    - ### Approach:
        1. **Iterate through the array**: Loop through the array from the first element to the second-last element.
        2. **Check parity of consecutive elements**: For each pair of consecutive elements, check if both are either both odd or both even.
            - We can do this efficiently by using bitwise operations to isolate the least significant bit of each element.
            - If two consecutive elements have the same parity (both odd or both even), return `false` immediately.
        3. **Return true**: If no consecutive pair with the same parity is found, return `true` at the end, indicating that the array is special.

    - ### Code Implementation:
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
            class Solution {
            public:
                bool isArraySpecial(vector<int>& nums) {
                    // Iterate through the vector 'nums', stopping at the second last element
                    // The loop runs from index 0 to nums.size() - 2, comparing each pair of consecutive elements
                    for(int currentIndex = 0; currentIndex < nums.size() - 1; ++currentIndex) {
                        
                        // Use bitwise AND operation to isolate the least significant bit (LSB) of the current element
                        // This tells us if the current element is odd (1) or even (0)
                        int currentElement_Bitwise = nums[currentIndex] & 1;
                        
                        // Similarly, use bitwise AND operation to isolate the LSB of the next element
                        // This tells us if the next element is odd (1) or even (0)
                        int nextElement_Bitwise = nums[currentIndex + 1] & 1;

                        // Check if both the current and next elements have the same parity
                        // XOR will be 0 if both bits are the same (both odd or both even)
                        // If XOR result is 0, return false since two consecutive elements are both odd or both even
                        if((currentElement_Bitwise ^ nextElement_Bitwise) == 0)
                            return false;
                    }

                    // If no violation (both elements are either both odd or both even) is found, return true
                    return true;
                }
            };
            ```

    - ### Time Complexity:
        - **$O(n)$**: We iterate through the array once. For each pair of consecutive elements, the parity check and comparison takes constant time ($O(1)$). So, the overall time complexity is linear with respect to the number of elements in the array.

    - ### Space Complexity:
        - **$O(1)$**: We only use a fixed amount of space for the bitwise results and the loop index. No additional space is needed that scales with the size of the input array, so the space complexity is constant.