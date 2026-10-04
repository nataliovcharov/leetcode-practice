"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Difficulty:  Easy
Pattern:     Two Pointers (exhaust both, from the back)
LeetCode 75: no (extra practice)
Confidence:  4/5
Solved:      1x  (first 2026-09-10, last 2026-09-10)

Time:  O(m + n)
Space: O(1)

Key insight:
    Go BACKWARDS. Going front-to-back would overwrite values in nums1 I haven't
    compared yet. The tail of nums1 is zeros I don't need, so it's safe to write
    there.

    Main loop: while both inputs still have elements, compare, write the
    "winner" at nums1[last], and move only that pointer.
    Cleanup: when one input runs out, handle what's left of the other.

    Time: each step writes one element and moves one pointer -> O(m + n).
    Space: merging in place, no extra array -> O(1).

Mistakes log:
    - (none yet)
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3, 0, 0, 0]; s.merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6]
    a = [1]; s.merge(a, 1, [], 0)
    assert a == [1]
    a = [0]; s.merge(a, 0, [1], 1)
    assert a == [1]
    print("All tests passed")
