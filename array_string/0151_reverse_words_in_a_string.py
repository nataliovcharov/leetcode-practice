"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/
Difficulty: Medium | Confidence: 5/5 (built-ins), 3/5 (two pointers)
Time: O(n) | Space: O(n)
Pattern: Built-ins / Two Pointers (anchor + scanner, from back)

KEY INSIGHT
Solution 1 (built-ins), confidence 5:
  Strip leading/trailing whitespace, split into a list, reverse the list,
  join with single spaces.
  Time: strip O(n) + reverse O(w) + join O(n) -> O(n). Space: O(n).

Solution 2 (two pointers), confidence 3:
  Start at the BACK. Skip whitespace (only need one variable for this).
  When I hit a word, drop an anchor j there, then keep decrementing i
  until I hit a space, which is the start of the word. Append s[i + 1:j + 1]
  to res. At the end, " ".join(res).
  Time: i only moves from len(s) down to 0, never resets -> O(n). Slices
  add up to O(n). Space: res holds <= n chars -> O(n).

SOLVED
- Sep 13, 2026: first solve
- Sep 15, 2026: re-solve (2x total)

MISTAKES
- Sep 15: Built-ins version, fully remembered.
- Sep 15: Two-pointer version, didn't remember at all. Start from the end,
  skip spaces, anchor, decrement until a space, slice (use Python slicing!)
  and append.
"""

from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        # TODO: paste my solution
        raise NotImplementedError

    def reverseWordsTwoPointers(self, s: str) -> str:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    for fn in (s.reverseWords, s.reverseWordsTwoPointers):
        assert fn("the sky is blue") == "blue is sky the"
        assert fn("  hello world  ") == "world hello"
        assert fn("a good   example") == "example good a"
    print("All tests passed")
