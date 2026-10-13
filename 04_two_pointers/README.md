Writing

# Day 1 — Finding Two Students Who Match a Target Score

### Problem 1

[solution.py](./01_two_sum_ii/problem_1_solution.py)

## 🎓 Real-life scenario: Finding two students with matching scores

This question is part of **Two Pointers**, not binary search.

You're building a school system that helps teachers find two students whose scores add up to a target score.

The scores are already sorted in ascending order:

```
scores = [1, 3, 4, 6, 8, 11]
```

The teacher wants to find two scores that add up to:

```
target = 10
```

Your program should return the indices of the two scores.

For example:

```
4 + 6 = 10
```

The values `4` and `6` are at indices `2` and `3` using zero-based indexing.

---

## Your programming version

Implement:

```
def two_sum(scores, target):
    ...
```

Example:

```
scores = [1, 3, 4, 6, 8, 11]
target = 10
```

Expected:

```
[2, 3]
```

Assume exactly one valid pair exists.

---

## ⚠️ Important clue

You could check every possible pair of scores, but that would take `O(n²)` time.

Instead, start with two pointers:

```
Left                       Right
  ↓                           ↓
[1, 3, 4, 6, 8, 11]
```

Calculate the sum of the values at both pointers.

- If the sum is too small, move the left pointer to the right.
- If the sum is too large, move the right pointer to the left.
- If the sum matches the target, return the indices.

Because the array is sorted, you can eliminate possibilities without checking every pair.

## Think before coding

1. Where should the left pointer start?
2. Where should the right pointer start?
3. What should happen if the sum is smaller than the target?
4. What should happen if the sum is larger than the target?
5. When should the function return the answer?
6. Why does this approach take `O(n)` time?
7. What is the space complexity?

---

# Day 2 — Checking Whether a Message Is a Palindrome

### Problem 2

[solution.py](./02_valid_palindrome/problem_2_solution.py)

## 💬 Real-life scenario: Text validation

This question is part of **Two Pointers**, not binary search.

You're building a text-validation feature that checks whether a word reads the same forward and backward.

For example:

```
racecar
level
madam
```

These are palindromes.

But:

```
hello
python
world
```

These are not.

Your program should ignore capitalization, spaces, and punctuation.

---

## Your programming version

Implement:

```
def is_palindrome(text):
    ...
```

Example:

```
text = "A man, a plan, a canal: Panama"
```

Expected:

```
True
```

Another example:

```
text = "hello"
```

Expected:

```
False
```

An empty string or a string containing only non-alphanumeric characters should return `True`.

---

## ⚠️ Important clue

Imagine checking a word from both ends:

```
Left                  Right
  ↓                      ↓
r  a  c  e  c  a  r
```

Compare the leftmost and rightmost characters.

If they match, move both pointers inward.

If they don't match, the string is not a palindrome.

Remember to skip spaces and punctuation.

For an efficient solution, avoid creating a completely cleaned copy of the string.

## Think before coding

1. Where should both pointers start?
2. How can you check whether a character is alphanumeric?
3. What should happen when the left character is a space or punctuation?
4. What should happen when the right character is a space or punctuation?
5. What should happen when the two characters are different?
6. When should the loop stop?
7. Why is the time complexity `O(n)`?
8. What is the space complexity?

---

# Day 3 — Removing Duplicate Product IDs

### Problem 3

[solution.py](./03_remove_duplicates_from_sorted_array/problem_3_solution.py)

## 📦 Real-life scenario: Cleaning warehouse inventory

This question is part of **Two Pointers**, not binary search.

You're building an inventory system for a warehouse. Product IDs are stored in ascending order, but some IDs appear multiple times.

For example:

```
product_ids = [1, 1, 2, 2, 3, 4, 4]
```

Your task is to remove the duplicates without creating another array.

The final unique values should be:

```
[1, 2, 3, 4]
```

You must modify the original array in place.

---

## Your programming version

Implement:

```
def remove_duplicates(product_ids):
    ...
```

Example:

```
product_ids = [1, 1, 2, 2, 3, 4, 4]
```

Expected:

```
4
```

The function returns the number of unique elements.

After the function runs, the first four positions of the array should contain:

