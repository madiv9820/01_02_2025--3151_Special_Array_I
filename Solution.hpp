#include <vector>
using namespace std;

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