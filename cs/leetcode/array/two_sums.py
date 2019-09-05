"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class TwoSum:
    @staticmethod
    def brute_force(nums, target):
        """
        time complexity: O(n^2)
        space complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    @staticmethod
    def two_pass_hash_table(nums, target):
        """
        time complexity: O(n), on passe deux fois sur les données
        space complexity: O(n)
        """
        nums_to_indices = {num: index for index, num in enumerate(nums)}

        for index, num in enumerate(nums):
            if target - num in nums_to_indices and target - num != num:
                return [index, nums_to_indices[target - num]]

    @staticmethod
    def one_pass_hash_table(nums, target):
        """
        time complexity: O(n), on passe au maximum une fois sur les données
        space complexity: O(n)
        """
        nums_to_indices = {}

        for index, num in enumerate(nums):
            if target - num in nums_to_indices:
                return [nums_to_indices[target - num], index]

            nums_to_indices[num] = index




nums = [2, 7, 11, 15]

assert(TwoSum.brute_force(nums, 9) == [0, 1])
assert(TwoSum.brute_force(nums, 18) == [1, 2])
assert(TwoSum.brute_force(nums, 26) == [2, 3])
assert(TwoSum.brute_force(nums, 17) == [0, 3])

assert(TwoSum.two_pass_hash_table(nums, 9) == [0, 1])
assert(TwoSum.two_pass_hash_table(nums, 18) == [1, 2])
assert(TwoSum.two_pass_hash_table(nums, 26) == [2, 3])
assert(TwoSum.two_pass_hash_table(nums, 17) == [0, 3])

assert(TwoSum.one_pass_hash_table(nums, 9) == [0, 1])
assert(TwoSum.one_pass_hash_table(nums, 18) == [1, 2])
assert(TwoSum.one_pass_hash_table(nums, 26) == [2, 3])
assert(TwoSum.one_pass_hash_table(nums, 17) == [0, 3])
