"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

It demonstrates both implementations, tests them on multiple datasets
and edge cases, measures performance, and applies sorting to a
real-world example.
"""

import random
import time


def bubble_sort(lst):
    """
    Bubble Sort (iterative, comparison-based).

    Repeatedly steps through the list, compares adjacent elements, and
    swaps them if they are out of order. After each full pass, the
    largest remaining value has "bubbled" to its final position.

    Time:  O(n^2) average/worst, O(n) best (already sorted, thanks to
           the early-exit flag below)
    Space: O(1) extra (sorts the copy in place)

    Returns a NEW sorted list; the original is left unchanged.
    """
    # Work on a copy so the caller's list is not modified
    result = lst[:]
    n = len(result)

    for i in range(n - 1):
        swapped = False  # Tracks whether this pass changed anything

        # The last i elements are already in place, so skip them
        for j in range(n - 1 - i):
            # Compare adjacent elements; swap if out of order
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # If no swaps occurred, the list is already sorted -- stop early
        if not swapped:
            break

    return result


def merge_sort(lst):
    """
    Merge Sort (recursive, divide-and-conquer).

    Divide the list into halves, recursively sort each half, then merge
    the two sorted halves into one sorted list.

    Time:  O(n log n) in best, average, and worst cases
    Space: O(n) extra for the merged lists

    Returns a NEW sorted list; the original is left unchanged.
    """
    # Base case: a list of 0 or 1 elements is already sorted
    if len(lst) <= 1:
        return lst[:]

    # Divide: split the list at the midpoint
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Conquer: recursively sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Combine: merge the two sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Merge two already-sorted lists into one sorted list.

    Uses two index pointers, always taking the smaller front value.
    Using <= when comparing keeps equal values in their original order,
    which makes Merge Sort stable.
    """
    merged = []  # The new sorted result
    i = 0        # Pointer into left
    j = 0        # Pointer into right

    # Compare front values of each list and take the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # One list is exhausted; append whatever remains of the other
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# ----------------------------------------------------------------
# Helper functions for testing and analysis
# ----------------------------------------------------------------

def compare_algorithms(label, data):
    """Sort data with both algorithms, print results, and verify them."""
    snapshot = data[:]  # Saved to confirm the sorts don't modify the input
    bubble_result = bubble_sort(data)
    merge_result = merge_sort(data)
    expected = sorted(data)  # Python's built-in sort, used as a check

    print(f"{label}")
    print(f"  Original:    {data}")
    print(f"  Bubble Sort: {bubble_result}")
    print(f"  Merge Sort:  {merge_result}")
    print(f"  Results match each other: {bubble_result == merge_result}")
    print(f"  Results match sorted():   {bubble_result == expected}")
    print(f"  Original list unchanged:  {data == snapshot}")
    return bubble_result, merge_result


def time_sort(sort_func, data):
    """Return the seconds taken by sort_func to sort data."""
    start = time.perf_counter()
    sort_func(data)
    return time.perf_counter() - start


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # DATASET #1
    # ===============================
    print("\n=== DATASET #1 ===")
    dataset1 = [64, 34, 25, 12, 22, 11, 90, 5]
    compare_algorithms("Dataset #1 (integers):", dataset1)

    # ===============================
    # DATASET #2
    # ===============================
    print("\n=== DATASET #2 ===")
    dataset2 = [88, -3, 47, 0, 19, 73, -15, 56, 31]
    b2, m2 = compare_algorithms("Dataset #2 (includes negatives and zero):", dataset2)
    print("  Comparison: both algorithms produce identical output; they")
    print("  differ only in how much work they do to get there.")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    print("\n1) Empty list")
    compare_algorithms("Empty list:", [])
    print("  Explanation: Bubble Sort's loops never run; Merge Sort hits its")
    print("  base case immediately. Both return an empty list without errors.")

    print("\n2) Single-element list")
    compare_algorithms("Single element:", [42])
    print("  Explanation: A one-item list is already sorted, so both return it as is.")

    print("\n3) Already sorted list")
    compare_algorithms("Already sorted:", [1, 2, 3, 4, 5, 6, 7])
    print("  Explanation: Bubble Sort finishes after ONE pass with no swaps")
    print("  (the early-exit optimization gives O(n)). Merge Sort still")
    print("  splits and merges everything, so it stays O(n log n).")

    print("\n4) Reverse-sorted list")
    compare_algorithms("Reverse sorted:", [7, 6, 5, 4, 3, 2, 1])
    print("  Explanation: This is Bubble Sort's worst case; every comparison")
    print("  triggers a swap (O(n^2)). Merge Sort is unaffected (O(n log n)).")

    print("\n5) List with duplicate values")
    compare_algorithms("Duplicates:", [4, 2, 7, 2, 4, 1, 7, 2])
    print("  Explanation: Both algorithms handle duplicates correctly and are")
    print("  stable, meaning equal values keep their original relative order.")

    # ===============================
    # PERFORMANCE ANALYSIS
    # ===============================
    print("\n=== PERFORMANCE ANALYSIS ===")
    print("Timing both algorithms on random lists (seconds, lower is better):\n")
    print(f"{'Size':>8} {'Bubble Sort':>14} {'Merge Sort':>14} {'Bubble / Merge':>16}")

    random.seed(7)  # Fixed seed so results are repeatable
    for size in [100, 500, 1000, 2000]:
        data = [random.randint(0, 100000) for _ in range(size)]
        t_bubble = time_sort(bubble_sort, data)
        t_merge = time_sort(merge_sort, data)
        ratio = t_bubble / t_merge if t_merge > 0 else float("inf")
        print(f"{size:>8} {t_bubble:>14.6f} {t_merge:>14.6f} {ratio:>15.1f}x")

    print("\nObservation: when the input size doubles, Bubble Sort's time grows")
    print("roughly 4x (quadratic), while Merge Sort's grows a little over 2x")
    print("(n log n). The gap widens rapidly as the list gets larger.")

    # ===============================
    # REAL-WORLD EXAMPLE
    # ===============================
    print("\n=== REAL-WORLD EXAMPLE: ONLINE STORE PRODUCTS ===")
    products = [
        ("Wireless Mouse", 24.99),
        ("Laptop Stand", 39.50),
        ("USB-C Cable", 9.99),
        ("Mechanical Keyboard", 89.00),
        ("Webcam", 49.95),
        ("Desk Lamp", 24.99),
        ("Monitor", 179.00),
    ]

    # Sorting by price: sort the prices, then look up product names.
    # To keep this simple and reuse our algorithms, we sort (price, name)
    # tuples; Python compares the price first, then the name for ties.
    by_price = merge_sort([(price, name) for name, price in products])

    print("Products sorted by price (low to high) using Merge Sort:")
    for price, name in by_price:
        print(f"  ${price:>7.2f}  {name}")

    print("\nWhy Merge Sort here? A real store may have thousands or millions")
    print("of products and re-sorts whenever a shopper changes a filter, so")
    print("the O(n log n) guarantee matters much more than Bubble Sort's")
    print("simplicity. (Equal prices are ordered alphabetically by name.)")


if __name__ == "__main__":
    main()