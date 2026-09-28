# Problem 1

[solution.py](./01_two_sum/problem_1_solution.py)


## Two Sum as a shopping problem. 
You’re at a grocery store with **RM50** to spend on exactly two items.
The prices are:
 ```
 [RM12, RM25, RM38, RM20, RM30]
 ```
You want to find **two different items whose prices add up to exactly RM50**.
For example:
```
RM20 + RM30 = RM50
```
So the answer is the **two items priced RM20 and RM30**.
### Your programming version
Imagine the store gives you:
```
prices = [12, 25, 38, 20, 30]
budget = 50
```
Your job is to find the **positions (indices)** of the two items whose prices add up to `50`.
Don't think about HashMaps yet.
**Question:** If you were standing in the store, how would you manually find the two items?
## The expected result is: [0, 2],[3, 4]






 # Problem 2 — Contains Duplicate
 [solution.py](./02_contains_duplicate/problem_2_solution.py)


 ## 🌍 Real-life scenario: Event check-in

 Imagine you're organizing a conference.

 Every person who enters the building scans their **unique registration ID**:

```
A102
B305
C201
A102
D410
```

 Each registration ID is supposed to belong to **one person**.

 You need to detect whether **the same ID was scanned more than once**.

 For example:

```
A102
B305
C201
A102
D410
```

 `A102` appears twice.

 So the answer is:

```
True
```

 because a duplicate exists.

 But:

```
A102
B305
C201
D410
```

 has no repeated ID:

```
False
```


 ### Your first thinking exercise

 Don't write Python yet.

 Answer these **5 questions**:

 1. If you solved this by brute force, what would you do?
2. What would make that approach slow?
3. While going through the list from left to right, what information would you want to **remember**?
4. What Python data structure is good at answering:
    > "Have I seen this value before?"
5. Can you describe your algorithm in **plain English**, without code?




# Problem 3 - Valid Anagram
[solution.py](./03_valid_anagram/problem_3_solution.py)

## Customer Support Message Matching

 A customer submits a support message, but the system needs to determine whether it contains **exactly the same characters** as a previously flagged message, regardless of:

 - uppercase/lowercase
- spaces
- punctuation
- emojis should **count**
- repeated characters matter

 For example:

```
Message A:
"Refund requested!!!"

Message B:
"requested refund"
```

 These should **not** match because the character counts differ once normalization rules are applied.

 Your task:

 > Write a function that determines whether two customer messages are character-anagrams after removing spaces and punctuation and converting letters to lowercase.

 Example:

```
is_same_message(
    "Dormitory!",
    "Dirty room"
)
```

 Expected:

```
True
```

 ### Think before coding

 Ask yourself:

 1. What exactly should be removed?
2. What should happen to repeated characters?
3. What information do I need to remember while processing the first message?
4. Can I solve it in one pass?
5. What's the time and space complexity?

---


# Problem 4 - Valid Anagram
[solution.py](./03_valid_anagram/problem_4_solution.py)


 ## Warehouse Inventory Reconciliation

 You're building software for a warehouse.

 Two inventory systems produce lists of product IDs for the same shipment. The order doesn't matter, but **the number of times each product appears does**.

 For example:

```
system_a = [
    "SKU-101",
    "SKU-205",
    "SKU-101",
    "SKU-300",
    "SKU-205"
]

system_b = [
    "SKU-205",
    "SKU-101",
    "SKU-205",
    "SKU-300",
    "SKU-101"
]
```

 These represent the same shipment:

```
True
```

 But:

```
system_b = [
    "SKU-205",
    "SKU-101",
    "SKU-300",
    "SKU-300",
    "SKU-101"
]
```

 should produce:

```
False
```

 because `SKU-300` appears twice instead of once, while `SKU-205` is missing.

 ### Your challenge

 Implement:

```
def same_inventory(system_a, system_b):
    ...
```

 **Do not sort the lists.**

 Try to discover the data structure that lets you answer:

 > "How many times have I seen this product?"

 ### Extra challenge

 Can you make it work with:

 - 10 million product IDs
- without creating a second copy of either entire list
- in **O(n)** time?

---



# Problem 5 — Group Anagrams

[solution.py](./04_group_anagrams/solution.py)

## 🍜 Real-life scenario: Restaurant order consolidation

You run the backend system for a food-delivery company.

