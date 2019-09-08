"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

from collections import Counter, defaultdict


class ValidAnagram:
    @staticmethod
    def with_sort(s, t):
        """
        n = len(s) = len(t)
        time complexity: O(nlog(n))
        space complexity: O(1). NB: O(1) et pas O(n) car:
            - l'espace pris dépend de l'agorithme de sort utilisé. heapsort prend par
            exemple 0(1) en espace auxiliaire. On ignore le coup d'une copie car c'est
            un détail dépendant du langage et que ça dépend de la façon dont la fonction
            est codée
        """
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    @staticmethod
    def with_counters(s, t):
        """
        time complexity: O(n)
        space complexity: O(n)
        => en fait on a au maximum 26 lettres donc c'est O(1). De plus, on n'est pas obligé
        d'avoir deux counters, on peut d'abord incrémenter pour les lettres de s puis décrémenter
        pour les lettres de t et comparer ensuite les valeurs à 0.
        """
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

    @staticmethod
    def with_hash_tables(s, t):
        s_counter = {}
        t_counter = {}

        for letter in s:
            if letter in s_counter:
                s_counter[letter] += 1
            else:
                s_counter[letter] = 1

        for letter in t:
            if letter in t_counter:
                t_counter[letter] += 1
            else:
                t_counter[letter] = 1

        return s_counter == t_counter

    @staticmethod
    def with_default_dict(s, t):
        if len(s) != len(t):
            return False

        s_counter = defaultdict(int)
        t_counter = defaultdict(int)

        for letter in s:
            s_counter[letter] += 1

        for letter in t:
            t_counter[letter] += 1

        return s_counter == t_counter


s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

assert(ValidAnagram.with_sort(s1, t1))
assert(not ValidAnagram.with_sort(s2, t2))

assert(ValidAnagram.with_counters(s1, t1))
assert(not ValidAnagram.with_counters(s2, t2))

assert(ValidAnagram.with_hash_tables(s1, t1))
assert(not ValidAnagram.with_hash_tables(s2, t2))

assert(ValidAnagram.with_default_dict(s1, t1))
assert(not ValidAnagram.with_default_dict(s2, t2))
