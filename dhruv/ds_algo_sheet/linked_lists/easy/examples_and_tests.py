"""Linked List Easy - Examples and Tests
Builds diverse linked lists and tests implementations in this folder.
Targets:
- reverse_ll (1_reverse_ll.py)
- middle_of_node (2_middle_of_ll.py)
- detect_cycle (3_detect_a_cycle.py)
 - nth_from_end (4_nth_node_from_end.py)
 - merge_two_sorted_lists (5_merge_two_sorted_ll.py)
 - delete_duplicates_sorted (6_delete_duplicates.py)
 - check_palindrome (7_palindrome_ll.py)
"""

import os
import importlib.util
from node import Node


def build_list(values):
    head = None
    tail = None
    for v in values:
        n = Node(v)
        if head is None:
            head = n
            tail = n
        else:
            tail.next = n
            tail = n
    return head


def to_values(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


def _load_module(basename):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, f"{basename}.py")
    spec = importlib.util.spec_from_file_location(basename, file_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_reverse_ll():
    reverse_mod = _load_module("1_reverse_ll")
    reverse_ll = reverse_mod.reverse_ll

    cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([1, 1, 2, 2, 3], [3, 2, 2, 1, 1]),
        ([0, -1, 2, -3], [-3, 2, -1, 0]),
    ]

    print("\nTesting reverse_ll:")
    for inp, expected in cases:
        head = build_list(inp)
        out_head = reverse_ll(head)
        actual = to_values(out_head)
        print(
            f"in={inp} -> out={actual} expected={expected} ok={actual == expected}")


def test_middle_of_ll():
    mid_mod = _load_module("2_middle_of_ll")
    middle_of_node = mid_mod.middle_of_node

    cases = [
        ([1], 1),
        ([1, 2], 1),  # conventional: first middle for even length
        ([1, 2, 3], 2),
        ([1, 2, 3, 4, 5], 3),
        ([10, 20, 30, 40], 20),
    ]

    print("\nTesting middle_of_node:")
    for inp, expected in cases:
        head = build_list(inp)
        actual = middle_of_node(head)
        print(
            f"in={inp} -> middle={actual} expected={expected} ok={actual == expected}")


def test_nth_from_end():
    nth_mod = _load_module("4_nth_node_from_end")
    nth_from_end = nth_mod.nth_from_end

    print("\nTesting nth_from_end:")

    # Empty list
    head = None
    print(f"empty, n=1 -> {nth_from_end(head, 1)} expected=None")

    # Single element
    head = build_list([42])
    node = nth_from_end(head, 1)
    print(f"[42], n=1 -> {node.val if node else None} expected=42")
    print(f"[42], n=2 -> {nth_from_end(head, 2)} expected=None")

    # Multiple elements
    head = build_list([1, 2, 3, 4, 5])
    for n, expected in [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]:
        node = nth_from_end(head, n)
        print(
            f"[1..5], n={n} -> {node.val if node else None} expected={expected}")

    # n out of bounds
    print(f"[1..5], n=6 -> {nth_from_end(head, 6)} expected=None")

    # Non-positive n
    print(f"[1..5], n=0 -> {nth_from_end(head, 0)} expected=None")
    print(f"[1..5], n=-2 -> {nth_from_end(head, -2)} expected=None")


def test_merge_two_sorted_ll():
    merge_mod = _load_module("5_merge_two_sorted_ll")
    merge_two_sorted_lists = merge_mod.merge_two_sorted_lists

    print("\nTesting merge_two_sorted_lists:")

    def vals(head):
        return to_values(head)

    # Both empty
    print(f"[] + [] -> {vals(merge_two_sorted_lists(None, None))} expected=[]")

    # One empty
    a = build_list([1, 3, 5])
    print(
        f"[1,3,5] + [] -> {vals(merge_two_sorted_lists(a, None))} expected=[1, 3, 5]")

    b = build_list([2, 4, 6])
    print(
        f"[] + [2,4,6] -> {vals(merge_two_sorted_lists(None, b))} expected=[2, 4, 6]")

    # Both non-empty
    a = build_list([1, 3, 5])
    b = build_list([2, 4, 6])
    print(
        f"[1,3,5] + [2,4,6] -> {vals(merge_two_sorted_lists(a, b))} expected=[1, 2, 3, 4, 5, 6]")

    # With duplicates
    a = build_list([1, 2, 2, 3])
    b = build_list([2, 2, 4])
    print(
        f"[1,2,2,3] + [2,2,4] -> {vals(merge_two_sorted_lists(a, b))} expected=[1, 2, 2, 2, 2, 3, 4]")

    # Different lengths
    a = build_list([1, 4, 7])
    b = build_list([2, 3, 5, 6, 8])
    print(
        f"[1,4,7] + [2,3,5,6,8] -> {vals(merge_two_sorted_lists(a, b))} expected=[1, 2, 3, 4, 5, 6, 7, 8]")


