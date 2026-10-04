"""
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/

Difficulty:  Easy
Pattern:     Array / String - Math (GCD)
LeetCode 75: yes
Confidence:  3/5
Solved:      2x  (first 2026-09-12, last 2026-09-15)

Time:  O(min(m, n) * (m + n))
Space: O(m + n)

Key insight:
    Brute force it first to see that I have to take the shorter string and check
    its prefixes, starting from the LONGEST (I want the largest x), to find the
    one that divides both strings.

    Main loop: for k from min(len1, len2) down to 1, call valid(k). The first
    k that passes -> return str1[:k].

    valid(k):
      - if len1 % k or len2 % k -> False (lengths have to divide evenly)
      - base = str1[:k]; n1, n2 = len1 // k, len2 // k
      - return str1 == base * n1 and str2 == base * n2

    Time: the loop is O(min(m, n)) and each valid() builds/compares O(m + n)
    chars -> multiplied, O(min(m, n) * (m + n)).
    Space: the strings I build are about m + n chars at peak.

Mistakes log:
    - 2026-09-15: Couldn't remember how to solve it. Looked at the solution
      again, then solved it twice without looking.
"""

from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert s.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert s.gcdOfStrings("LEET", "CODE") == ""
    print("All tests passed")
