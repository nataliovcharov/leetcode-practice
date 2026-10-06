"""
1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
Difficulty: Medium | Confidence: 3/5
Time: O(n) | Space: O(1)
Pattern: Sliding Window (fixed size)

KEY INSIGHT
Vowels in a set for O(1) lookup. Move the right pointer through the string,
counting vowels. As soon as the window gets longer than k
(r - l + 1 > k), shrink it: if s[l] is a vowel decrement count, then l += 1.
Track the max count.

SOLVED
- Sep 21, 2026: first solve
- 1 more re-solve in between (dates not logged)
- Sep 24, 2026: re-solve (3x total)

MISTAKES
- (none logged)
"""

from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxVowels("abciiidef", 3) == 3
    assert sol.maxVowels("aeiou", 2) == 2
    assert sol.maxVowels("leetcode", 3) == 2
    print("All tests passed")
