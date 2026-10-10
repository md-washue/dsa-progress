### Problem 1
[solution.py](./01_Basic_stack/problem_1_solution.py)

## 🧮 Real-life scenario: Document structure validation

You're building a document editor that checks whether brackets in a document are correctly opened and closed.

For example:

```
()
[]{}
{[()]}
```

These are valid because every opening bracket has a matching closing bracket in the correct order.

But:

```
([)]
(((
{[}]
```

These are invalid.

Your system must support three types of brackets:

- `()`
- `[]`
- `{}`

---

## Your programming version

Implement:

```
def is_valid(s):
    ...
```

For example:

```
s = "{[()]}"
```

Expected:

```
True
```

And:

```
s = "([)]"
```

Expected:

```
False
```

---

## ⚠️ Important clue

Imagine opening several brackets while writing a document.

```
{
  [
    (
```

Which bracket must you close first?

The most recently opened bracket must be closed first.

This is the same principle used by a **stack**.

---

## Think before coding

Don't write Python yet.

Answer:

1. What would a brute-force approach try to do?
2. Why isn't counting opening and closing brackets enough?
3. What information should you store when you encounter an opening bracket?
4. When you encounter a closing bracket, what should you check?
5. Why must the most recently opened bracket be checked first?
6. What should happen if a closing bracket appears when the stack is empty?
7. What should happen if the stack still contains brackets at the end?
8. Which Python list operations could implement a stack?
9. When should the function return `False`?
10. What is the time and space complexity?

Try to discover:

```
Opening bracket
       ↓
Push onto stack
       ↓
Closing bracket
       ↓
Check the top of stack
       ↓
Matching? ── Yes → Pop
       │
       No
       ↓
     Invalid
```

---

# Day 2 — Browser Back Button

### Problem 2

[solution.py](./02_Stack_operations/problem_2_solution.py)

## 🌐 Real-life scenario: Browser navigation history

You're building a simple browser that records the websites a user visits.

For example:

```
history = [
    "google.com",
    "youtube.com",
    "github.com"
]
```

The user is currently on:

```
github.com
```

When they press the Back button, they should return to:

```
youtube.com
```

Pressing Back again should take them to:

```
google.com
```

If there are no previous pages, pressing Back should return `None`.

---

## Your programming version

Implement:

```
def browser_back(history):
    ...
```

Example:

```
history = [
    "google.com",
    "youtube.com",
    "github.com"
]
```

Expected result:

```
"github.com"
```

The function should remove the page being left from the history, so the next Back operation returns `"youtube.com"`.

For an empty history, return `None`.

---

## ⚠️ Important clue

When a user visits a new page, that page is added to the history.

When the user presses Back, the most recently visited page is removed.

Ask yourself:

> Which Python list operation adds an item to the end, and which operation removes the last item?

---

## Think before coding

1. What does each item in the history represent?
2. Which page is the most recently visited?
3. What should happen when the user presses Back?
4. Why is removing the first item incorrect?
5. Which stack operations would you use?
6. What should happen when the history is empty?
7. How would you support repeated Back operations?
8. What is the time complexity of a single Back operation?
9. How would you distinguish browser history from a normal queue?
10. Can you explain the algorithm in plain English?

Try to discover:

```
Visit Google
     ↓
Visit YouTube
     ↓
Visit GitHub
     ↓
Press Back
     ↓
Remove GitHub
     ↓
Return YouTube
```

---

# Day 3 — Next Greater Temperature

### Problem 3

[solution.py](./03_Monotonic_stack/problem_3_solution.py)

## 🌤️ Real-life scenario: Weather forecasting

You're building a weather application that records the daily temperature.

```
temperatures = [30, 32, 31, 35, 34, 36]
```

For every day, you want to calculate how many days the user must wait until a warmer temperature occurs.

For example:

- Day 1: `30°C` — wait 1 day for `32°C`.
- Day 2: `32°C` — wait 2 days for `35°C`.
- Day 3: `31°C` — wait 1 day for `35°C`.
- Day 4: `35°C` — wait 2 days for `36°C`.
- Day 5: `34°C` — wait 1 day for `36°C`.
- Day 6: `36°C` — no warmer day exists.

---

## Your programming version

Implement:

```
def daily_temperatures(temperatures):
    ...
```

Example:

```
temperatures = [30, 32, 31, 35, 34, 36]
```

Expected:

```
[1, 2, 1, 2, 1, 0]
```

If no warmer temperature occurs later, return `0` for that day.

---

## ⚠️ Important clue

A straightforward solution would examine every future day for each temperature.

That can take `O(n²)` time.

But consider this situation:

