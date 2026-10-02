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

---

 ## Think before coding

 Don't jump directly to three nested loops.

 Start with brute force.

 Ask:

 1. How would you check every possible combination?
2. What would the complexity be?
3. Is there repeated work?
4. What if you sorted the array first?
5. Suppose you choose the first number.
6. What problem remains?
7. Does the remaining problem look familiar?
8. Can the two-pointer technique from Day 2 help?
9. How do you avoid returning the same combination multiple times?
10. Why does sorting help with duplicates?

 Try to discover this progression:

```
3 numbers
    ↓
fix one number
    ↓
find two numbers
    ↓
Two Sum
    ↓
Two Pointers
```

---

 ## 🔥 Important lesson

 Don't memorize:

 > "3Sum = sorting + two pointers."

 Instead understand:

 > **"I can reduce a bigger problem into a smaller problem I already understand."**

 That's much more valuable.

---

 # Day 4 — Maximum Profit

 ### Problem 4

[solution.py](./04_Introduction_to_maintaining_a_range/problem_4_solution.py)

 ## 💰 Real-life scenario: Concert ticket resale

 You record the price of a concert ticket every day:

```
prices = [120, 95, 80, 110, 150, 130, 170]
```

 You can:

 1. Buy once.
2. Sell once.
3. You must buy before selling.

 Your goal is to find the maximum possible profit.

 For example:

```
Buy:  RM80
Sell: RM170

Profit = RM90
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
prices = [120, 95, 80, 110, 150, 130, 170]
```

 Expected:

```
90
```

---

 ## Think before coding

 1. What would brute force do?
2. How many possible buy/sell combinations are there?
3. Why can't you simply find the smallest and largest numbers?
4. Why is this invalid?

```
[200, 100, 50, 300]
```

 5. While moving from left to right, what information about the past matters?
6. When you see today's price, what previous price would you most like to know?
7. Do you really need to remember every previous price?
8. Can you keep only the cheapest valid price so far?
9. How would you calculate today's possible profit?
10. How would you remember the best profit?

 Try to discover:

```
past prices
     ↓
cheapest price so far
     ↓
today's price
     ↓
today's profit
     ↓
best profit so far
```


---

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

 ## 🚚 Real-life scenario: Delivery route monitoring

 You work on the backend system for a food-delivery company.

 A driver's GPS system records the driver's distance from the restaurant at each checkpoint:

```
distances = [2, 5, 3, 7, 8, 4, 9]
```

 You want to detect whether the driver ever moved **back toward the restaurant**.

 For example:

```
2 → 5 → 3
```

 The driver reached:

```
5 km
```

 and then moved back to:

```
3 km
```

 So the answer is:

```
True
```

---

 ## Your programming version

 Implement:

```
def route_moved_backward(distances):
    ...
```

 Example:

```
distances = [2, 5, 3, 7, 8, 4, 9]
```

 Expected:

```
True
```

 But:

```
distances = [2, 3, 5, 6, 8, 10]
```

 should return:

```
False
```

---

 ## ⚠️ Important complication

 You are **not** looking for the largest distance.

 You're checking whether the current value is smaller than the value immediately before it.

 For example:

```
[2, 10, 3]
```

 returns:

```
True
```

 because:

```
10 → 3
```

 is a decrease.

 And:

```
[10, 2, 3]
```

 also returns:

```
True
```

 because:

```
10 → 2
```

 is a decrease.

---

 ## Think before coding

 This is your **mixed problem**.

 I don't want to tell you the pattern.

 Ask yourself:

 1. What exactly am I looking for?
2. Does the problem involve a contiguous range?
3. Do I need two pointers?
4. Do I need a sliding window?
5. Do I need a HashMap?
6. Do I need to remember everything I've seen?
7. Or do I only need a small amount of information from the previous position?
8. What would brute force look like?
9. Can I solve it with one pass?
10. What is the complexity?

 The important part is **not the difficulty of this problem**.

 The important part is that you decide:

 > **What pattern does this problem require?**

 before writing code.

---



 > "I solved 7 problems."

 Measure yourself by:

 > **"When I see a new problem, can I explain what information I need to maintain before I write code?"**

 By Day 7, I want your thought process to start becoming:

```
New problem
     ↓
What is being asked?
     ↓
What does brute force do?
     ↓
What work repeats?
     ↓
What information can I maintain?
     ↓
Two pointers?
Sliding window?
HashMap?
Something else?
     ↓
Algorithm in English
     ↓
Code
```

 That is the transition from **"I know Python"** to **"I can solve problems with Python."**