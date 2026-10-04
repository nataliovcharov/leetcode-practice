"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/

Difficulty:  Easy
Pattern:     Two Pointers (both start at the beginning)
LeetCode 75: yes
Confidence:  5/5
Solved:      2x  (first 2026-09-20, last 2026-09-21)

Time:  O(n)
Space: O(1)

Key insight:
    Both pointers start at the beginning. Walk through t every step, but only
    advance the pointer on s when the characters match. s is a subsequence of t
    if its pointer reaches len(s).

Mistakes log:
    - (none yet)
"""

from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    sol = Solution()
    assert sol.isSubsequence("abc", "ahbgdc") is True
    assert sol.isSubsequence("axc", "ahbgdc") is False
    assert sol.isSubsequence("", "ahbgdc") is True
    print("All tests passed")
