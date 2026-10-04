"""
1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/

Difficulty:  Easy
Pattern:     Two Pointers (exhaust both, no condition)
LeetCode 75: yes
Confidence:  4/5
Solved:      2x  (first 2026-09-11, last 2026-09-15)

Time:  O(m + n)
Space: O(m + n)

Key insight:
    Nothing to compare here, just alternate word1, word2, so I'm building a new
    list and nothing gets overwritten. Use a list + "".join() because strings
    are immutable.

    Main loop: while both words have characters, append one from each and move
    BOTH pointers.
    Cleanup: when one word runs out, append what's left of the other (only one
    of the cleanup loops actually runs). Can also just do res.append(word1[i:]).

    Time: every character is appended exactly once -> O(m + n).
    Space: res holds m + n characters; i and j are O(1).

Mistakes log:
    - 2026-09-15: Returned res as a list of chars. Have to return "".join(res).
"""

from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # TODO: paste my solution
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.mergeAlternately("abc", "pqr") == "apbqcr"
    assert s.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert s.mergeAlternately("abcd", "pq") == "apbqcd"
    print("All tests passed")
