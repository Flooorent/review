"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class ContainsDuplicate:
    @staticmethod
    def with_builtins(nums):
        return not (len(set(nums)) == len(nums))

    @staticmethod
    def with_hashmaps(nums):
        """
        time complexity: O(n)
        space complexity: O(n)
        """
        unique_nums = {}

        for num in nums:
            if num in unique_nums:
                return True

            unique_nums[num] = 1

        return False


input1 = [1, 2, 3, 1]
input2 = [1, 2, 3, 4]
input3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

assert(ContainsDuplicate.with_builtins(input1))
assert(not ContainsDuplicate.with_builtins(input2))
assert(ContainsDuplicate.with_builtins(input3))

assert(ContainsDuplicate.with_hashmaps(input1))
assert(not ContainsDuplicate.with_hashmaps(input2))
assert(ContainsDuplicate.with_hashmaps(input3))
