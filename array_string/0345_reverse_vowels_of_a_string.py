"""
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
Difficulty: Easy | Confidence: 5/5
Time: O(n) | Space: O(n)
Pattern: Two Pointers (opposite ends)

KEY INSIGHT
Convert to a list (strings are immutable) so I can swap in place. Put the
vowels in a set, set("aeiouAEIOU"), for O(1) lookup. Two pointers from
opposite ends, swap when both land on vowels.

Time: list(s) O(n) + pointer scan O(n) + "".join O(n) -> O(n).
Space: the chars list and the output string are O(n); the set and pointers
are O(1). O(n) is unavoidable in Python because strings are immutable.

SOLVED
- Sep 13, 2026: first solve
- Sep 15, 2026: re-solve (2x total)

MISTAKES
- Sep 15: Logic was correct. I used if/if/if instead of if/elif/else and got
  confused for a second. With elif, each iteration moves one side; it just
  takes another iteration to move the other pointer before hitting the else
  (swap).
"""

from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.reverseVowels("IceCreAm") == "AceCreIm"
    assert s.reverseVowels("leetcode") == "leotcede"
    print("All tests passed")
