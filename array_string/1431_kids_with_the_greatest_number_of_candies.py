"""
1431. Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Difficulty:  Easy
Pattern:     Array / String
LeetCode 75: yes
Confidence:  5/5
Solved:      2x  (first 2026-09-12, last 2026-09-15)

Time:  O(n)
Space: O(1) extra (O(n) for the result list)

Key insight:
    Compute the max once with max(candies), then loop and check whether
    candies[i] + extraCandies >= that max.

Mistakes log:
    - 2026-09-15: Logic was right, but I wrote res[i] = True on an empty list
      (res = []). Have to append. Also: I can find the max with a loop
      instead of max(candies).
"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]
    assert s.kidsWithCandies([4, 2, 1, 1, 2], 1) == [True, False, False, False, False]
    assert s.kidsWithCandies([12, 1, 12], 10) == [True, False, True]
    print("All tests passed")
