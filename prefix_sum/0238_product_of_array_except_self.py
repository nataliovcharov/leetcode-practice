"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium | Confidence: 4/5
Time: O(n) | Space: O(1) (output array doesn't count, per the problem)
Pattern: Prefix Sum (prefix x postfix product)

KEY INSIGHT
Two passes: prefix x postfix.

Pass 1 (left -> right): prefix = 1 (product of nothing before index 0).
At each i: res[i] = prefix, THEN prefix *= nums[i]. After this pass, res[i]
is the product of everything strictly left of i.

Pass 2 (right -> left): postfix = 1. At each i: res[i] *= postfix, THEN
postfix *= nums[i]. Now each slot is also multiplied by everything strictly
right of i.

res[i] = (everything left) x (everything right) = product except self.
(LeetCode 75 lists this under Array / String; I keep it with prefix sum.)

SOLVED
- Sep 14, 2026: first solve
- Sep 15, 2026: re-solve (2x total)

MISTAKES
- Sep 15: In pass 2 I multiplied postfix by nums[i] BEFORE multiplying
  res[i] by postfix. Order matters: use the running value first, then update
  it.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("All tests passed")
