"""
334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/

Difficulty:  Medium
Pattern:     Array / String - Greedy
LeetCode 75: yes
Confidence:  3/5
Solved:      2x  (first 2026-09-14, last 2026-09-15)

Time:  O(n)
Space: O(1)

Key insight:
    Greedy, one pass. Keep first = the smallest number seen so far. If I see a
    number bigger than first, it becomes second. Keep both as SMALL as
    possible, because a tighter pair leaves more room for a valid third. If a
    number is bigger than both, I've found k and the triplet exists.

    Subtle part: first can get updated to a value that comes AFTER second in
    the array, so the pair isn't valid by position (need i < j < k). It's still
    correct, because when second was set there WAS a smaller element before it,
    and that fact doesn't expire. I only need existence, not the actual indices.

Mistakes log:
    - 2026-09-15: Logic right, but the conditions must be <= not <. With only <,
      first and second can end up equal and the sequence isn't strictly
      increasing. I used a while loop with a manual index; for num in nums
      is cleaner (no pointer to increment).
"""

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert s.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert s.increasingTriplet([2, 1, 5, 0, 4, 6]) is True
    print("All tests passed")
