"""
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/
Difficulty: Easy | Confidence: 3/5
Time: O(n) | Space: O(1)
Pattern: Prefix Sum

KEY INSIGHT
Looking for the index where left_sum == right_sum.
total = sum(nums) up front. At each i:
    right_sum = total - nums[i] - left_sum
    if left_sum == right_sum: return i
    left_sum += nums[i]
Return -1 if none.

Time: sum() O(n) + loop O(n) -> O(n).

SOLVED
- Sep 23, 2026: first solve
- Sep 24, 2026: re-solve (2x total)

MISTAKES
- (none logged)
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
