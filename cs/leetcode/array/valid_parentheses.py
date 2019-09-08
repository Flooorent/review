"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""

closers_to_openers = {
    ')': '(',
    '}': '{',
    ']': '[',
}


class ValidParentheses:
    @staticmethod
    def with_stack(s):
        """
        time complexity: O(n)
            - traversée de la string: O(n)
            - append: O(1)
            - pop last: O(1)
        space complexity: O(n)
        """
        stack = []
        for letter in s:
            if letter in ['(', '[', '{']:
                stack.append(letter)
                # if stack is empty and we try to remove a character, this is an error
            elif not stack:
                return False
            else:
                if stack[-1] == closers_to_openers[letter]:
                    stack.pop()
                else:
                    return False

        return not stack


input1 = "()"
input2 = "()[]{}"
input3 = "(]"
input4 = "([)]"
input5 = "{[]}"
input6 = ""

assert(ValidParentheses.with_stack(input1))
assert(ValidParentheses.with_stack(input2))
assert(not ValidParentheses.with_stack(input3))
assert(not ValidParentheses.with_stack(input4))
assert(ValidParentheses.with_stack(input5))
assert(ValidParentheses.with_stack(input6))
