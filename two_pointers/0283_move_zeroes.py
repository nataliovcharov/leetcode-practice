"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
Difficulty: Easy | Confidence: 3/5
Time: O(n) | Space: O(1)
Pattern: Two Pointers (both start at the beginning)

KEY INSIGHT
i always points to where I write next; j scans for non-zero numbers. When
nums[j] isn't zero, swap it to nums[i] and move i. Zeros just get skipped
by j. The idea is to only bring actual numbers forward and let the zeros
end up at the back.

SOLVED
- Sep 19, 2026: first solve
- 1 more re-solve in between (dates not logged)
- Sep 21, 2026: re-solve (3x total)

MISTAKES
- (none logged)
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    a = [0, 1, 0, 3, 12]; s.moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]
    a = [0]; s.moveZeroes(a)
    assert a == [0]
    print("All tests passed")