During a busy dinner period, customers place orders through different devices. Because of a synchronization bug, the same set of dishes can arrive in different orders.

For example:

```python
["rice", "chicken", "egg"]
["egg", "rice", "chicken"]
["chicken", "egg", "rice"]
````

 These are actually the **same combination of dishes**.

 Your job is to group orders that contain exactly the same items, regardless of their order.

 For example:

```
orders = [
    ["rice", "chicken", "egg"],
    ["pizza", "cola"],
    ["egg", "rice", "chicken"],
    ["cola", "pizza"],
    ["burger"],
    ["chicken", "egg", "rice"]
]
```

 The system should group them like this:

```
[
    [
        ["rice", "chicken", "egg"],
        ["egg", "rice", "chicken"],
        ["chicken", "egg", "rice"]
    ],
    [
        ["pizza", "cola"],
        ["cola", "pizza"]
    ],
    [
        ["burger"]
    ]
]
```

 The order of the groups does not matter.

 The order of the orders inside each group also does not matter.

 ## Your programming version

 Implement:

```
def group_orders(orders):
    ...
```

 Each order is a list of dish names.

 For example:

```
orders = [
    ["rice", "chicken", "egg"],
    ["pizza", "cola"],
    ["egg", "rice", "chicken"],
    ["cola", "pizza"],
    ["burger"],
    ["chicken", "egg", "rice"]
]
```

 Your function should return groups of orders containing the same dishes.

 ## ⚠️ Important complication

 A dish can appear **more than once** in an order.

 For example:

```
["rice", "egg", "egg"]
```

 and:

```
["egg", "rice", "egg"]
```

 belong together.

 But:

```
["rice", "egg"]
```

 does not belong in that group.

 So you cannot simply ask:

 > "Which dishes are present?"

 You also need to care about:

 > "How many times does each dish appear?"

 ## Think before coding

 **Don't write Python yet.**

 Answer these questions:

 1. If you solved this by brute force, how would you determine whether two orders belong to the same group?
2. Why would comparing every order with every other order become expensive?
3. What makes these two orders equivalent?

```
["rice", "chicken", "egg"]

["egg", "rice", "chicken"]
```

 4. If the order of dishes doesn't matter, how could you create some kind of **identity** or **signature** for an order?
5. What happens if you simply use a `set` of dishes?

 Would this incorrectly treat these as equal?

```
["egg", "egg", "rice"]

["egg", "rice"]
```

 6. What information must your signature preserve?
7. Imagine you process the orders from left to right. What information should you remember so that you can immediately find the correct group for the next order?
8. What Python data structure could map:

```
"same order signature"
        ↓
"all orders with that signature"
```

 9. Can you describe your complete algorithm in **plain English**, without writing Python?
10. Only after that: what is the time and space complexity?

 

 ## 🔥 Extra challenge

 Suppose there are:

```
10 million orders
```

 and each order contains up to:

```
100 dishes
```

 You want to avoid repeatedly comparing an order against every existing group.

 Can you design a solution where each order is processed independently and then placed into its group using a lookup?

 Before coding, write:

```
Approach:
...

Key observation:
...

Data structure:
...

Why it works:
...

Time complexity:
...

Space complexity:
...

Pseudocode:
...
```

 **Do not look up the Group Anagrams solution yet.**

 Your goal is not to remember the LeetCode solution.

 Your goal is to discover:

 > **"I need a canonical representation for each order, then use that representation to group equivalent orders."**

```




# Problem 5 — Best Time to Buy and Sell Stock

[solution.py](./05_best_time_to_buy_sell_stock/problem_6_solution.py)

## 💰 Real-life scenario: Buying and selling concert tickets

You run a ticket-resale business.

Every morning, you record the price of a concert ticket.

For example:

```python
prices = [120, 95, 80, 110, 150, 130, 170]
````

 The prices represent the ticket price on each day:

```
Day 0 → RM120
Day 1 → RM95
Day 2 → RM80
Day 3 → RM110
Day 4 → RM150
Day 5 → RM130
Day 6 → RM170
```

 You are allowed to:

 1. Buy **one** ticket.
2. Sell that ticket **once**.
3. You must buy before you sell.

 Your goal is to make the **maximum possible profit**.

 For example:

```
Buy on Day 2 → RM80
Sell on Day 6 → RM170

