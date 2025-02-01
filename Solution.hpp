#include <vector>
using namespace std;

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