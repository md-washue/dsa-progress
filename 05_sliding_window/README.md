
# Day 1 - Woman analyzing sales report on laptop, managing small business operations in retail store

## 1. Best 7-Day Sales Period

[Solution.py](./01_best_7_day_sales_period/problem_1_solution.py)

Pattern: Fixed-size sliding window

A shop records its daily sales. The manager wants to know which consecutive 7-day period generated the highest total sales.

Question: Given a list of daily sales and an integer `k`, find the maximum total sales over any `k` consecutive days.

Example

python
```
sales = [120, 200, 150, 300, 250, 100, 180, 400]
k = 3

# Output: 700
# Best 3-day window: [150, 300, 250]
# Maximum total sales: 150 + 300 + 250 = 700
```

Requirements

- Return the maximum sum of any `k` consecutive elements.
- Aim for $O(n)$ time, not $O(nk)$.
- Handle `k = 1` and `k = len(sales)`.

Hint: Calculate the first window's sum, then subtract the outgoing value and add the incoming value.

# Day 2- Chronotropic incompetence: when your heart rate does not rise adequately during exertion – People & Health

## 2. Longest Healthy Activity Period

[Solution.py](./02_longest_healthy_activity_period/problem_2_solution.py)

Pattern: Variable-size window

A fitness app records the number of active minutes per hour. A user wants the longest consecutive period whose total active minutes do not exceed a daily energy budget.

Question: Given a list of non-negative activity values and a budget `limit`, find the maximum length of a contiguous window whose sum is at most `limit`.

Example

python
```
activity = [10, 20, 15, 5, 10, 10]
limit = 30

# Output: 3
# [5, 10, 10] has sum 25
```

Requirements

- Return the longest valid window length.
- Solve in $O(n)$ time.
- Consider what happens when one value exceeds the limit.

Hint: Expand the right pointer; while the sum exceeds the limit, move the left pointer forward.


# Day 3- Longest Customer Session 
## 3. Longest Customer Session With at Most K Products

[Solution.py](./03_longest_customer_session/problem_3_solution.py)

Pattern: Variable-size window + frequency dictionary

An online store tracks product categories viewed during a customer's session. The business wants to find the longest consecutive sequence containing no more than `k` distinct product categories.

Question: Find the longest contiguous subarray with at most `k` distinct values.

Example

python
```
products = ["shoe", "bag", "shoe", "hat", "bag", "bag"]
k = 2

# Output: 3
# Longest valid windows:
# ["shoe", "bag", "shoe"] = 3
# ["hat", "bag", "bag"] = 3
```

Requirements

- Return the maximum window length.
- Maintain a frequency dictionary as the window changes.
- Remove a category from the dictionary when its count reaches zero.

Hint: The window is valid while the number of keys in the frequency dictionary is at most `k`.

# Day 4 - IT-Sicherheit im Mittelstand: Der vollständige Leitfaden 2025

## 4. Detect Repeated Login Attempts

[Solution.py](./04_detect_repeated_login_attempts/problem_4_solution.py)


Pattern: Fixed-size window + set

A security system stores usernames from the last few login attempts. It needs to determine whether any `k` consecutive attempts contain a repeated username.

Question: Given a list of usernames and an integer `k`, determine whether any window of exactly `k` consecutive attempts contains a duplicate username.

Example

python
```
logins = ["amy", "bob", "carl", "bob", "dina"]
k = 4

# Output: True
# ["amy", "bob", "carl", "bob"] has a duplicate.
```

Requirements

- Return `True` if any window contains duplicates; otherwise return `False`.
- Target $O(n)$ time.
- Do not rebuild a new set for every window.

Hint: Track the current window's values and update membership when elements enter or leave.

# Day 5- 10 tips to save on groceries — OnPoint

## 5. Shortest Shopping Segment to Reach a Budget

[Solution.py](./05_shortest_shopping_segment/problem_5_solution.py)

Pattern: Minimum-length variable-size window

A shopper adds item prices to a shopping list in a particular order. They want the shortest consecutive segment whose total cost is at least their target budget.

Question: Given positive item prices and a target `target`, return the minimum length of a contiguous subarray with sum at least `target`. Return `0` if no such segment exists.

Example

python
```
prices = [2, 3, 1, 2, 4, 3]
target = 7

# Output: 2
# [4, 3] totals 7
```

Requirements

- Return the minimum valid window length.
- Solve in $O(n)$ time.
- Handle cases where the entire list is too small to reach the target.

Hint: Whenever the sum reaches the target, record the length and try shrinking the window from the left.

# Day 6- From Zero to AI-Powered Developer: Your Complete Claude Code CLI Setup Guide - DEV Community

## 6. Find a Keyword in a Live Text Stream

[Solution.py](./06_find_keyword_anagrams/problem_6_solution.py)

Pattern: Fixed-size window + character frequencies

A search engine receives a long string of text and needs to find every starting position where a substring is an anagram of a given keyword.

Question: Given strings `text` and `pattern`, return all starting indices of substrings of `text` that contain exactly the same characters, including their frequencies, as `pattern`.

Example

python
```
text = "cbaebabacd"
pattern = "abc"

# Output: [0, 6]
# "cba" at index 0
# "bac" at index 6
```

Requirements

- Return every matching starting index.
- Target $O(n + m)$ time, where `n` and `m` are the string lengths.
- Account for repeated characters in the pattern.

Hint: Compare character frequencies for a fixed-size window. For a more advanced solution, update a running match count instead of comparing whole dictionaries each time.

# Day 7- CRO Readiness Assessment: A Complete Guide 

## 7. Longest Website Visit Sequence After Two Changes

[Solution.py](./07_longest_website_visit_sequence/problem_7_solution.py)

Pattern: Variable-size window + frequency counting + maximum frequency

A website records whether visitors clicked one of two buttons, represented by `"A"` and `"B"`. You can change at most `k` recorded outcomes in one consecutive segment to make every outcome in that segment the same.

Question: Find the maximum length of a contiguous segment that can be made identical by changing at most `k` characters.

Example

python
```
visits = "AABABBA"
k = 1

# Output: 4
# "AABA" can become "AAAA" with one change.
```

Requirements

- Return the maximum possible segment length.
- Solve in $O(n)$ time.
- Track the frequency of each character and the maximum frequency in the window.

Hint: A window is valid when `window_length - max_frequency <= k`. Decide how to maintain `max_frequency` efficiently as the window moves.

## Coverage checklist

These seven problems cover the major sliding window techniques you'll encounter in interviews.

| Problem | Core technique | Main skill |
| --- | --- | --- |
| 1 | Fixed-size window | Running sum |
| 2 | Variable-size window | Expand and shrink |
| 3 | Variable-size window | Frequency dictionary |
| 4 | Fixed-size window | Set and duplicate detection |
| 5 | Minimum-size window | Optimize window length |
| 6 | Fixed-size string window | Character frequencies |
| 7 | Variable-size string window | Frequency optimization |

## How to practice

For each problem, follow this routine:

1. Brute force first. Write the simplest correct solution, even if it's $O(n^2)$.
2. Identify the window. Decide what enters, what leaves, and what makes the window valid.
3. Optimize. Aim for $O(n)$ time whenever possible.
4. Test edge cases. Try empty input, one element, repeated values, and the smallest valid window.
5. Explain your solution. Be able to explain why moving the left pointer never skips a better answer.

One important distinction: the sum-based variable-window problems above assume non-negative or positive numbers. With arbitrary negative numbers, the same shrinking-window logic is not generally valid.

My recommendation: Solve these in order, without looking up solutions. Start with Question 1 and move on only when you can explain both the code and its time complexity.