"""
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/

Difficulty:  Easy
Pattern:     Prefix Sum
LeetCode 75: yes
Confidence:  3/5
Solved:      2x  (first 2026-09-23, last 2026-09-24)

Time:  O(n)
Space: O(1)

Key insight:
    Looking for the index where left_sum == right_sum.
    total = sum(nums) up front. At each i:
        right_sum = total - nums[i] - left_sum
        if left_sum == right_sum: return i
        left_sum += nums[i]
    Return -1 if none.

    Time: sum() O(n) + loop O(n) -> O(n).

Mistakes log:
    - (none yet)
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert s.pivotIndex([1, 2, 3]) == -1
    assert s.pivotIndex([2, 1, -1]) == 0
    print("All tests passed")
