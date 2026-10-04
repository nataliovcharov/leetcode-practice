"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Difficulty:  Medium
Pattern:     Prefix Sum + Hashmap
LeetCode 75: no (extra practice)
Confidence:  3/5
Solved:      2x  (first 2026-09-23, last 2026-09-24)

Time:  O(n)
Space: O(n)

Key insight:
    Main identity:  sum(i..j) = prefix[j] - prefix[i - 1]

    I want prefix[j] - prefix[i - 1] == k, so I look for
    prefix[i - 1] == prefix[j] - k: an earlier prefix (one I've already
    passed) that I can "chop off" the front so what's left sums to k.

    Keep a hashmap of prefix sum -> how many times I've seen it. Start it as
    {0: 1} so subarrays starting at index 0 get counted. At each step:
        count += seen.get(prefix - k, 0)
        seen[prefix] += 1     (AFTER the lookup)

Mistakes log:
    - (none yet)
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.subarraySum([1, 1, 1], 2) == 2
    assert s.subarraySum([1, 2, 3], 3) == 2
    assert s.subarraySum([1, -1, 0], 0) == 3
    print("All tests passed")