```
Day 1: 30°C
Day 2: 32°C
Day 3: 31°C
Day 4: 35°C
```

When you reach Day 4, the temperature is warmer than all three earlier temperatures.

You can resolve multiple earlier days at once.

Ask yourself:

> Can I keep track of earlier days whose warmer temperature has not yet been found?

This is where a **monotonic stack** becomes useful.

---

## Think before coding

1. What does the output at each index represent?
2. Why is checking every future day inefficient?
3. What information must you remember about an unresolved day?
4. Should the stack store temperatures, indices, or both?
5. What happens when the current temperature is warmer than the temperature at the top of the stack?
6. Why might one current temperature resolve several earlier days?
7. When should you stop removing items from the stack?
8. What should happen to days remaining in the stack after the loop?
9. Why is the total time complexity `O(n)`, even though there is a `while` loop inside a loop?
10. What is the space complexity?

Try to discover:

```
Earlier unresolved days
          ↓
New temperature arrives
          ↓
Is it warmer than the top?
          ↓
        Yes
          ↓
Resolve that earlier day
          ↓
Repeat until no longer warmer
```

---

# Day 4 — Finding a Product in a Warehouse

### Problem 4

[solution.py](./04_Basic_binary_search/problem_4_solution.py)

## 📦 Real-life scenario: Warehouse inventory lookup

You're building an inventory system for a warehouse.

The warehouse stores product IDs in ascending order:

```
product_ids = [101, 108, 115, 123, 140, 155, 170]
```

A worker needs to find a product with ID `140`.

Your program should return its index.

If the product does not exist, return `-1`.

---

## Your programming version

Implement:

```
def search_product(product_ids, target):
    ...
```

Example:

```
product_ids = [101, 108, 115, 123, 140, 155, 170]

search_product(product_ids, 140)
```

Expected:

```
4
```

Another example:

```
search_product(product_ids, 130)
```

Expected:

```
-1
```

---

## ⚠️ Important clue

The product IDs are **already sorted**.

A straightforward approach checks each product until it finds the target.

But imagine a warehouse with one million products.

You could instead check the middle product first.

```
[101, 108, 115, 123, 140, 155, 170]
                 ↑
               Middle
```

If the target is `140` and the middle value is `123`, what can you conclude?

Because the list is sorted, you can eliminate part of the search space.

---

## Think before coding

1. What would a linear search do?
2. Why is sorted order useful?
3. Where should the left pointer start?
4. Where should the right pointer start?
5. How do you calculate the middle index?
6. What should happen if the middle value equals the target?
7. What should happen if the middle value is smaller than the target?
8. What should happen if the middle value is larger than the target?
9. When should the loop stop?
10. Why is binary search `O(log n)` instead of `O(n)`?

Try to discover:

```
Left                    Right
  ↓                       ↓
[101, 108, 115, 123, 140, 155, 170]
                 ↑
               Middle

Target > Middle
      ↓
Discard left half
      ↓
Search remaining half
```

---

# Day 5 — Finding the First Available Appointment

### Problem 5

[solution.py](./05_Binary_search_boundaries/problem_5_solution.py\)

## 📅 Real-life scenario: Appointment scheduling

You're building an appointment system for a clinic.

The clinic records whether each time slot is available.

```
slots = [False, False, False, True, True, True]
```

Here:

- `False` means the slot is unavailable.
- `True` means the slot is available.

The slots are arranged in chronological order, and once availability becomes `True`, all later slots are also available.

Your task is to find the **index of the first available slot**.

---

## Your programming version

Implement:

```
def first_available_slot(slots):
    ...
```

Example:

```
slots = [False, False, False, True, True, True]
```

Expected:

```
3
```

Another example:

```
slots = [False, False, False, False]
```

Expected:

```
-1
```

And:

```
slots = [True, True, True]
```

Expected:

```
0
```

---

## ⚠️ Important clue

This is not simply a question of finding a value.

You need to find the **boundary** between unavailable and available slots.

```
False False False True True True
                  ↑
           First available
```

Because the values follow a predictable order, binary search can help you locate that boundary efficiently.

---

## Think before coding

1. What would a linear search do?
2. What makes the array suitable for binary search?
3. If the middle slot is available, could an earlier available slot still exist?
4. If the middle slot is unavailable, what can you conclude about earlier slots?
5. Should you immediately return when you find `True`?
6. How can you continue searching for an earlier available slot?
7. What should you return if no available slot exists?
8. How can you handle the case where the first slot is available?
9. What is the time complexity?
10. How is finding a boundary different from finding any matching value?

Try to discover:

```
False False False True True True
                  ↑
              Available

Could there be an earlier True?
          ↓
Search the left half
```

