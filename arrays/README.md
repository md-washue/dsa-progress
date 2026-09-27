# Problem 1

[solution.py](./two_sum/problem_1_solution.py)

**Two Sum as a shopping problem**. 
### Real-life Two Sum problem
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
 [solution.py](./contains_duplicate/problem_2_solution.py)


 ### 🌍 Real-life scenario: Event check-in

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

---

 ## Now translate it to a programming problem

 Given a list of numbers:

```
nums = [1, 2, 3, 1]
```

 return `True` if **any value appears more than once**.

 Examples:

```
[1, 2, 3, 1]       → True
[1, 2, 3, 4]       → False
[1, 1]             → True
[5, 7, 5, 9, 2]    → True
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

 Give me your answers. I'll guide you from there without giving you the solution immediately.