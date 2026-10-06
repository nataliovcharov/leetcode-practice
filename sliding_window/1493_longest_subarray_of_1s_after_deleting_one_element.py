"""
1493. Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
Difficulty: Medium | Confidence: 3/5
Time: O(n) | Space: O(1)
Pattern: Sliding Window (dynamic)

KEY INSIGHT
Same as 1004 with k = 1: allow at most one zero in the window, shrink with
a while loop when there are more. The answer is window length - 1, because
I have to delete one element (even if it's all ones).

Note: update max_len at EVERY iteration.

SOLVED
- Sep 22, 2026: first solve
- 1 more re-solve in between (dates not logged)
- Sep 24, 2026: re-solve (3x total)

MISTAKES
- (none logged)
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.longestSubarray([1, 1, 0, 1]) == 3
    assert s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
    assert s.longestSubarray([1, 1, 1]) == 2
    print("All tests passed")
