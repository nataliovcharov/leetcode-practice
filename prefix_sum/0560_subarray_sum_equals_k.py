"""
560. Subarray Sum Equals K  (extra, not LeetCode 75)
https://leetcode.com/problems/subarray-sum-equals-k/
Difficulty: Medium | Confidence: 3/5
Time: O(n) | Space: O(n)
Pattern: Prefix Sum + Hashmap

KEY INSIGHT
Main identity:  sum(i..j) = prefix[j] - prefix[i - 1]

I want prefix[j] - prefix[i - 1] == k, so I look for
prefix[i - 1] == prefix[j] - k: an earlier prefix (one I've already
passed) that I can "chop off" the front so what's left sums to k.

Keep a hashmap of prefix sum -> how many times I've seen it. Start it as
{0: 1} so subarrays starting at index 0 get counted. At each step:
    count += seen.get(prefix - k, 0)
    seen[prefix] += 1     (AFTER the lookup)

Brute force = 303's sumRange on every pair (i, j), O(n^2). The inner loop is
just searching earlier prefixes for prefix - k, so the hashmap replaces it.
Rule: LOOK UP prefix - k, STORE prefix.

SOLVED
- Sep 23, 2026: first solve
- Sep 24, 2026: re-solve
- Oct 4, 2026: re-solve: brute force (303 on every pair) -> hashmap

MISTAKES
- (none logged)
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_map = {0: 1}
        curr = 0

        for n in nums:
            curr += n
            diff = curr - k
            count += prefix_map.get(diff, 0)
            prefix_map[curr] = prefix_map.get(curr, 0) + 1

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.subarraySum([1, 1, 1], 2) == 2
    assert s.subarraySum([1, 2, 3], 3) == 2
    assert s.subarraySum([1, -1, 0], 0) == 3
    print("All tests passed")
