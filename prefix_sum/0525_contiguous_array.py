"""
525. Contiguous Array  (extra, not LeetCode 75)
https://leetcode.com/problems/contiguous-array/
Difficulty: Medium | Confidence: 3/5
Time: O(n) | Space: O(n)
Pattern: Prefix Sum + Hashmap

KEY INSIGHT
Start from the identity: sum(i..j) = prefix[j] - prefix[i-1], and ask what I
want sum(i..j) to measure: (number of 1s) - (number of 0s). With the original
values the 0s add nothing, so they need to CANCEL the 1s: 0 -> -1, 1 -> +1.

Balanced = sum(i..j) == 0 -> prefix[j] == prefix[i-1]. The SAME prefix
appearing twice means everything in between is balanced.

Longest -> map stores prefix -> FIRST index seen (never overwrite; the earliest
index gives the longest subarray). Start with {0: -1}: sum 0 happens just before
the array starts, so a balanced subarray from index 0 gets length i - (-1).

Recognize: subarray + 'equal number of X and Y' -> X = +1, Y = -1, then
prefix sum.

Why not sliding window: growing an unbalanced window can make it balanced
again (e.g. [1,1,0,0]), so there's no rule for when to shrink.

SOLVED
- Oct 4, 2026: started, stuck on why it isn't sliding window
- Oct 5, 2026: solved with a step-by-step walkthrough

MISTAKES
- Oct 5: Couldn't see the transformation on my own. 0 -> -1 is a known
  trick: the 0s have to cancel the 1s.
- Oct 5: Confused {0: -1} with 560's {0: 1}. The key is always the prefix
  sum; here the value is an INDEX (just before the array starts), not a
  count.
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        prefix = 0
        best = 0

        for i, n in enumerate(nums):
            if n == 1:
                prefix += 1
            else:
                prefix -= 1

            if prefix in first_seen:
                best = max(best, i - first_seen[prefix])
            else:
                first_seen[prefix] = i

        return best


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxLength([0, 1]) == 2
    assert s.findMaxLength([0, 1, 0]) == 2
    assert s.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]) == 6
    print("All tests passed")