```
[1, 2, 3, 4]
```

The values beyond those four positions do not matter.

---

## ⚠️ Important clue

Imagine that one pointer scans the array while another tracks where the next unique value should be placed.

```
[1, 1, 2, 2, 3, 4, 4]
    ↑
  Scanner
  ↑
 Writer
```

The first value is already unique.

When the scanning pointer encounters a value different from the previous unique value, copy it to the next available position.

This allows you to remove duplicates without creating a new list.

## Think before coding

1. Why does the array need to be sorted?
2. Where should the scanning pointer start?
3. Where should the writing pointer start?
4. How can you tell whether a value is a duplicate?
5. When should the writing pointer move?
6. Why can you overwrite elements in the original array?
7. What should the function return?
8. Why is the time complexity `O(n)`?
9. What is the extra space complexity?

---

# Day 4 — Finding Two Houses Within a Budget

### Problem 4

[solution.py](./04_two_houses_within_budget/problem_4_solution.py)
## 🏠 Real-life scenario: Choosing two houses within a budget

This question is part of **Two Pointers**, not binary search.

You're helping someone choose two houses from a list of prices sorted from cheapest to most expensive.

For example:

```
prices = [100, 200, 300, 400, 500]
```

The buyer has a budget of:

```
budget = 700
```

They want to choose two houses whose combined price is as large as possible without exceeding their budget.

For this example:

```
200 + 500 = 700
```

This exactly matches the budget.

---

## Your programming version

Implement:

```
def best_house_pair(prices, budget):
    ...
```

Example:

```
prices = [100, 200, 300, 400, 500]
budget = 700
```

Expected:

```
[200, 500]
```

Assume at least one valid pair exists.

Return the two prices in ascending order.

---

## ⚠️ Important clue

Start with the cheapest and most expensive houses:

```
Left                    Right
  ↓                        ↓
[100, 200, 300, 400, 500]
```

Calculate their combined price.

If the sum exceeds the budget, the most expensive house cannot form a valid pair with any house to its left, so move the right pointer left.

If the sum is within budget, record the pair if it improves the best result, then move the left pointer right to explore a potentially more expensive pair.

Continue until the pointers meet.

## Think before coding

1. Why is the sorted order important?
2. Where should the two pointers start?
3. What happens when the sum exceeds the budget?
4. What happens when the sum is within the budget?
5. How do you remember the best pair found so far?
6. When should the loop stop?
7. Why is checking every pair inefficient?
8. What is the time complexity?
9. What is the space complexity?

---

# Day 5 — Matching Delivery Packages to Truck Capacity

### Problem 5

[solution.py](./05_maximum_package_pairs/problem_5_solution.py)

## 🚚 Real-life scenario: Pairing packages for delivery

This question is part of **Two Pointers**, not binary search.

You're managing a delivery company that needs to pair packages for transport.

Each package has a weight, and the weights are sorted in ascending order.

For example:

```
weights = [1, 2, 3, 4, 5, 6]
```

The maximum combined weight for two packages is:

```
limit = 7
```

Each package can be used only once.

Your task is to find the maximum number of pairs that can be formed without exceeding the weight limit.

For example:

```
(1, 6)
(2, 5)
(3, 4)
```

All three pairs satisfy the limit.

---

## Your programming version

Implement:

```
def max_package_pairs(weights, limit):
    ...
```

Example:

```
weights = [1, 2, 3, 4, 5, 6]
limit = 7
```

Expected:

```
3
```

If no pair can be formed, return `0`.

---

## ⚠️ Important clue

Start with the lightest and heaviest remaining packages.

```
Lightest                  Heaviest
   ↓                         ↓
[1, 2, 3, 4, 5, 6]
```

If their combined weight is within the limit, pair them and move both pointers inward.

If their combined weight exceeds the limit, the heaviest package cannot fit with any remaining package because all other packages are at least as heavy as the lightest one.

Set the heaviest package aside by moving the right pointer left.

Repeat until the pointers meet.

## Think before coding

1. Why does sorting the package weights help?
2. Where should the two pointers start?
3. When can you form a pair?
4. What should happen when the combined weight exceeds the limit?
5. Why can you safely set aside the heaviest package when the pair is too heavy?
6. When should the pair counter increase?
7. Can a package be used more than once?
8. What is the time complexity?
9. What is the space complexity?

