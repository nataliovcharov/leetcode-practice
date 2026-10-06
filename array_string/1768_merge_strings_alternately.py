"""
1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/
Difficulty: Easy | Confidence: 4/5
Time: O(m + n) | Space: O(m + n)
Pattern: Two Pointers (exhaust both, no condition)

KEY INSIGHT
Nothing to compare here, just alternate word1, word2, so I'm building a new
list and nothing gets overwritten. Use a list + "".join() because strings
are immutable.

Main loop: while both words have characters, append one from each and move
BOTH pointers.
Cleanup: when one word runs out, append what's left of the other (only one
of the cleanup loops actually runs). Can also just do res.append(word1[i:]).

Time: every character is appended exactly once -> O(m + n).
Space: res holds m + n characters; i and j are O(1).

SOLVED
- Sep 11, 2026: first solve
- Sep 15, 2026: re-solve (2x total)

MISTAKES
- Sep 15: Returned res as a list of chars. Have to return "".join(res).
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
