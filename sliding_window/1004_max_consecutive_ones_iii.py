"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/
Difficulty: Medium | Confidence: 3/5
Time: O(n) | Space: O(1)
Pattern: Sliding Window (dynamic)

KEY INSIGHT
Move the right pointer through the array and count zeros. Dynamic window,
so there's a while loop that shrinks until the window is valid again:
    while zeros > k: if nums[l] == 0: zeros -= 1; l += 1
Track the max length r - l + 1.

SOLVED
- Sep 21, 2026: first solve
- 1 more re-solve in between (dates not logged)
- Sep 24, 2026: re-solve (3x total)

MISTAKES
- (none logged)
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10
    print("All tests passed")
