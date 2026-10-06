"""
1248. Count Number of Nice Subarrays  (extra, not LeetCode 75)
https://leetcode.com/problems/count-number-of-nice-subarrays/
Difficulty: Medium | Confidence: 3/5
Time: O(n) | Space: O(n)
Pattern: Prefix Sum + Hashmap (count) - transform input

KEY INSIGHT
560 in disguise. Transform: odd -> 1, even -> 0. Then 'exactly k odd numbers'
becomes 'subarray sum equals k', and it's 930/560 exactly.

curr counts the odd numbers seen so far (n % 2 is the remainder after
dividing by 2: 1 = odd, 0 = even).

Recognize: counting subarrays with EXACTLY k of something -> map each element
to 1 (has it) or 0 (doesn't), then use the 560 template.

SOLVED
- Oct 5, 2026: first solve

MISTAKES
- Oct 5: Flipped the condition: wrote 'if not n % 2' (true for EVEN) instead
  of 'if n % 2' (true for ODD). Example 2 ([2,4,6], k=1) should obviously be
  0, so trace the 'obvious' examples first.
"""

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_map = {0: 1}
        curr = 0

        for n in nums:
            if n % 2:
                curr += 1

            diff = curr - k
            count += prefix_map.get(diff, 0)
            prefix_map[curr] = prefix_map.get(curr, 0) + 1

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2
    assert s.numberOfSubarrays([2, 4, 6], 1) == 0
    assert s.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16
    print("All tests passed")
