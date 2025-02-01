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