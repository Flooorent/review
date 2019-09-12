"""
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from collections import defaultdict


def solution(nums):
    solutions = set()

    positives = defaultdict(int)
    negatives = defaultdict(int)
    nb_zeros = 0

    if not nums:
        return list(solutions)

    for num in nums:
        if num == 0:
            nb_zeros += 1
        elif num > 0:
            positives[num] += 1
        else:
            negatives[num] += 1

    if nb_zeros >= 3:
        solutions.add((0, 0, 0))

    if not positives or not negatives:
        return solutions

    if nb_zeros >= 1:
        for key in negatives.keys():
            if - key in positives:
                solutions.add((key, 0, - key))

    for key1 in negatives.keys():
        for key2 in negatives.keys():
            if key1 == key2 and negatives[key1] == 1:
                continue

            if - (key1 + key2) in positives:
                if key1 <= key2:
                    solutions.add((key1, key2, - (key1 + key2)))
                else:
                    solutions.add((key2, key1, - (key1 + key2)))

    for key1 in positives.keys():
        for key2 in positives.keys():
            if key1 == key2 and positives[key1] == 1:
                continue

            if - (key1 + key2) in negatives:
                if key1 <= key2:
                    solutions.add((- (key1 + key2), key1, key2))
                else:
                    solutions.add((- (key1 + key2), key2, key1))

    return [list(tup) for tup in list(solutions)]


data = [-1, 0, 1, 2, -1, -4]
expected = [[-1, 0, 1], [-1, -1, 2]]

assert(sorted(solution(data)) == sorted(expected))
