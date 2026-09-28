# Unit 7 Discussion: Sorting Algorithms
 
## Overview
 
This assignment compares Bubble Sort and Merge Sort. Both are implemented in
`unit7_discussion.py`, tested on multiple datasets and edge cases, timed on
lists of increasing size, and applied to a real-world example (sorting store
products by price).
 
## Learning Objectives
 
- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency
## Requirements
 
1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.
## How to Run
 
```
python unit7_discussion.py
```
 
The program prints results for two datasets, five edge cases (empty,
single-element, already sorted, reverse sorted, duplicates), a timing table,
and the product-sorting example. Each result is checked against Python's
built-in `sorted()`.
 
## Algorithm Summary
 
| | Bubble Sort | Merge Sort |
|---|---|---|
| Approach | Iterative, swaps adjacent pairs | Recursive, divide and conquer |
| Best case | O(n) with early exit | O(n log n) |
| Average / worst | O(n^2) | O(n log n) |
| Extra space | O(1) | O(n) |
| Stable | Yes | Yes |
 
## Sample Timing Results
 
| Size | Bubble Sort (s) | Merge Sort (s) |
|---|---|---|
| 100 | 0.000236 | 0.000097 |
| 500 | 0.007063 | 0.000640 |
| 1000 | 0.031688 | 0.001335 |
| 2000 | 0.133874 | 0.002923 |
 
(Exact times vary by machine, but the growth pattern is consistent.)
 
## Discussion Board Reflection
 
**1. Concepts and skills learned.** This assignment taught me how two
algorithms can produce identical output while doing very different amounts of
work. I practiced writing Bubble Sort with an early-exit flag, and I saw how
recursion and the merge step make divide-and-conquer work. Timing both
algorithms on growing lists made Big O notation feel concrete.
 
**2. Challenges.** My hardest challenge was the merge step, especially
handling leftover elements once one list ran out. Tracing small lists by hand
and comparing every result to Python's `sorted()` helped me find mistakes. I
also had to remember to copy the list so the original stayed unchanged.
 
**3. Compare and contrast.** Bubble Sort is simple and uses almost no extra
memory, and it finishes in one pass on sorted data. However, it is O(n^2) and
slows dramatically as lists grow. Merge Sort is always O(n log n) and stable,
but it needs O(n) extra space and is harder to write. I would use Bubble Sort
only for tiny lists or teaching, and Merge Sort for large datasets like
sorting store products by price.
