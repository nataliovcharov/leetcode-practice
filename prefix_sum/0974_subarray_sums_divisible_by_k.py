"""
974. Subarray Sums Divisible by K  (extra, not LeetCode 75)
https://leetcode.com/problems/subarray-sums-divisible-by-k/
Difficulty: Medium | Confidence: 3/5
Time: O(n) | Space: O(k) (only remainders 0..k-1)
Pattern: Prefix Sum + Hashmap (count) - remainders

KEY INSIGHT
Identity as a condition: sum(i..j) divisible by k
    <-> sum[j] % k == sum[i-1] % k
Two numbers differ by a multiple of k exactly when they have the same
remainder (the multiples of k cancel, only the remainders matter).

Template: write the condition as EARLIER side == CURRENT side; LOOK UP the
current side, STORE the earlier side. Here both are prefix % k.

Counting -> map is remainder -> how many times seen, start with {0: 1}.
Same as 560, but the key is the remainder instead of the prefix.

Recognize: subarray + 'divisible by k' -> think remainders.
Negatives: Python % is never negative (-6 % 5 = 4); in Java/C++/JS use
((prefix % k) + k) % k.

SOLVED
- Oct 6, 2026: first solve

MISTAKES
- Oct 6: KEY REALIZATION I was missing: sum[j] % k == sum[i-1] % k. Many
  earlier prefixes can work (p, p-k, p+k...), so group them by what they
  share: the remainder.
- Oct 6: Was confused how -6 % 5 = 4: Python goes down to the multiple of k
  BELOW the number (-10), then counts up (+4).
"""

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_map = {0: 1}
        curr = 0

        for n in nums:
            curr += n
            remainder = curr % k
            count += prefix_map.get(remainder, 0)
            prefix_map[remainder] = prefix_map.get(remainder, 0) + 1

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5) == 7
    assert s.subarraysDivByK([5], 9) == 0
    print("All tests passed")
