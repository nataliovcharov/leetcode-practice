"""
1732. Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/
Difficulty: Easy | Confidence: 5/5
Time: O(n) | Space: O(1)
Pattern: Prefix Sum

KEY INSIGHT
Initialize prefix = 0 AND max_alt = 0 (the starting altitude counts).
Iterate gain, add to prefix each step, update the max.

SOLVED
- Sep 23, 2026: first solve
- Sep 24, 2026: re-solve (2x total)

MISTAKES
- (none logged)
"""

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.largestAltitude([-5, 1, 5, 0, -7]) == 1
    assert s.largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0
    print("All tests passed")