Profit = RM170 - RM80
       = RM90
```

 So the maximum profit is:

```
RM90
```

---

 ## Your programming version

 Implement:

```
def max_profit(prices):
    ...
```

 For example:

```
prices = [120, 95, 80, 110, 150, 130, 170]
```

 Your function should return:

```
90
```

 because:

```
Buy:  RM80
Sell: RM170
Profit: RM90
```

---

 ## ⚠️ Important complication

 You cannot travel backward in time.

 For example:

```
prices = [200, 150, 100, 80, 50]
```

 You might notice:

```
RM200 → RM50
```

 and think:

```
RM200 - RM50 = RM150
```

 But that would require you to:

```
Sell at RM200
then
Buy at RM50
```

 which violates the rules.

 You must always:

```
BUY
 ↓
SELL
```

 So the answer for:

```
prices = [200, 150, 100, 80, 50]
```

 is:

```
0
```

 because there is no profitable transaction.

---

 ## Think before coding

 **Don't write Python yet.**

 Answer these questions:

 1. If you solved this by brute force, what would you try?
2. If you wanted to check every possible transaction, how many pairs might you have to examine?
3. What makes a transaction valid?

 For example:

```
Day 2 → Day 6
```

 is valid, but:

```
Day 6 → Day 2
```

 is not.

 4. While moving from left to right through the prices, what information from the past would be useful?
5. Suppose you are currently looking at:

```
Day 5 → RM130
```

 What would you want to know about the previous days?

 6. If you have already seen:

```
RM120
RM95
RM80
RM110
RM150
```

 which previous price would be most interesting when today's price is:

```
RM130
```

 And why?

 7. Do you actually need to remember **every previous price**, or is there some smaller piece of information that summarizes what you need?
8. Imagine you process prices from left to right.

 What information should you maintain so that, when you see today's price, you can immediately calculate the best possible profit ending today?

 9. Can you describe your complete algorithm in **plain English**, without writing Python?
10. Only after that: what is the time and space complexity?

---

 ## 🧠 Harder challenge

 Don't immediately think:

 > "Find the largest number and subtract the smallest number."

 That isn't always correct.

 Consider:

```
prices = [100, 180, 60, 200]
```

 The smallest price is:

```
RM60
```

 and the largest price is:

```
RM200
```

 But you cannot buy at RM60 and somehow use a price from before it.

 The correct transaction is:

```
Buy  → RM100
Sell → RM200

Profit = RM100
```

 So ask yourself:

 > **How can I keep track of the cheapest valid buying opportunity seen so far?**

 Then ask:

 > **When I see today's price, what profit would I make if I sold today?**

 And finally:

 > **How do I remember the best profit I've seen so far?**

---

 ## 🔥 Extra challenge

 Suppose there are:

```
10 million price records
```

 and you need to process them efficiently.

 You are not allowed to repeatedly compare every price with every other price.

 Can you design a solution where you process each price **once**?

 Try to discover what you need to maintain:

```
Information from the past
        ↓
Today's price
        ↓
Potential profit
        ↓
Best profit so far
```

 Before coding, write:

```
Approach:
...

Key observation:
...

Information I need to remember:
...

Data structure / variables:
...

Why it works:
...

Time complexity:
...

Space complexity:
...

Pseudocode:
...
```

---

 ## 🎯 Final thinking exercise

 Imagine you are manually looking at this:

```
prices = [7, 1, 5, 3, 6, 4]
```

 Walk through it one price at a time.

 Create a table like:

```
Day    Price    Cheapest seen so far    Profit if sold today    Best profit
---    -----    --------------------    ---------------------    -----------
0       7              ?                        ?                    ?
1       1              ?                        ?                    ?
2       5              ?                        ?                    ?
3       3              ?                        ?                    ?
4       6              ?                        ?                    ?
5       4              ?                        ?                    ?
```

 Fill in the table **before writing any code**.

 Then ask yourself:

 > **What does each column represent?**

 If you can explain that clearly, you are very close to discovering the algorithm.

 **Do not look up the Best Time to Buy and Sell Stock solution yet.**

 Your goal is not to remember:

 > "Use this exact code."

 Your goal is to discover the reasoning pattern:

 > **"Keep the best buying opportunity seen so far, calculate today's possible profit, and keep the best profit found so far."**

```

```