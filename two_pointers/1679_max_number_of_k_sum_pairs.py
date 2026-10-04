"""
1679. Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/

Difficulty:  Medium
Pattern:     Two Pointers (sort, then opposite ends)
LeetCode 75: yes
Confidence:  4/5
Solved:      2x  (first 2026-09-20, last 2026-09-21)

Time:  O(n log n) (the sort dominates)
Space: O(n) (Python's sort; O(1) besides that)

Key insight:
    Sort first, then start at opposite ends.
      - sum < k  -> i += 1. nums[i] already got the biggest boost possible
                    (nums[j] is the largest left), so drop it.
      - sum > k  -> j -= 1. nums[j] is already paired with the smallest
                    number left and it's still too big.
      - sum == k -> count += 1, move BOTH pointers.

    Why: the array is sorted, so nums[j] is the largest number left. If even
    that isn't enough to reach k, pairing nums[i] with anything else (all
    smaller) gives an even smaller sum. It can never reach k.

    Note: I originally wrote O(n) time / O(1) space, but the sort makes it
    O(n log n). A hashmap version can do it in O(n) time with O(n) space.

Mistakes log:
    - 2026-09-21: Forgot to move the pointers after incrementing count when a
      pair is found.
"""

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.maxOperations([1, 2, 3, 4], 5) == 2
    assert s.maxOperations([3, 1, 3, 4, 3], 6) == 1
    print("All tests passed")
