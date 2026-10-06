"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium | Confidence: 4/5
Time: O(n) | Space: O(1)
Pattern: Two Pointers (opposite ends, move the shorter wall)

KEY INSIGHT
Start at opposite ends and only move the pointer whose wall is shorter.

Why: I start at maximum width, so width can only shrink. For the shorter
wall, every remaining pair is both narrower AND capped at the same height,
so it's strictly worse than what I just measured. That wall can't improve,
so I drop it and keep searching among the rest.

SOLVED
- Sep 20, 2026: first solve
- Sep 21, 2026: re-solve (2x total)

MISTAKES
- (none logged)
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
