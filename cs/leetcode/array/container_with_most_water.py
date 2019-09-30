from typing import List


def solution1(height: List[int]) -> int:
    """Time limit exceeded sur array ordonné de façon croissante car du coup on est O(n^2)"""
    tops = []
    current = 0

    for i, x in enumerate(height):
        for k, (j, y, res) in enumerate(tops):
            volume = (i - j) * min(x, y)
            if volume > res:
                tops[k] = (j, y, volume)

        if x > current:
            tops.append((i, x, 0))
            current = x

    return max([top for _, _, top in tops])


def solution2(height: List[int]) -> int:
    left_candidates = []
    right_candidates = []

    top_left = 0
    top_right = 0

    for left_index in range(len(height)):
        right_index = len(height) - left_index - 1
        left = height[left_index]
        right = height[right_index]

        if left > top_left:
            left_candidates.append((left_index, left))
            top_left = left

        if right > top_right:
            right_candidates.append((right_index, right))
            top_right = right

    top_volume = 0

    for left_index, left_value in left_candidates:
        for right_index, right_value in right_candidates:
            volume = abs(left_index - right_index) * min(left_value, right_value)
            if volume > top_volume:
                top_volume = volume

    return top_volume


def best_solution(height: List[int]) -> int:
    left_pointer = 0
    right_pointer = len(height) - 1
    top_volume = 0

    while left_pointer < right_pointer:
        left_value = height[left_pointer]
        right_value = height[right_pointer]

        volume = (right_pointer - left_pointer) * min(left_value, right_value)

        if volume > top_volume:
            top_volume = volume

        if left_value <= right_value:
            left_pointer += 1
        else:
            right_pointer -= 1

    return top_volume


input1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
expected1 = 49

input2 = [3, 8, 7, 4]
expected2 = 9

assert(solution1(input1) == expected1)
assert(solution1(input2) == expected2)

assert(solution2(input1) == expected1)
assert(solution2(input2) == expected2)

#assert(best_solution(input1) == expected1)
#assert(best_solution(input2) == expected2)

print(best_solution(input1))
print(best_solution(input2))
