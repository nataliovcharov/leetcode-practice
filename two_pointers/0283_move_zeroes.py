"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Difficulty:  Easy
Pattern:     Two Pointers (both start at the beginning)
LeetCode 75: yes
Confidence:  3/5
Solved:      3x  (first 2026-09-19, last 2026-09-21)

Time:  O(n)
Space: O(1)

Key insight:
    i always points to where I write next; j scans for non-zero numbers. When
    nums[j] isn't zero, swap it to nums[i] and move i. Zeros just get skipped
    by j. The idea is to only bring actual numbers forward and let the zeros
    end up at the back.

Mistakes log:
    - (none yet)
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    a = [0, 1, 0, 3, 12]; s.moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]
    a = [0]; s.moveZeroes(a)
    assert a == [0]
    print("All tests passed")
