"""
303. Range Sum Query - Immutable  (extra, not LeetCode 75)
https://leetcode.com/problems/range-sum-query-immutable/
Difficulty: Easy | Confidence: 4/5
Time: O(n) build, O(1) per query | Space: O(n)
Pattern: Prefix Sum

KEY INSIGHT
Build the prefix array once in __init__, so sumRange is just a
subtraction. With a leading 0 (prefix[0] = 0, prefix[i + 1] = sum of
nums[:i + 1]):
    sumRange(l, r) = prefix[r + 1] - prefix[l]
The leading 0 removes the l == 0 edge case.

My version has no leading 0, so prefix[k] = sum of nums[0..k] inclusive and
sumRange = prefix[right] - prefix[left - 1], with a special case for left == 0
(prefix[-1] in Python would silently return the LAST element).

SOLVED
- Oct 1, 2026: first solve
- Oct 4, 2026: re-solve: my version without the leading 0

MISTAKES
- (none logged)
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0

        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        if left > 0:
            leftSum = self.prefix[left - 1]
        else:
            leftSum = 0
        return rightSum - leftSum


if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    assert na.sumRange(0, 2) == 1
    assert na.sumRange(2, 5) == -1
    assert na.sumRange(0, 5) == -3
    print("All tests passed")
