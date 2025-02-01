# 3151. Special Array I (All Approaches)
- ## Approach 1:- Modulo Comparison
    - ### Intuition
        We need to check if an array satisfies the **"special"** condition, which is that **no two consecutive elements are either both odd or both even**. This means that every consecutive pair of elements in the array should consist of one odd and one even element.
    
        #### Key Observations:
        1. If two consecutive numbers are both odd, or both even, the condition is violated and we immediately return `false`.
        2. If we successfully check the entire array without finding such a violation, we return `true`.

    - ### Approach
        1. **Iterate through the array** starting from the second element (index 1) to compare each element with the previous one.
        2. **Check the parity (odd or even)** of the current element and the previous element:
            - If both elements are odd or both elements are even, return `false` immediately.
        3. If no violation is found after checking all consecutive pairs, return `true`.

        This approach ensures that we only check consecutive pairs and stop early if the condition is violated.

    - ### Code Implementation
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
            class Solution {
            public:
                bool isArraySpecial(vector<int>& nums) {
                    // Iterate through the array starting from the second element (index 1)
                    for(int currentIndex = 1; currentIndex < nums.size(); ++currentIndex) {
                        // Check if both current and previous elements are odd
                        bool both_Elements_Odd = (nums[currentIndex] % 2 == 1) & (nums[currentIndex-1] % 2 == 1);
                        
                        // Check if both current and previous elements are even
                        bool both_Elements_Even = (nums[currentIndex] % 2 == 0) & (nums[currentIndex-1] % 2 == 0);

                        // If both elements are either both even or both odd, return false
                        if(both_Elements_Even || both_Elements_Odd)
                            return false;
                    }

                    // If no consecutive pair of both odd or both even elements is found, return true
                    return true;
                }
            };
            ```

    - ### Time Complexity
        - **Time Complexity:** **$O(n)$**
            - The algorithm iterates through the array once (from the second element to the last), where $n$ is the length of the array. 
            - Each check (modulus operation and comparison) takes constant time $O(1)$, so the total time complexity is linear in terms of the size of the array.

    - ### Space Complexity
        - **Space Complexity:** **$O(1)$**
            - We are using only a few variables (`currentIndex`, `both_Elements_Odd`, `both_Elements_Even`) that require constant space, regardless of the size of the input array. Thus, the space complexity is constant.
<hr>

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
        - **$O(n)$**: We iterate through the array once. For each pair of consecutive elements, the parity check and comparison takes constant time $O(1)$. So, the overall time complexity is linear with respect to the number of elements in the array.

    - ### Space Complexity:
        - **$O(1)$**: We only use a fixed amount of space for the bitwise results and the loop index. No additional space is needed that scales with the size of the input array, so the space complexity is constant.