# HealthMerge Patient Records Integration

## Problem Statement

HealthMerge Inc. recently acquired CarePlus. Both healthcare providers maintain patient records in linked lists sorted by Social Security Number (SSN).

The objective is to merge two sorted linked lists into a single sorted linked list while preserving all patient records, including duplicates.

Each patient record contains:

- SSN
- Age
- Full Name

The merged list must remain sorted by SSN to ensure efficient access to patient information.

---

## Clarifying Questions

Before implementing the solution, I would ask the following questions:

1. Are both linked lists guaranteed to already be sorted by SSN?
2. Can either linked list be empty?
3. Should duplicate SSNs be preserved if they appear in both lists?
4. Am I allowed to reuse existing nodes, or should I create new nodes?
5. Is SSN the only field used for sorting?

### Assumptions

For this solution, I assume:

- Both linked lists are already sorted.
- Duplicate SSNs should be preserved.
- Existing nodes can be reused.
- SSN is the sorting key.

---

## Solution Approach

The solution uses a two-pointer technique.

1. Compare the current nodes of both linked lists.
2. Select the node with the smaller SSN.
3. Attach that node to the merged list.
4. Move the corresponding pointer forward.
5. Continue until one list becomes empty.
6. Append the remaining nodes from the other list.

This guarantees that the final merged list remains sorted.

---

## Flowchart

<img width="1536" height="1024" alt="flowchart healthcare linked list" src="https://github.com/user-attachments/assets/4de1863a-e525-4b9e-b41a-860df653e3dc" />


The flowchart demonstrates:

- Two sorted input lists
- Comparison of nodes
- Merging process
- Final sorted merged list

---

## Example

### Input

HealthMerge:

111 → 333 → 555

CarePlus:

222 → 444 → 666

### Output

111 → 222 → 333 → 444 → 555 → 666

---

## Test Cases

### Normal Test Case 1

Input:

List 1:

111 → 333 → 555

List 2:

222 → 444 → 666

Expected Output:

111 → 222 → 333 → 444 → 555 → 666

Purpose:

Verifies standard merging behavior.

---

### Normal Test Case 2

Input:

List 1:

100 → 200

List 2:

150 → 250 → 350 → 450

Expected Output:

100 → 150 → 200 → 250 → 350 → 450

Purpose:

Verifies merging when lists have different lengths.

---

### Normal Test Case 3

Input:

List 1:

100 → 200 → 300

List 2:

200 → 300 → 400

Expected Output:

100 → 200 → 200 → 300 → 300 → 400

Purpose:

Verifies duplicate SSNs are preserved.

---

## Edge Cases

### Edge Case 1

Input:

List 1: None

List 2: None

Expected Output:

None

Purpose:

Verifies handling of two empty lists.

---

### Edge Case 2

Input:

List 1: None

List 2: 100 → 200

Expected Output:

100 → 200

Purpose:

Verifies handling when the first list is empty.

---

### Edge Case 3

Input:

List 1: 100 → 200

List 2: None

Expected Output:

100 → 200

Purpose:

Verifies handling when the second list is empty.

---

## Unit Testing

This project uses the Python testing framework pytest.

Run all tests:

```bash
pytest -v
```

Expected output:

```text
test_merge_normal PASSED
test_merge_different_sizes PASSED
test_duplicates PASSED
test_both_empty PASSED
test_first_empty PASSED
test_second_empty PASSED
```

---

## Time Complexity

Each node is visited exactly once.

If:

- n = number of nodes in the first list
- m = number of nodes in the second list

Time Complexity:

O(n + m)

---

## Space Complexity

The algorithm reuses the original linked list nodes and only stores a few pointers.

Space Complexity:

O(1)

---

## Optimization Discussion

### Initial Approach

Create a completely new linked list and copy all nodes.

Complexities:

Time: O(n + m)

Space: O(n + m)

### Optimized Approach

Reuse the existing nodes from the original linked lists.

Complexities:

Time: O(n + m)

Space: O(1)

### Benefit

The optimized solution maintains the same runtime while significantly reducing memory usage.

---

## Project Structure

```text
healthmerge-linked-list/
│
├── merge_lists.py
├── test_merge_lists.py
├── demo.py
├── flowchart.png
└── README.md
```

---

## Running The Program

Run the demonstration:

```bash
python demo.py
```

Run the unit tests:

```bash
pytest -v
```

---

## Conclusion

This solution successfully merges two sorted linked lists representing patient records from HealthMerge and CarePlus. The merged list preserves all records, maintains sorted order by SSN, handles duplicates and edge cases, and achieves efficient performance with O(n + m) time complexity and O(1) auxiliary space complexity.
