
# Week 4 — Linked Lists & Trees

## Day 1 — Reversing a Linked List

### Problem 1

[solution.py](./01_reverse_linked_list/problem_1_solution.py)

## 🔗 Real-life scenario: Reversing a train

Imagine a train consisting of several carriages connected in a sequence.

```
1 → 2 → 3 → 4 → 5 → None
```

Each carriage points to the next carriage.

You're building a system that reverses the direction of these connections.

After reversing the train, the sequence should become:

```
5 → 4 → 3 → 2 → 1 → None
```

Your task is to reverse the connections without creating an entirely new linked list.

---

## Your programming version

Each node contains a value and a pointer to the next node.

Implement:

```
def reverse_list(head):
    ...
```

Example:

```
Input:  1 → 2 → 3 → None
Output: 3 → 2 → 1 → None
```

Another example:

```
Input:  1 → None
Output: 1 → None
```

If the list is empty, return `None`.

---

## ⚠️ Important clue

Consider three consecutive nodes:

```
1 → 2 → 3 → None
```

To reverse the connection between `1` and `2`, you need to make node `2` point back to node `1`.

But before changing that connection, how will you remember where node `3` is?

Think about maintaining three references:

- The previous node
- The current node
- The next node

The key is to reverse one pointer at a time without losing access to the remaining list.

---

## Think before coding

1. What should the previous node initially be?
2. Which node should you process first?
3. Why must you save the next node before changing a pointer?
4. How do you reverse the current node's `next` pointer?
5. How do you advance the previous and current references?
6. When should the loop stop?
7. Which node becomes the new head?
8. Can you solve it in `O(n)` time and `O(1)` extra space?

---

## Day 2 — Finding the Middle Node

### Problem 2

[solution.py](./02_middle_of_linked_list/problem_2_solution.py)

## 🚆 Real-life scenario: Finding the middle carriage

You're building a system that manages a train with an unknown number of carriages.

```
10 → 20 → 30 → 40 → 50 → None
```

You need to find the middle carriage.

For this example, the answer is:

```
30 → 40 → 50 → None
```

If the train has an even number of carriages, return the second middle node.

For example:

```
10 → 20 → 30 → 40 → None
```

The answer should be:

```
30 → 40 → None
```

---

## Your programming version

Implement:

```
def middle_node(head):
    ...
```

Example:

```
Input:  1 → 2 → 3 → 4 → 5 → None
Output: 3 → 4 → 5 → None
```

Another example:

```
Input:  1 → 2 → 3 → 4 → 5 → 6 → None
Output: 4 → 5 → 6 → None
```

---

## ⚠️ Important clue

You could count all the nodes first and then traverse the list again.

But can you solve the problem using just one traversal?

Imagine two runners:

- A slow runner moves one node at a time.
- A fast runner moves two nodes at a time.

When the fast runner reaches the end, where will the slow runner be?

This technique is called the **fast and slow pointer technique**.

---

## Think before coding

1. Where should both pointers start?
2. How far should each pointer move during one iteration?
3. What happens when the fast pointer reaches the end?
4. Why does the slow pointer reach the middle?
5. How does this work when the list has an even number of nodes?
6. What should happen if the list contains only one node?
7. Can you solve it in `O(n)` time with `O(1)` extra space?

---

## Day 3 — Detecting a Linked List Cycle

### Problem 3

[solution.py](./03_linked_list_cycle/problem_3_solution.py)

## 🔄 Real-life scenario: Detecting an endless route

Imagine a delivery route represented by connected locations.

```
A → B → C → D
        ↑   |
        └───┘
```

The route loops back to a previous location instead of ending.

Your system needs to determine whether the route contains a cycle.

A normal linked list eventually reaches `None`.

A cyclic linked list never reaches `None` when following its `next` pointers.

---

## Your programming version

Implement:

```
def has_cycle(head):
    ...
```

Example:

```
Input:  1 → 2 → 3 → 4
            ↑       |
            └───────┘

Output: True
```

Another example:

```
Input:  1 → 2 → 3 → None

Output: False
```

Return `True` if a cycle exists and `False` otherwise.

---

## ⚠️ Important clue

One approach is to store every visited node in a set.

But that requires additional memory.

Instead, imagine two runners moving through the route:

- One moves one node at a time.
- The other moves two nodes at a time.

If there is a cycle, the faster runner will eventually catch the slower runner.

If the faster runner reaches `None`, there is no cycle.

This is known as **Floyd's cycle detection algorithm**.

---

## Think before coding

1. What should happen if the head is `None`?
2. Why must you check whether the fast pointer and its next node exist?
3. How should the two pointers move?
4. Why will they eventually meet if a cycle exists?
5. What does it mean if the fast pointer reaches `None`?
6. Can two pointers meet outside a cycle?
7. How can you solve this using `O(1)` extra space?
8. What are the time and space complexities?

---

# Day 4 — Maximum Depth of a Binary Tree

### Problem 4

[solution.py](./04_maximum_depth_of_binary_tree/problem_4_solution.py)

## 🌳 Real-life scenario: Measuring an organization hierarchy

You're building an application that displays an organization's reporting structure.

```
        CEO
       /   \
   Manager  Manager
      /
 Employee
```

The depth of a tree is the number of nodes along the longest path from the root to a leaf.

For the example above, the maximum depth is `3`.

Your task is to calculate the maximum depth of any given binary tree.

---

## Your programming version

Implement:

```
def max_depth(root):
    ...
```

Example:

```
Input:

       3
      / \
     9   20
        /  \
       15   7

Output: 3
```

Another example:

```
Input:  1
         \
          2

Output: 2
```

If the tree is empty, return `0`.

---

