"""
605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/

Difficulty:  Easy
Pattern:     Array / String - Greedy
LeetCode 75: yes
Confidence:  4/5
Solved:      2x  (first 2026-09-12, last 2026-09-15)

Time:  O(n)
Space: O(1)

Key insight:
    Greedy: make a sequence of decisions, take the locally best option at each
    step, never reconsider.

    Look at the spot before and after each candidate. First and last positions
    are edge cases: the left side counts as empty if i == 0 or
    flowerbed[i - 1] == 0, and the same logic applies on the right for the end
    of the array.

Mistakes log:
    - 2026-09-15: Remembered the logic but forgot that when I find an eligible
      spot I HAVE to set flowerbed[i] = 1, because the next spot's
      eligibility depends on it.
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True
    assert s.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False
    assert s.canPlaceFlowers([0], 1) is True
    print("All tests passed")
