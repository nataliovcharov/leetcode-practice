"""
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/

Difficulty:  Medium
Pattern:     Prefix Sum + Hashmap
LeetCode 75: no (extra practice)
Confidence:  3/5
Solved:      in progress (started 2026-10-04)

Time:  O(n)
Space: TBD

Key insight:
    IN PROGRESS.

    Open question: why isn't this sliding window? If I count zeros and ones,
    even when I reach a point where the subarray is valid, the pointers may
    not reflect it. There's no rule for when to shrink, because adding an
    element can make an invalid window valid again.

    Hint to self: what transformation turns this into a problem I've already
    solved (560)?

Mistakes log:
    - (none yet)
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxLength([0, 1]) == 2
    assert s.findMaxLength([0, 1, 0]) == 2
    assert s.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]) == 6
    print("All tests passed")