## ⚠️ Important clue

Instead of calculating the entire tree's depth at once, ask a smaller question:

"What is the maximum depth of the left subtree?"

Then ask:

"What is the maximum depth of the right subtree?"

Once you know both answers, you can calculate the depth of the current node.

Think about this relationship:

```
Depth of current node
          =
1 + maximum of
    /       \
Left depth  Right depth
```

This is an example of **recursive problem decomposition**.

---

## Think before coding

1. What should the function return when `root` is `None`?
2. What is the depth of a leaf node?
3. How can the function calculate the left subtree's depth?
4. How can it calculate the right subtree's depth?
5. Why do you add `1`?
6. Why do you use `max()`?
7. What does `max_depth(node)` mean at every recursive call?
8. What is the time complexity?
9. What is the auxiliary space complexity in terms of tree height?

---

# Day 5 — Inverting a Binary Tree

### Problem 5

[solution.py](./05_invert_binary_tree/problem_5_solution.py)

## 🪞 Real-life scenario: Mirroring a family tree

You're building a visual application that displays a binary tree.

The user wants to create a mirror image of the entire tree.

Original tree:

```
        4
       / \
      2   7
     / \ / \
    1  3 6  9
```

After inversion:

```
        4
       / \
      7   2
     / \ / \
    9  6 3  1
```

Every node must have its left and right children swapped.

---

## Your programming version

Implement:

```
def invert_tree(root):
    ...
```

Example:

```
Input:

    2
   / \
  1   3

Output:

    2
   / \
  3   1
```

Return the root of the inverted tree.

---

## ⚠️ Important clue

You don't need to rebuild the entire tree.

At every node, consider swapping its left and right child references.

Then ask:

"Have I inverted the subtrees below this node?"

If not, you still need to process them.

A recursive solution can invert each subtree and return the current node.

---

## Think before coding

1. What should happen when the current node is `None`?
2. How can you swap the left and right children?
3. Should you invert the children before or after swapping them?
4. What should the function return?
5. Why does processing every node eventually invert the whole tree?
6. What happens when the tree contains only one node?
7. Can you solve it recursively in `O(n)` time?
8. What is the auxiliary space complexity in terms of tree height?

---

# Day 6 — Checking Whether Two Trees Are Identical

### Problem 6

[solution.py](./06_same_tree/problem_6_solution.py)

## 🌲 Real-life scenario: Comparing two file structures

You're building a system that compares two hierarchical file structures.

Each node contains a value, and each node can have a left and right child.

Two trees are identical only if:

- Both have the same structure.
- Corresponding nodes contain the same values.

For example:

```
Tree A:       Tree B:

    1             1
   / \           / \
  2   3         2   3
```

These trees are identical.

But:

```
Tree A:       Tree B:

    1             1
   /               \
  2                 2
```

These trees are not identical because their structures differ.

---

## Your programming version

Implement:

```
def is_same_tree(p, q):
    ...
```

Example:

```
Tree A:  [1, 2, 3]
Tree B:  [1, 2, 3]

Output: True
```

Another example:

```
Tree A:  [1, 2]
Tree B:  [1, None, 2]

Output: False
```

Return `True` if both trees are identical, otherwise return `False`.

---

## ⚠️ Important clue

You need to compare both trees at the same time.

Start by considering these cases:

- Both nodes are `None`.
- Only one node is `None`.
- Both nodes exist but have different values.
- Both nodes exist and have equal values.

If the current nodes match, what should you check next?

The answer involves comparing both pairs of children recursively.

---

## Think before coding

1. What should happen if both nodes are `None`?
2. What if only one node is `None`?
3. How do you compare the current node values?
4. Why must both left subtrees match?
5. Why must both right subtrees match?
6. Can you combine these conditions with `and`?
7. What should the function return if any comparison fails?
8. What are the time and auxiliary space complexities?

---

# Day 7 — Binary Tree Level Order Traversal

### Problem 7

[solution.py](./07_binary_tree_level_order_traversal/problem_7_solution.py)


## 🏢 Real-life scenario: Processing employees by management level

You're building an employee directory for a company.

The company hierarchy is represented as a binary tree.

```
          CEO
         /   \
     Manager  Manager
       / \       \
    Staff Staff  Staff
```

The application must display employees level by level.

Expected order:

```
[
    ["CEO"],
    ["Manager", "Manager"],
    ["Staff", "Staff", "Staff"]
]
```

You must process all employees at one level before moving to the next.

---

## Your programming version

Implement:

```
def level_order(root):
    ...
```

Example:

```
Input:

       3
      / \
     9   20
        /  \
       15   7

Output:

[[3], [9, 20], [15, 7]]
```

If the tree is empty, return an empty list:

```
[]
```

---

## ⚠️ Important clue

A recursive DFS solution is useful for many tree problems, but this problem specifically requires level-by-level processing.

Imagine a queue at a service counter.

The first person to enter the queue is the first person served.

You can use a Python queue to process nodes in the order they are discovered.

For each level:

1. Record how many nodes are currently in the queue.
2. Process exactly that many nodes.
3. Add their children to the queue.
4. Store the current level's values.
5. Continue until the queue is empty.

Python's `collections.deque` is a good choice for implementing the queue efficiently.

---

## Think before coding

1. What should happen if the root is `None`?
2. Which data structure supports first-in, first-out processing?
3. How do you add the root to the queue?
4. How can you identify how many nodes belong to the current level?
5. Why must you process only the queue's current size for each level?
6. When should you add the left and right children?
7. Why should you use `deque.popleft()` rather than `list.pop(0)`?
8. When should you append the current level to the final result?
9. Why is the time complexity `O(n)`?
10. What is the space complexity?

---
