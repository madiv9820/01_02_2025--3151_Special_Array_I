from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ([1], True), 2: ([2,1,4], True), 3: ([4,3,1,6], False)}
        self.__sol = Solution()
        return super().setUp()

    @timeout(0.5)
    def test_case_1(self):
        nums, output = self.__testcases[1]
        result = self.__sol.isArraySpecial(nums = nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(output, result)

    @timeout(0.5)
    def test_case_2(self):
        nums, output = self.__testcases[2]
        result = self.__sol.isArraySpecial(nums = nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(output, result)

    @timeout(0.5)
    def test_case_3(self):
        nums, output = self.__testcases[3]
        result = self.__sol.isArraySpecial(nums = nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(output, result)

if __name__ == '__main__': unittest.main()