def test_delete_duplicates_sorted():
    delete_mod = _load_module("6_delete_duplicates")
    delete_duplicates_sorted = delete_mod.delete_duplicates_sorted

    print("\nTesting delete_duplicates_sorted:")

    def vals(head):
        return to_values(head)

    # Empty list
    print(f"[] -> {vals(delete_duplicates_sorted(None))} expected=[]")

    # Single element
    head = build_list([1])
    print(f"[1] -> {vals(delete_duplicates_sorted(head))} expected=[1]")

    # Two same elements
    head = build_list([1, 1])
    print(f"[1,1] -> {vals(delete_duplicates_sorted(head))} expected=[1]")

    # Two different elements
    head = build_list([1, 2])
    print(f"[1,2] -> {vals(delete_duplicates_sorted(head))} expected=[1, 2]")

    # Duplicates at beginning
    head = build_list([1, 1, 2])
    print(f"[1,1,2] -> {vals(delete_duplicates_sorted(head))} expected=[1, 2]")

    # Duplicates at end
    head = build_list([1, 2, 2])
    print(f"[1,2,2] -> {vals(delete_duplicates_sorted(head))} expected=[1, 2]")

    # Duplicates at both ends
    head = build_list([1, 1, 2, 2])
    print(
        f"[1,1,2,2] -> {vals(delete_duplicates_sorted(head))} expected=[1, 2]")

    # Multiple duplicates
    head = build_list([1, 1, 2, 3, 3])
    print(
        f"[1,1,2,3,3] -> {vals(delete_duplicates_sorted(head))} expected=[1, 2, 3]")

    # No duplicates
    head = build_list([1, 2, 3, 4, 5])
    print(
        f"[1,2,3,4,5] -> {vals(delete_duplicates_sorted(head))} expected=[1, 2, 3, 4, 5]")

    # All same elements
    head = build_list([1, 1, 1, 1])
    print(f"[1,1,1,1] -> {vals(delete_duplicates_sorted(head))} expected=[1]")

    # Complex case with multiple groups
    head = build_list([1, 1, 2, 2, 3, 3, 4, 4])
    print(
        f"[1,1,2,2,3,3,4,4] -> {vals(delete_duplicates_sorted(head))} expected=[1, 2, 3, 4]")

    # Mixed duplicates
    head = build_list([1, 2, 2, 3, 3, 3, 4])
    print(
        f"[1,2,2,3,3,3,4] -> {vals(delete_duplicates_sorted(head))} expected=[1, 2, 3, 4]")


def test_check_palindrome():
    palindrome_mod = _load_module("7_palindrome_ll")
    check_palindrome = palindrome_mod.check_palindrome

    print("\nTesting check_palindrome:")

    # Empty list
    print(f"[] -> {check_palindrome(None)} expected=True")

    # Single element
    head = build_list([1])
    print(f"[1] -> {check_palindrome(head)} expected=True")

    # Two elements - palindrome
    head = build_list([1, 1])
    print(f"[1,1] -> {check_palindrome(head)} expected=True")

    # Two elements - not palindrome
    head = build_list([1, 2])
    print(f"[1,2] -> {check_palindrome(head)} expected=False")

    # Three elements - palindrome
    head = build_list([1, 2, 1])
    print(f"[1,2,1] -> {check_palindrome(head)} expected=True")

    # Three elements - not palindrome
    head = build_list([1, 2, 3])
    print(f"[1,2,3] -> {check_palindrome(head)} expected=False")

    # Four elements - palindrome
    head = build_list([1, 2, 2, 1])
    print(f"[1,2,2,1] -> {check_palindrome(head)} expected=True")

    # Four elements - not palindrome
    head = build_list([1, 2, 3, 4])
    print(f"[1,2,3,4] -> {check_palindrome(head)} expected=False")

    # Five elements - palindrome
    head = build_list([1, 2, 3, 2, 1])
    print(f"[1,2,3,2,1] -> {check_palindrome(head)} expected=True")

    # Five elements - not palindrome
    head = build_list([1, 2, 3, 4, 5])
    print(f"[1,2,3,4,5] -> {check_palindrome(head)} expected=False")

    # Longer palindrome
    head = build_list([1, 2, 3, 4, 5, 4, 3, 2, 1])
    print(f"[1,2,3,4,5,4,3,2,1] -> {check_palindrome(head)} expected=True")

    # Longer not palindrome
    head = build_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"[1,2,3,4,5,6,7,8,9] -> {check_palindrome(head)} expected=False")

    # All same elements
    head = build_list([1, 1, 1, 1])
    print(f"[1,1,1,1] -> {check_palindrome(head)} expected=True")

    # Single different element in middle
    head = build_list([1, 1, 2, 1, 1])
    print(f"[1,1,2,1,1] -> {check_palindrome(head)} expected=True")


if __name__ == "__main__":
    test_reverse_ll()
    test_middle_of_ll()
    test_nth_from_end()
    test_merge_two_sorted_ll()
    test_delete_duplicates_sorted()
    test_check_palindrome()

    # Detect cycle tests
    detect_mod = _load_module("3_detect_a_cycle")
    detect_cycle = detect_mod.detect_cycle

    print("\nTesting detect_cycle:")
    # Case 1: empty list
    head = None
    print(f"empty -> {detect_cycle(head)} expected=False")

    # Case 2: single node no cycle
    a = Node(1)
    print(f"single no cycle -> {detect_cycle(a)} expected=False")

    # Case 3: two nodes no cycle
    a = Node(1)
    b = Node(2)
    a.next = b
    print(f"two no cycle -> {detect_cycle(a)} expected=False")

    # Case 4: simple 2-node cycle
    a = Node(1)
    b = Node(2)
    a.next = b
    b.next = a
    print(f"two cycle -> {detect_cycle(a)} expected=True")

    # Case 5: 3-node cycle at head
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c
    c.next = a
    print(f"cycle at head -> {detect_cycle(a)} expected=True")

    # Case 6: tail connects to middle
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    print(f"tail to middle -> {detect_cycle(a)} expected=True")

    # Case 7: longer acyclic
    head = build_list([1, 2, 3, 4, 5])
    print(f"long acyclic -> {detect_cycle(head)} expected=False")
