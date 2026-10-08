 # Week 2 — Two Pointers + Sliding Window

 ## Day 1 — Valid Palindrome

 ### Problem 1

[solution.py](./01_Basic_two_pointers/problem_1_solution.py)

 ## 🔐 Real-life scenario: Security code verification

 You're building a security system that checks whether a code reads the same from the front and the back.

 For example:

```
LEVEL
```

 reads:

```
L E V E L
```

 from left to right and:

```
L E V E L
```

 from right to left.

 So it is a palindrome.

 But:

```
HELLO
```

 is not.

 Your system should ignore:

 - spaces
- punctuation
- uppercase/lowercase differences

 For example:

```
"A man, a plan, a canal: Panama"
```

 should be considered a palindrome.

---

 ## Your programming version

 Implement:

```
def is_palindrome(s):
    ...
```

 For example:

```
s = "A man, a plan, a canal: Panama"
```

 Expected:

```
True
```

 And:

```
s = "race a car"
```

 Expected:

```
False
```

---

 ## Think before coding

 Don't write Python yet.

 Answer:

 1. If you manually checked whether this is a palindrome, what would you compare?
2. Do you need to start at only one end?
3. What happens if the first and last characters don't match?
4. After comparing the first and last characters, what should happen next?
5. What information do you need to keep track of?
6. Can two pointers represent the two characters you're currently comparing?
7. When should the left pointer move?
8. When should the right pointer move?
9. When should you stop?
10. Can you describe the algorithm in plain English?

 Try to discover:

```
left →                 ← right

compare

left →              ← right

compare

left →          ← right
```

---


 # Day 2 — Two Sum II

 ### Problem 2

[solution.py](./02_Two_pointers_on_sorted_data/problem_2_solution.py)

 ## 🍔 Real-life scenario: Restaurant bill

 You're at a restaurant with a list of menu prices.

 The prices are already sorted:

```
prices = [5, 10, 15, 20, 25, 30]
```

 You have a target budget:

```
target = 35
```

 You need to find **two different items** whose prices add up to exactly RM35.

 For example:

```
5 + 30 = 35
10 + 25 = 35
15 + 20 = 35
```

 Your task is to find one valid pair.

---

 ## Your programming version

 Implement:

```
def two_sum_sorted(prices, target):
    ...
```

 Example:

```
prices = [5, 10, 15, 20, 25, 30]
target = 35
```

 Possible answer:

```
[0, 5]
```

 because:

```
5 + 30 = 35
```

---

 ## ⚠️ Important clue

 The array is **already sorted**.

 That is very important.

 Don't immediately use a HashMap.

 Ask yourself:

 > What information does the sorted order give me?

 Suppose your two numbers are:

```
5 + 30 = 35
```

 What if you instead have:

```
5 + 25 = 30
```

 The sum is too small.

 Should you make the smaller number even smaller?

 Or should you make the larger number bigger?

---

 ## Think before coding

 1. What would brute force do?
2. What is inefficient about brute force?
3. What does the sorted order tell you?
4. Could you start with one pointer at the beginning?
5. Could another pointer start at the end?
6. What should happen if the sum is too small?
7. What should happen if the sum is too large?
8. When should you stop?
9. Why does moving the correct pointer eliminate possibilities?
10. What is the complexity?

 Try to discover:

```
left →                    ← right

sum too small?
      ↓
move left

sum too large?
      ↓
move right
```

---

 # Day 3 — 3Sum

 ### Problem 3

[solution.py](./03_Harder_two_pointers/problem_3_solution.py)


 ## 🍕 Real-life scenario: Restaurant meal combination

 You're building a restaurant promotion system.

 You have a list of meal prices:

```
prices = [-4, -1, -1, 0, 1, 2]
```

 You want to find **three different meals whose prices add up to exactly RM0**.

 For example:

```
-1 + -1 + 2 = 0
```

 and:

```
-1 + 0 + 1 = 0
```

 So the result should contain combinations such as:

```
[-1, -1, 2]
[-1, 0, 1]
```

---

 ## Your programming version

 Implement:

```
def three_sum(nums):
    ...
```

 Example:

```
nums = [-4, -1, -1, 0, 1, 2]
```

 Expected combinations:

```
[
    [-1, -1, 2],
    [-1, 0, 1]
]
```

 The order of the combinations does not matter.





 # Day 4 — Maximum Profit

 ### Problem 4

[solution.py](./04_Introduction_to_maintaining_a_range/problem_4_solution.py)


 ## 📈 Real-life scenario: Buying and selling stocks

 You are building a system that analyzes the daily price of a company's stock.

 You are given the stock price for each day:

```
prices = [7, 1, 5, 3, 6, 4]
```

 You may:

 - buy the stock **once**
- sell the stock **once**
- you must **buy before you sell**

 Your goal is to find the **maximum possible profit**.

 For example:

```
Buy at:  1
Sell at: 6

Profit = 6 - 1 = 5
```

 So the answer is:

```
5
```

---

 ## Your programming version

 Implement:

```
def max_profit(prices):
    ...
```

 Example:

```
prices = [7, 1, 5, 3, 6, 4]
```

 Expected:

```
5
```

 Another example:

```
prices = [7, 6, 4, 3, 1]
```

 Expected:

```
0
```

 Because there is no profitable transaction.

---

 ## ⚠️ Important rule

 You cannot sell before you buy.

 For:

```
prices = [7, 1, 5]
```

 You cannot do:

```
5 - 7
```

 because that would mean selling before buying.

 Your buy day must always be **before** your sell day.

---

 ## Think before coding

 Don't write Python yet.

 Answer these questions first:

 1. If you knew the selling price today, what information from previous days would you need?
2. Do you really need to remember every previous price?
3. What is the most useful piece of information to maintain as you move from left to right?
4. If today's price is higher than the lowest price you've seen, what can you calculate?
5. What should happen if today's price is lower than your current minimum?
6. Should you update the best profit when you find a cheaper buying price?
7. Or should you update it when you find a better selling opportunity?
8. Can you solve this by looking at each price only once?
9. What variables would you need to maintain?
10. What is the time complexity?

---

 ## 🧠 Think in terms of a range

 Imagine scanning the prices from left to right:

```
[7, 1, 5, 3, 6, 4]
       ↑        ↑
      buy     sell
```

 At every point, ask:

```
What is the cheapest price I've seen so far?

What profit would I make if I sold today?
```

 For example:

```
price = 5

minimum so far = 1

possible profit = 5 - 1
                = 4
```

 Then:

```
price = 6

minimum so far = 1

possible profit = 6 - 1
                = 5
```

 So the best profit becomes:

```
5
```


 # Day 5 — Longest Substring Without Repeating Characters

 ### Problem 5

[solution.py](./05_Variable_sliding_window/problem_5_solution.py)

 ## 📱 Real-life scenario: Username validation

 You're building a system that analyzes usernames.

 You want to find the **longest consecutive section containing no repeated characters**.

 For example:

```
"abcabcbb"
```

 contains:

```
"abc"
```

 as its longest substring without repeating characters.

 Its length is:

```
3
```

 Another example:

```
"bbbbb"
```

 has:

```
"b"
```

 so the answer is:

```
1
```

---

 ## Your programming version

 Implement:

```
def longest_unique_substring(s):
    ...
```

 Example:

```
s = "abcabcbb"
```

 Expected:

```
3
```

---

 ## ⚠️ Important

 The characters must be **contiguous**.

 For:

```
"abcabcbb"
```

 you cannot simply pick:

```
a c b
```

 from different positions.

 You need an actual substring.

 Think:

```
[ a b c ]
```

 then:

```
[ a b c a ]
```

 The second window is invalid because `a` appears twice.

---

 ## Think before coding

 This is your first real sliding-window problem.

 Don't code yet.

 Ask:

 1. What exactly is a substring?
2. What makes a window valid?
3. What makes a window invalid?
4. Could you represent the current substring using `left` and `right`?
5. What should happen when you add a character that already exists?
6. Which side of the window should move?
7. What information should you maintain?
8. Could a `set` help?
9. When should you update the maximum length?
10. Can you describe the algorithm without Python?

 Try to visualize:

```
a b c
↑   ↑
L   R
```

 Then:

```
a b c a
↑     ↑
L     R
```

 Invalid.

 So:

```
a b c a
  ↑   ↑
  L   R
```

 Now the window is valid again.

---

 ## 🧠 Your key question

 Whenever you see:

 > **longest/shortest contiguous substring/subarray satisfying a condition**

 ask:

 > **"Can I maintain a window instead of checking every possible substring?"**

 That's the mental trigger I want you to develop.

---

 # Day 6 — Longest Repeating Character Replacement

 ### Problem 6

[solution.py](./06_Frequency-based_sliding_window/problem_6_solution.py)

 ## 🎨 Real-life scenario: Factory label correction

 A factory produces labels using uppercase letters.

 Sometimes labels contain inconsistent characters.

 For example:

```
A A B A
```

 You are allowed to change at most `k` characters.

 Suppose:

```
s = "AABABBA"
k = 1
```

 You can change one character.

 For example:

```
A A B A
```

 Change:

```
B → A
```

 and get:

```
A A A A
```

 So the longest valid section has length:

```
4
```

---

 ## Your programming version

 Implement:

```
def character_replacement(s, k):
    ...
```

 Example:

```
s = "AABABBA"
k = 1
```

 Expected:

```
4
```

---

 ## The important question

 Suppose your current window is:

```
A A B A
```

 You have:

```
3 A's
1 B
```

 The window has:

```
4 characters
```

 The most common character is:

```
A
```

 To make the entire window consist of `A`s, you need to change:

```
1 character
```

 So the window is valid when the number of replacements needed is at most `k`.

---

 ## Think before coding

 Don't look for the solution yet.

 Answer:

 1. What is the window?
2. What makes the window valid?
3. What makes it invalid?
4. How many characters would need to be changed?
5. Which character should you change everything into?
6. Do you need to know the frequency of every character?
7. What information should your frequency dictionary store?
8. What does the most frequent character in the window tell you?
9. When the window becomes invalid, what should happen?
10. When should you update the maximum answer?

 Try to derive:

```
window length
      -
most frequent character count
      =
characters that must be replaced
```

 Then:

```
replacements <= k
        ↓
window valid
```

---


 # Day 7 — Mixed Problem

 ### Problem 7

[solution.py](./07_Mixed_pattern-recognition_problem/problem_7_solution.py)

 # Day 7 — Mixed Problem

### Problem 7

[solution.py](./07_Mixed_pattern-recognition_problem/problem_7_solution.py)

## 🏭 Real-life scenario: Smart Factory Sensor Analysis

A factory monitors the temperature of its machines every minute.

You are given:

temperature = [4, 2, 2, 3, 5, 2, 2, 4, 3]

Each number represents the temperature recorded at one minute.

The factory wants to identify the longest continuous period of readings
that can be considered "stable".

A stable period must satisfy several conditions.

### Rules

1. The temperature difference between the hottest and coldest reading
   must be at most `limit`.

2. No temperature may appear more than `maxFreq` times.

3. You are allowed to remove at most one reading from the period.

4. After removing that reading, the remaining period must satisfy
   all the stability rules.

Your task is to find the maximum length of the original continuous
period that can be made stable.

---

## Your programming version

Implement:

def longest_stable_period(temperature, limit, maxFreq):
    ...

Example:

temperature = [4, 2, 2, 3, 5, 2, 2, 4, 3]
limit = 3
maxFreq = 2

Expected:

???


## Think before coding

Don't write Python yet.

Answer these questions first:

1. What exactly is the "window" in this problem?

2. Is the window fixed-size or variable-size?

3. What makes a window invalid?

4. How can you efficiently know the minimum temperature?

5. How can you efficiently know the maximum temperature?

6. How can you track how many times each temperature appears?

7. What happens when one temperature appears too many times?

8. Could removing one element make an invalid window valid?

9. If the window becomes invalid, which pointer should move?

10. When should you update the maximum answer?

11. What information must be maintained while the window moves?

12. Can you describe the complete algorithm in plain English
    before writing code?

