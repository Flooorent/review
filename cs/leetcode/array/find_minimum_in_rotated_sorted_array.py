from typing import List


def solution1(nums: List[int]) -> int:
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    minimum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return min(minimum, nums[i])

    # in case there is only one element in nums
    return minimum


def solution2(nums: List[int]) -> int:
    """
    time complexity: O(log(n))
    space complexity: O(1)
    """
    first_index = 0
    last_index = len(nums) - 1

    # dernière condition : pour éviter les cas où les index font (1+2)//2 = 1 et on tourne en boucle
    while first_index != last_index and first_index + 1 != last_index:
        middle_index = (first_index + last_index) // 2

        if nums[middle_index] < nums[0]:
            last_index = middle_index
        else:
            first_index = middle_index

    return min(nums[0], nums[first_index], nums[last_index])


input1 = [3, 4, 5, 1, 2]
output1 = 1

input2 = [4, 5, 6, 7, 0, 1, 2]
output2 = 0

input3 = [5, 6, 2, 3, 4]
output3 = 2

assert(solution1(input1) == output1)
assert(solution1(input2) == output2)

assert(solution2(input1) == output1)
assert(solution2(input2) == output2)
assert(solution2(input3) == output3)
