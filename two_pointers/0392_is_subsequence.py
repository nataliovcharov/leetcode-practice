"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/
Difficulty: Easy | Confidence: 5/5
Time: O(n) | Space: O(1)
Pattern: Two Pointers (both start at the beginning)

KEY INSIGHT
Both pointers start at the beginning. Walk through t every step, but only
advance the pointer on s when the characters match. s is a subsequence of t
if its pointer reaches len(s).

SOLVED
- Sep 20, 2026: first solve
- Sep 21, 2026: re-solve (2x total)

MISTAKES
- (none logged)
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
