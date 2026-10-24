def reverse_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next  # Remember the next node
        current.next = prev       # Reverse the arrow
        prev = current            # Move prev forward
        current = next_node       # Move current forward

    return prev


