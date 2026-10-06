"""
1094. Car Pooling  (extra, not LeetCode 75)
https://leetcode.com/problems/car-pooling/
Difficulty: Medium | Confidence: 2/5
Time: O(n + 1001) | Space: O(1001) (fixed size, stops go up to 1000)
Pattern: Prefix Sum - Difference Array

KEY INSIGHT
Think like a bus driver: don't count every seat at every stop, just note the
CHANGES. For each trip:
    change[start] += passengers   (get on)
    change[end]   -= passengers   (get off; the seat is free AT end)
Then drive the route with a running total; if it ever exceeds capacity,
return False.

The running total of the changes rebuilds how many people are in the car at
every stop (it's a prefix sum, same as 1732, where gain = change).

Brute force = for each trip, add passengers to every stop from start to
end - 1 (inner loop over a whole range). The difference array replaces that
inner loop with 2 marks.

Prefix sum = READ ranges fast. Difference array = WRITE ranges fast.
If positions were huge (up to 10^9), sort the events (sweep line) or use
sort + min-heap instead, O(n log n).

SOLVED
- Oct 6, 2026: first solve, with a step-by-step walkthrough (drew the change row by hand)

MISTAKES
- Oct 6: Didn't know how to start the brute force. What helped: draw the
  stops as a row, fill in 'people in car' for one trip, then write only the
  CHANGES, then a running total over the changes gives back 'people in car'.
"""

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        change = [0] * 1001

        for passengers, start, end in trips:
            change[start] += passengers      # get on
            change[end] -= passengers        # get off (seat is free AT end)

        in_car = 0
        for c in change:
            in_car += c
            if in_car > capacity:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.carPooling([[2, 1, 5], [3, 3, 7]], 4) is False
    assert s.carPooling([[2, 1, 5], [3, 3, 7]], 5) is True
    print("All tests passed")
