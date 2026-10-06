"""
930. Binary Subarrays With Sum  (extra, not LeetCode 75)
https://leetcode.com/problems/binary-subarrays-with-sum/
Difficulty: Medium | Confidence: 4/5
Time: O(n) | Space: O(n)
Pattern: Prefix Sum + Hashmap (count)

KEY INSIGHT
Same algorithm as 560, with goal instead of k. Identity:
sum(i..j) = prefix[j] - prefix[i-1] = goal, so look for an EARLIER prefix equal
to curr - goal. Every time it appeared before is a valid subarray ending here,
so add its count (not just 1).

Rule: search for curr - goal, STORE curr. Start the map with {0: 1}.

Alt: no negatives, so sliding window also works:
exactly(goal) = at_most(goal) - at_most(goal - 1); count += right - left + 1.
O(1) space, but only because all values are >= 0 (doesn't work for 560).

SOLVED
- Oct 5, 2026: first solve, plus the sliding window version

MISTAKES
- Oct 5: Stored diff (curr - goal) in the map instead of curr. Example 2
  still passed because goal = 0 makes diff == curr, so always test more than
  one example.
"""

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_map = {0: 1}
        curr = 0

        for n in nums:
            curr += n
            diff = curr - goal
            count += prefix_map.get(diff, 0)
            prefix_map[curr] = prefix_map.get(curr, 0) + 1

        return count

    def numSubarraysWithSumSlidingWindow(self, nums: List[int], goal: int) -> int:
        def at_most(g):
            if g < 0:
                return 0
            left = window_sum = count = 0
            for right in range(len(nums)):
                window_sum += nums[right]
                while window_sum > g:
                    window_sum -= nums[left]
                    left += 1
                count += right - left + 1
            return count

        return at_most(goal) - at_most(goal - 1)


if __name__ == "__main__":
    s = Solution()
    for fn in (s.numSubarraysWithSum, s.numSubarraysWithSumSlidingWindow):
        assert fn([1, 0, 1, 0, 1], 2) == 4
        assert fn([0, 0, 0, 0, 0], 0) == 15
    print("All tests passed")
