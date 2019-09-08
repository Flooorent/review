"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

from collections import Counter, defaultdict


def solution(strs):
    """
    n = len(strs)
    m = taille de la plus longue string dans strs

    time complexity: O(n * m * log(m))
        - O(n) itération sur chaque mot
        - O(m * log(m)) pour le sort
        - O(1) pour insertion/append
    space complexity: O(n * m)
    """
    anagrams = defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


def solution_avec_count(strs):
    """
    time complexity: O(n * m)
    space complexity: O(n * m)
    """
    ans = defaultdict(list)

    for s in strs:
        # l'idée qui change tout: avoir un array de taille 26 puisqu'on travaille avec des lettres !!!
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)

    return ans.values()


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

expected = [
  ["ate", "eat", "tea"],
  ["nat", "tan"],
  ["bat"],
]

print(solution(words))
