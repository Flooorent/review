"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]

Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


def solution(intervals):
    """
    time complexity: O(n * log(n)) (sort)
    space complexity: O(1)
        - l'output ne compte pas
        - le sort peut se faire en O(1)
    """
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    output = []

    for interval in sorted_intervals:
        if not output or interval[0] > output[-1][1]:
            output.append(interval)
        else:
            output[-1][1] = max(output[-1][1], interval[1])

    return output


input1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
output1 = [[1, 6], [8, 10], [15, 18]]

input2 = [[1, 4], [4, 5]]
output2 = [[1, 5]]

input3 = [[1, 3], [8, 10], [2, 6]]
output3 = [[1, 6], [8, 10]]

input4 = [[2, 3], [8, 10], [1, 11]]
output4 = [[1, 11]]

assert(solution(input1) == output1)
assert(solution(input2) == output2)
assert(solution(input3) == output3)
assert(solution(input4) == output4)
