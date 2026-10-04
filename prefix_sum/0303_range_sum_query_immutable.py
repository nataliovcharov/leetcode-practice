"""
303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/

Difficulty:  Easy
Pattern:     Prefix Sum
LeetCode 75: no (extra practice)
Confidence:  4/5
Solved:      1x  (first 2026-10-01, last 2026-10-01)

Time:  O(n) build, O(1) per query
Space: O(n)

Key insight:
    Build the prefix array once in __init__, so sumRange is just a
    subtraction. With a leading 0 (prefix[0] = 0, prefix[i + 1] = sum of
    nums[:i + 1]):
        sumRange(l, r) = prefix[r + 1] - prefix[l]
    The leading 0 removes the l == 0 edge case.

Mistakes log:
    - (none yet)
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        # TODO: paste my solution
        raise NotImplementedError

    def sumRange(self, left: int, right: int) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    assert na.sumRange(0, 2) == 1
    assert na.sumRange(2, 5) == -1
    assert na.sumRange(0, 5) == -3
    print("All tests passed")
