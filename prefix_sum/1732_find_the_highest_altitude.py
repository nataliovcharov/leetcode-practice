"""
1732. Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/

Difficulty:  Easy
Pattern:     Prefix Sum
LeetCode 75: yes
Confidence:  5/5
Solved:      2x  (first 2026-09-23, last 2026-09-24)

Time:  O(n)
Space: O(1)

Key insight:
    Initialize prefix = 0 AND max_alt = 0 (the starting altitude counts).
    Iterate gain, add to prefix each step, update the max.

Mistakes log:
    - (none yet)
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
