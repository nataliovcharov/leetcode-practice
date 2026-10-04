"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Difficulty:  Medium
Pattern:     Sliding Window (dynamic)
LeetCode 75: yes
Confidence:  3/5
Solved:      3x  (first 2026-09-21, last 2026-09-24)

Time:  O(n)
Space: O(1)

Key insight:
    Move the right pointer through the array and count zeros. Dynamic window,
    so there's a while loop that shrinks until the window is valid again:
        while zeros > k: if nums[l] == 0: zeros -= 1; l += 1
    Track the max length r - l + 1.

Mistakes log:
    - (none yet)
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
