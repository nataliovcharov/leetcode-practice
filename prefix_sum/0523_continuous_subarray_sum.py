"""
523. Continuous Subarray Sum  (extra, not LeetCode 75)
https://leetcode.com/problems/continuous-subarray-sum/
Difficulty: Medium | Confidence: 3/5
Time: O(n) | Space: O(min(n, k))
Pattern: Prefix Sum + Hashmap (first index) - remainders

KEY INSIGHT
974's condition + 525's map. sum(i..j) = n * k <-> sum[j] % k == sum[i-1] % k.
Look up and store prefix % k.

The map value is the FIRST INDEX (not a count) because I need the length:
length = i - first_seen[remainder], and it must be >= 2. Start with {0: -1}.

Three cases:
  1. remainder seen before, length >= 2 -> return True
  2. seen before, length < 2 -> do nothing, KEEP the earlier index
  3. never seen -> store remainder: i
Never overwrite: [5, 0, 0], k = 3 -> overwriting at i = 1 would miss [0, 0].

Recognize: subarray + divisible by k + exists/length -> remainders + first index.

SOLVED
- Oct 6, 2026: first solve

MISTAKES
- Oct 6: Needed help with the map value: it's an INDEX (to check length),
  not a count like 974.
- Oct 6: prefix_map[key] crashes (KeyError) if the key is missing -> check
  'if key in prefix_map' first.
- Oct 6: My first accepted version set index = i in the else branch just so
  the length check would fail. It works, but checking the length inside the
  'if' (only when there's an earlier match) follows the logic better, so I
  switched to that.
"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curr = 0
        prefix_map = {0: -1}

        for i, n in enumerate(nums):
            curr += n
            remainder = curr % k

            if remainder in prefix_map:
                if i - prefix_map[remainder] >= 2:
                    return True
            else:
                prefix_map[remainder] = i

        return False


if __name__ == "__main__":
    s = Solution()
    assert s.checkSubarraySum([23, 2, 4, 6, 7], 6) is True
    assert s.checkSubarraySum([23, 2, 6, 4, 7], 6) is True
    assert s.checkSubarraySum([23, 2, 6, 4, 7], 13) is False
    assert s.checkSubarraySum([5, 0, 0], 3) is True
    assert s.checkSubarraySum([0, 0], 5) is True
    print("All tests passed")
