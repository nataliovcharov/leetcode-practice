"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/
Difficulty: Easy | Confidence: 3/5
Time: O(n) | Space: O(1)
Pattern: Sliding Window (fixed size)

KEY INSIGHT
Start with window_sum = sum(nums[:k]). Then loop for i in
range(len(nums) - k). It only goes up to len(nums) - k because each step
adds nums[i + k], so the loop still reaches every element.

Main line:  window_sum += nums[i + k] - nums[i]
            (add the new rightmost, remove the old leftmost)
Track the max sum, return max_sum / k.

SOLVED
- Sep 21, 2026: first solve
- 1 more re-solve in between (dates not logged)
- Sep 24, 2026: re-solve (3x total)

MISTAKES
- Sep 24: Completely messed up the pointers. Thought it was a dynamic
  window; it's FIXED size.
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert abs(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-5
    assert abs(s.findMaxAverage([5], 1) - 5.0) < 1e-5
    print("All tests passed")
