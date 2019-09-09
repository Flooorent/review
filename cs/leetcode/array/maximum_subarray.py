"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

"""
- prendre le premier élément = current
- prendre le second elem
    - si current + elem >= current
        - current += elem
        - si current > best
            - best = current
    - sinon si current + elem > 0
        - current += elem
    - sinon
        - current = 0
"""


def solution(nums):
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    best = current = nums[0]

    for i in range(1, len(nums)):
        elem = nums[i]

        if current <= 0:
            current = elem
            if current > best:
                best = current
        elif current + elem >= current:
            current += elem
            if current > best:
                best = current
        elif current + elem > 0:
            current += elem
        else:
            current = elem

    return best


input1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
expected1 = 6

input2 = [-2, 1]
expected2 = 1

input3 = [-2, -1]
expected3 = -1

assert(solution(input1) == expected1)
assert(solution(input2) == expected2)
