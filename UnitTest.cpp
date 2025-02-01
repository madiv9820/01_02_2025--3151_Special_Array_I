#include <iostream>
#include "Solution.hpp"

class UnitTest {
private:
    Solution sol;
    vector<pair<vector<int>, bool>> testcases;
public:
    UnitTest() { testcases = {{{1}, true}, {{2,1,4}, true}, {{4,3,1,6}, false}}; }
    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            vector<int>& nums = testcases[i].first;
            bool output = testcases[i].second;

            bool result = sol.isArraySpecial(nums);
            cout << "TestCase " << i+1 << ": " << ((result == output) ? "passed":"failed") << endl; 
        }
    }
};

int main() {
    UnitTest test;
    test.test();
}