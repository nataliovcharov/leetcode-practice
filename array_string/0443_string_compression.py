"""
443. String Compression
https://leetcode.com/problems/string-compression/

Difficulty:  Medium
Pattern:     Two Pointers (anchor + scanner, plus a write pointer)
LeetCode 75: yes
Confidence:  3/5
Solved:      1x  (first 2026-09-15, last 2026-09-15)

Time:  O(n)
Space: O(1)

Key insight:
    Two pointers with two while loops, plus a separate write index. In the
    outer loop, anchor j = i, then scan j forward in the inner loop while it's
    the same char. When it stops, count = j - i. Write the char, then the count
    if it's > 1.

    Trick: to write a multi-digit count, iterate over str(count):
        for digit in str(count): ...

Mistakes log:
    - (none yet)
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    c = ["a", "a", "b", "b", "c", "c", "c"]
    assert s.compress(c) == 6 and c[:6] == ["a", "2", "b", "2", "c", "3"]
    c = ["a"]
    assert s.compress(c) == 1 and c[:1] == ["a"]
    c = ["a"] + ["b"] * 12
    assert s.compress(c) == 4 and c[:4] == ["a", "b", "1", "2"]
    print("All tests passed")