---

# Day 6 — Comparing Customer Lists

### Problem 6

[solution.py](./06_intersection_of_two_sorted_arrays/problem_6_solution.py)

## 👥 Real-life scenario: Finding customers in two marketing lists

This question is part of **Two Pointers**, not binary search.

You're building a marketing system that combines customer information from two departments.

Both departments have customer IDs sorted in ascending order.

For example:

```
team_a = [1, 2, 2, 3, 5, 8]
team_b = [2, 2, 3, 4, 8, 8]
```

You need to find the customer IDs that appear in both lists.

Each customer ID should appear only once in the result.

For these lists, the common IDs are:

```
[2, 3, 8]
```

---

## Your programming version

Implement:

```
def common_customers(team_a, team_b):
    ...
```

Example:

```
team_a = [1, 2, 2, 3, 5, 8]
team_b = [2, 2, 3, 4, 8, 8]
```

Expected:

```
[2, 3, 8]
```

If there are no common customer IDs, return an empty list:

```
[]
```

---

## ⚠️ Important clue

Use one pointer for each list.

```
Team A: [1, 2, 2, 3, 5, 8]
          ↑

Team B: [2, 2, 3, 4, 8, 8]
         ↑
```

Compare the values at the two pointers.

- If the values are equal, add that ID to the result if it has not already been added, then advance both pointers past that value.
- If the value in the first list is smaller, advance the first pointer.
- If the value in the second list is smaller, advance the second pointer.

Since both lists are sorted, you never need to move a pointer backward.

## Think before coding

1. Why should each list have its own pointer?
2. What happens when both values match?
3. What happens when the value in the first list is smaller?
4. What happens when the value in the second list is smaller?
5. How can you prevent duplicate IDs in the result?
6. What happens when one pointer reaches the end of its list?
7. Why is this more efficient than checking every value against every other value?
8. If the lists have lengths `n` and `m`, what is the time complexity?
9. What is the space complexity, excluding the output list?

---

# Day 7 — Finding the Maximum Water Container

### Problem 7

[solution.py](./07_container_with_most_water/problem_7_solution.py)

## 🌊 Real-life scenario: Designing a water-storage container

This question is part of **Two Pointers**, not binary search.

You're helping an engineer design a water-storage system using vertical barriers of different heights.

The heights of the barriers are represented by an array:

```
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```

Each barrier is positioned one unit apart from the next barrier.

The engineer wants to select two barriers that can hold the largest possible amount of water between them.

The area of water that can fit between two barriers is calculated using:

```
area = min(height_left, height_right) * (right - left)
```

For the example above, the maximum area is:

```
49
```

This comes from the barriers with heights `8` and `7`, which are seven units apart.

---

## Your programming version

Implement:

```
def max_water(heights):
    ...
```

Example:

```
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```

Expected:

```
49
```

Assume the array contains at least two positive integers.

---

## ⚠️ Important clue

Start with the two barriers that are farthest apart.

```
Left                              Right
  ↓                                  ↓
[1, 8, 6, 2, 5, 4, 8, 3, 7]
```

Calculate the area between them.

The amount of water is limited by the shorter barrier, not the taller one.

After calculating the area, move the pointer at the shorter barrier inward.

Why?

Moving the taller barrier inward reduces the width without improving the limiting height. Moving the shorter barrier gives you a chance to find a taller barrier that might produce a larger area.

Keep track of the maximum area until the pointers meet.

## Think before coding

1. Where should the left and right pointers start?
2. How do you calculate the width between the barriers?
3. Why does the shorter barrier determine the water height?
4. How do you calculate the area?
5. What should you store as the current maximum?
6. Which pointer should move after calculating the area?
7. What happens when both barriers have the same height?
8. Why does this algorithm avoid checking every possible pair?
9. Why is the time complexity `O(n)`?
10. What is the space complexity?

Try to discover:

```
Choose the widest container
          ↓
Calculate its area
          ↓
Update the maximum area
          ↓
Which barrier is shorter?
          ↓
Move the shorter barrier inward
          ↓
Repeat until the pointers meet
```

---

