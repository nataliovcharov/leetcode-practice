# LeetCode 75

My solutions and notes as I work through the [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/) study plan,
plus extra problems when I want to go deeper on a pattern.

Solutions are organized by **pattern**. Every file has a header with the link, complexity,
my key insight, and a log of mistakes I made, plus the problem's examples as tests at the bottom.

**Progress:** 23 problems logged (19 from LeetCode 75, 4 extra)

## Running a solution

```bash
python3 prefix_sum/0724_find_pivot_index.py
```

Prints `All tests passed` if the examples pass.

## Tracker

Confidence is 1-5. `LC75` is ✓ for study-plan problems and blank for extra practice.

### Array / String

| # | Problem | Difficulty | Pattern | LC75 | Confidence | Solved | Last solved | Code |
|---|---|---|---|:-:|:-:|:-:|---|---|
| 1768 | [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | Easy | Two Pointers (exhaust both, no condition) | ✓ | 4 | 2x | 2026-09-15 | [py](array_string/1768_merge_strings_alternately.py) |
| 1071 | [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | Easy | Array / String - Math (GCD) | ✓ | 3 | 2x | 2026-09-15 | [py](array_string/1071_greatest_common_divisor_of_strings.py) |
| 1431 | [Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) | Easy | Array / String | ✓ | 5 | 2x | 2026-09-15 | [py](array_string/1431_kids_with_the_greatest_number_of_candies.py) |
| 605 | [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/) | Easy | Array / String - Greedy | ✓ | 4 | 2x | 2026-09-15 | [py](array_string/0605_can_place_flowers.py) |
| 345 | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) | Easy | Two Pointers (opposite ends) | ✓ | 5 | 2x | 2026-09-15 | [py](array_string/0345_reverse_vowels_of_a_string.py) |
| 151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | Medium | Built-ins / Two Pointers (anchor + scanner, from back) | ✓ | 5 / 3 | 2x | 2026-09-15 | [py](array_string/0151_reverse_words_in_a_string.py) |
| 334 | [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | Medium | Array / String - Greedy | ✓ | 3 | 2x | 2026-09-15 | [py](array_string/0334_increasing_triplet_subsequence.py) |
| 443 | [String Compression](https://leetcode.com/problems/string-compression/) | Medium | Two Pointers (anchor + scanner, plus a write pointer) | ✓ | 3 | 1x | 2026-09-15 | [py](array_string/0443_string_compression.py) |

### Two Pointers

| # | Problem | Difficulty | Pattern | LC75 | Confidence | Solved | Last solved | Code |
|---|---|---|---|:-:|:-:|:-:|---|---|
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | Two Pointers (exhaust both, from the back) |  | 4 | 1x | 2026-09-10 | [py](two_pointers/0088_merge_sorted_array.py) |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | Two Pointers (both start at the beginning) | ✓ | 3 | 3x | 2026-09-21 | [py](two_pointers/0283_move_zeroes.py) |
| 392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Easy | Two Pointers (both start at the beginning) | ✓ | 5 | 2x | 2026-09-21 | [py](two_pointers/0392_is_subsequence.py) |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Two Pointers (opposite ends, move the shorter wall) | ✓ | 4 | 2x | 2026-09-21 | [py](two_pointers/0011_container_with_most_water.py) |
| 1679 | [Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) | Medium | Two Pointers (sort, then opposite ends) | ✓ | 4 | 2x | 2026-09-21 | [py](two_pointers/1679_max_number_of_k_sum_pairs.py) |

### Sliding Window

| # | Problem | Difficulty | Pattern | LC75 | Confidence | Solved | Last solved | Code |
|---|---|---|---|:-:|:-:|:-:|---|---|
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | Sliding Window (fixed size) | ✓ | 3 | 3x | 2026-09-24 | [py](sliding_window/0643_maximum_average_subarray_i.py) |
| 1456 | [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Medium | Sliding Window (fixed size) | ✓ | 3 | 3x | 2026-09-24 | [py](sliding_window/1456_maximum_number_of_vowels_in_a_substring_of_given_length.py) |
| 1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | Sliding Window (dynamic) | ✓ | 3 | 3x | 2026-09-24 | [py](sliding_window/1004_max_consecutive_ones_iii.py) |
| 1493 | [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | Medium | Sliding Window (dynamic) | ✓ | 3 | 3x | 2026-09-24 | [py](sliding_window/1493_longest_subarray_of_1s_after_deleting_one_element.py) |

### Prefix Sum

| # | Problem | Difficulty | Pattern | LC75 | Confidence | Solved | Last solved | Code |
|---|---|---|---|:-:|:-:|:-:|---|---|
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Prefix Sum (prefix x postfix product) | ✓ | 4 | 2x | 2026-09-15 | [py](prefix_sum/0238_product_of_array_except_self.py) |
| 1732 | [Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/) | Easy | Prefix Sum | ✓ | 5 | 2x | 2026-09-24 | [py](prefix_sum/1732_find_the_highest_altitude.py) |
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy | Prefix Sum | ✓ | 3 | 2x | 2026-09-24 | [py](prefix_sum/0724_find_pivot_index.py) |
| 303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | Prefix Sum |  | 4 | 1x | 2026-10-01 | [py](prefix_sum/0303_range_sum_query_immutable.py) |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Prefix Sum + Hashmap |  | 3 | 2x | 2026-09-24 | [py](prefix_sum/0560_subarray_sum_equals_k.py) |
| 525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Medium | Prefix Sum + Hashmap |  | 3 | in progress | - | [py](prefix_sum/0525_contiguous_array.py) |

## Commit conventions

- New problem: `Add 0525 contiguous-array (prefix sum)`
- Re-solve: `Re-solve 0605 can-place-flowers (forgot to mark planted spot)`
- Notes only: `Update notes 0560 subarray-sum-equals-k`
