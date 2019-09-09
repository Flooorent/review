"""
medium

Given an array nums of n integers where n > 1, return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as
extra space for the purpose of space complexity analysis.)
"""


def solution(nums):
    left_products = [1]
    right_products = [1]

    for i in range(1, len(nums)):
        left_products.append(left_products[-1] * nums[i - 1])
        right_products.append(right_products[-1] * nums[len(nums) - i])

    results = [left_products[i] * right_products[len(nums) - 1 - i] for i in range(len(nums))]
    return results


input = [1, 2, 3, 4]
output = [24, 12, 8, 6]

assert(solution(input) == output)
print(solution(input))