---

# Day 6 — Minimum Delivery Capacity

### Problem 6

[solution.py](./06_Binary_search_on_answer/problem_6_solution.py)

## 🚚 Real-life scenario: Delivery truck capacity

You're managing a delivery company.

Packages must be delivered within a specified number of days. Each package has a weight, and packages must be loaded in their original order.

For example:

```
weights = [3, 2, 2, 4, 1, 4]
days = 3
```

The truck has a maximum weight capacity.

If the next package would exceed that capacity, it must be delivered on the next day.

Your task is to find the **minimum truck capacity** that allows all packages to be delivered within the given number of days.

---

## Your programming version

Implement:

```
def min_capacity(weights, days):
    ...
```

Example:

```
weights = [3, 2, 2, 4, 1, 4]
days = 3
```

Expected:

```
6
```

One possible arrangement with capacity `6` is:

```
Day 1: [3, 2]       Total = 5
Day 2: [2, 4]       Total = 6
Day 3: [1, 4]       Total = 5
```

A capacity of `5` cannot complete the deliveries in only three days.

---

## ⚠️ Important clue

You don't know the answer in advance, but you can test a possible capacity.

For example:

```
Capacity = 4
Capacity = 6
Capacity = 10
```

For each capacity, determine how many days are required.

Notice the pattern:

- If a capacity works, any larger capacity also works.
- If a capacity fails, any smaller capacity also fails.

This creates a **monotonic condition**, which is a powerful signal for binary search on the answer.

---

## Think before coding

1. What is the smallest possible capacity?
2. What is the largest capacity you would ever need?
3. How would you calculate the number of days needed for a given capacity?
4. What happens when adding the next package exceeds the capacity?
5. How can you decide whether a capacity is valid?
6. If a capacity is valid, should you search for a larger or smaller one?
7. If a capacity is invalid, which direction should you search?
8. How can you avoid checking every possible capacity?
9. Why does the monotonic property make binary search possible?
10. What is the overall time complexity?

Try to discover:

```
Possible capacities
        ↓
Test middle capacity
        ↓
Can all packages be delivered in time?
        ↓
    Yes       No
     ↓         ↓
Try smaller  Try larger
capacity     capacity
        ↓
Find the minimum valid capacity
```

---

# Day 7 — Mixed Problem: Smart Warehouse Monitoring

### Problem 7

[solution.py](./07_Mixed_pattern_recognition/problem_7_solution.py)

## 🏭 Real-life scenario: Warehouse temperature monitoring

You're building a monitoring system for a warehouse.

A sensor records the temperature every minute:

```
temperatures = [30, 32, 31, 35, 34, 36, 33]
```

The monitoring system needs to answer two questions:

1. For each minute, how many minutes must pass until the temperature is higher than the current reading?
2. What is the earliest minute when the temperature reaches or exceeds a target temperature?

For example, the target temperature is:

```
target = 34
```

The first temperature that reaches or exceeds `34` is at index `3`, where the reading is `35`.

However, there is a catch: **the temperature readings are not sorted**, so you cannot directly apply binary search to the original list.

Your job is to implement both operations correctly.

---

## Your programming version

Implement:

```
def next_warmer_period(temperatures):
    ...

def first_temperature_at_least(temperatures, target):
    ...
```

Example:

```
temperatures = [30, 32, 31, 35, 34, 36, 33]

next_warmer_period(temperatures)
```

Expected:

```
[1, 2, 1, 2, 1, 0, 0]
```

For the second function:

```
first_temperature_at_least(temperatures, 34)
```

Expected:

```
3
```

Return `-1` if no temperature reaches the target.

---

## ⚠️ Important clue

These two tasks look similar because both analyze temperatures, but their underlying patterns are different.

- The first task asks you to find the next greater value for every position.
- The second task asks you to find the first qualifying position in the original sequence.

The first is suitable for a **monotonic stack**.

The second cannot use ordinary binary search on the original unsorted list. You must reason about how to find the earliest qualifying position without assuming sorted order.

---

## Think before coding

Don't write Python yet.

Answer these questions first:

1. What does each output index represent?
2. Which task requires remembering unresolved earlier temperatures?
3. How can a monotonic stack avoid repeatedly scanning future temperatures?
4. Why can't ordinary binary search be applied directly to the unsorted list?
5. Could you find the earliest qualifying index by scanning from left to right?
6. What is the time complexity of that straightforward approach?
7. Could you sort the temperatures first? Would that preserve the original earliest index?
8. What information must you maintain to preserve the original order?
9. Which problem can be solved in `O(n)` time using a stack?
10. Can you identify the correct technique for each task before writing any code?

---

