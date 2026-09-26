# Problem 1: API Replay Attack & Duplicate Webhook Detector

You are building a security middleware layer for a payment processing API. When a client sends a payment request, your server logs the arrival timestamp (in seconds) and a unique cryptographic hash of the request payload. 

Sometimes, due to poor mobile network connections—or a malicious replay attack—the exact same request payload is sent multiple times. 

## Rules
1. If a `payload_hash` arrives, and the **exact same `payload_hash`** was already seen within the last `k` seconds (meaning `current_timestamp - last_seen_timestamp <= k`), this request is flagged as a **Duplicate Replay**.
2. Every time a request arrives (whether it is valid or a duplicate), you must update its `last_seen_timestamp` to the current timestamp.
3. To prevent your security dashboard from being spammed if an attacker replays the same packet 500 times in a row, your function must return a list of **unique flagged `payload_hash` strings**, ordered by the exact moment each hash was **first flagged** as a duplicate.

## Function Signature
```python
def detect_replays(logs: list[tuple[int, str]], k: int) -> list[str]:
```

## Examples

**Example 1:**
```python
logs = [
    (10, "req_A"),
    (12, "req_B"),
    (14, "req_A"),  # 14 - 10 = 4 <= 5 -> FLAGGED ("req_A")
    (16, "req_A"),  # 16 - 14 = 2 <= 5 -> Replay again, but "req_A" is already in our alert list
    (20, "req_B"),  # 20 - 12 = 8 > 5  -> Valid (outside 5s window). Update last seen to 20
    (23, "req_B"),  # 23 - 20 = 3 <= 5 -> FLAGGED ("req_B")
    (25, "req_C")
]
k = 5

# Output: ["req_A", "req_B"]
```

**Example 2:**
```python
logs = [
    (1, "tx_99"),
    (10, "tx_99"),
    (20, "tx_99")
]
k = 3

# Output: []
```

## Constraints
- `1 <= len(logs) <= 100,000` (Must run in $O(n)$ time).
- `logs` are sorted in chronological (non-decreasing) order by timestamp.


<br>


# Problem 2: Out-of-Order UDP Packet Stream Reconstruction

When data is transmitted over UDP, network packets travel through different routers and arrive out of order. Some packets are duplicated along the way, and others are dropped entirely.

Your network interface card captures an unsorted array of integer `seq_numbers` representing the sequence IDs of packets currently sitting in the receive buffer. You need to find the **longest contiguous block of sequence numbers** (where each packet ID is consecutive: $x, x+1, x+2, \dots, y$) that can be reassembled from the buffer.

## Rules
1. Duplicate sequence numbers in the buffer do not break a contiguous sequence, nor do they extend its length (e.g., `[10, 11, 11, 12]` represents the contiguous sequence `10` to `12` of length `3`).
2. Return a tuple of three integers: `(start_seq, end_seq, length)` representing the starting packet ID, ending packet ID, and total unique packets in the longest contiguous stream. (If `seq_numbers` is empty, return `(0, 0, 0)`).
3. If there is a tie between two contiguous streams of the exact same maximum length, return the one with the **smaller `start_seq`**.
4. **Constraint:** You are **not allowed to sort the array** (`O(n log n)`). Your algorithm must run in **$O(n)$ average time**.

## Function Signature
```python
def longest_packet_stream(seq_numbers: list[int]) -> tuple[int, int, int]:
```

## Examples

**Example 1:**
```python
seq_numbers = [104, 4, 200, 1, 3, 2, 105, 2, 103]

# Output: (1, 4, 4)
# Explanation: Streams are [1, 2, 3, 4] (length 4), [103, 104, 105] (length 3), and [200] (length 1).
```

**Example 2:**
```python
seq_numbers = [50, 51, 52, 10, 11, 12, 99]

# Output: (10, 12, 3)
# Explanation: Both [10, 11, 12] and [50, 51, 52] have length 3, so the smaller start_seq (10) wins.
```