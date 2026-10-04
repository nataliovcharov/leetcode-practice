"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Difficulty:  Medium
Pattern:     Two Pointers (opposite ends, move the shorter wall)
LeetCode 75: yes
Confidence:  4/5
Solved:      2x  (first 2026-09-20, last 2026-09-21)

Time:  O(n)
Space: O(1)

Key insight:
    Start at opposite ends and only move the pointer whose wall is shorter.

    Why: I start at maximum width, so width can only shrink. For the shorter
    wall, every remaining pair is both narrower AND capped at the same height,
    so it's strictly worse than what I just measured. That wall can't improve,
    so I drop it and keep searching among the rest.

Mistakes log:
    - (none yet)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 1]) == 1
    print("All tests passed")
