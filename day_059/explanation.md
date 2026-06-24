# Combination Sum — Code Review & Fix

## The Original Code

```python
class Solution:
    def targetSumComb(self, arr, target):
        combination = []
        combinations = []
        self.backtracker(arr, target, combination, combinations, 0)
        return combinations

    def backtracker(self, arr, target, combination, combinations, index):
        for i in range(index, len(arr)):
            integer = arr[i]
            if sum(combination)+integer==target:
                combination.append(integer)
                combination.sort()
                if combination not in combinations:
                    combinations.append(list(combination))
                combination.pop()
            elif sum(combination)+integer<target:
                combination.append(integer)
                self.backtracker(arr, target, combination, combinations, i)
                combination.pop()
            else:
                pass
```

---

## What the Original Code Got Right

### 1. Backtracking skeleton
The core structure is correct — explore a candidate, recurse, then undo (append → recurse → pop). This is textbook backtracking.

### 2. Iterating from `index`, not `0`
Passing `i` (not `i+1`) as the new index correctly allows the **same element to be reused** (since combination sum allows repetition), while still preventing going *backwards* in the array and generating reversed duplicates.

### 3. Snapshot on append
```python
combinations.append(list(combination))
```
Taking a copy before appending is correct. Without `list()`, you'd only store a reference to the same mutable list, which would reflect future mutations — every stored combination would end up identical by the end.

---

## What the Original Code Got Wrong

### 1. Sorting mid-recursion mutates shared state

```python
combination.sort()
```

`combination` is a **single shared list** passed by reference down the entire call stack. Sorting it mid-recursion scrambles the order of elements that the current recursive path depends on. The path through the backtracking tree is encoded in the sequence of elements in `combination` — mutating that ordering breaks the traversal.

### 2. The deduplication strategy was treating a symptom, not the cause

The reason `combination.sort()` + `if combination not in combinations` was added was to handle potential duplicate combinations. But the real question is: *why would duplicates occur at all?*

Duplicates occur when the **input array is unsorted**. For example, with `arr = [3, 1, 2]` and `target = 3`:
- One path picks `[3]`
- Another picks `[1, 2]`
- Another picks `[2, 1]` ← duplicate of `[1, 2]`, different order

Sorting the combination before checking was a patch over this. The root cause is that without a sorted input, different traversal paths can produce the same multiset in different orders.

### 3. `pass` instead of `break` wastes work

```python
else:
    pass
```

When `sum(combination) + integer > target`, the code does nothing and continues to the next element. But if `arr` were sorted, every subsequent element would also overshoot. The correct move is to `break` early and prune the rest of the branch.

---

## What the Fix Does

### 1. Sort the input once upfront

```python
arr.sort()
```

This single line makes duplicate combinations **structurally impossible to generate**. Since `arr` is sorted and we always iterate `from index`, every element added to `combination` is ≥ the previous one. Every valid path through the tree is uniquely determined — no two paths can produce the same multiset in a different order.

This eliminates the need for mid-recursion sorting and the existence check entirely.

### 2. Remove mid-recursion sort and dedup check

With a sorted input and `from index` traversal, combinations are always built in non-decreasing order by construction. There is no way for two different paths to produce the same combination. The check is not just redundant — it's an indicator of a misdiagnosed problem.

### 3. Use `break` for early pruning

```python
else:
    break
```

Since `arr` is sorted, once an element causes the sum to exceed the target, all subsequent elements will too. Breaking here prunes the remaining branch entirely, reducing unnecessary iterations.

---

## The Fixed Version

```python
class Solution:
    def targetSumComb(self, arr, target):
        arr.sort()  # guarantees non-decreasing order, makes duplicates structurally impossible
        combinations = []
        self.backtracker(arr, target, [], combinations, 0)
        return combinations

    def backtracker(self, arr, target, combination, combinations, index):
        for i in range(index, len(arr)):
            integer = arr[i]
            current_sum = sum(combination) + integer
            if current_sum == target:
                combinations.append(combination + [integer])  # snapshot for storage only
                # no need to pop because we didnt actually modify the orignal combination list in the above line, we created a new modified list instead
            elif current_sum < target:
                combination.append(integer)
                self.backtracker(arr, target, combination, combinations, i)
                combination.pop()  # undo — backtrack to explore next branch
            else:
                break  # arr is sorted, all further elements will also exceed target
```

The append/pop pattern is preserved around the recursive call — this is the correct, memory-efficient backtracking idiom. One shared list is mutated in place and cleaned up as the tree unwinds, costing `O(d)` space where `d` is the recursion depth.

The only place a new list is created is on the `==` branch — `combination + [integer]` — but that is not for recursion, it's purely to take a **snapshot** of the current path before storing it. Without this, you'd store a reference to the shared list which would keep mutating after the fact.

---

## Key Takeaway

The original code was **correct in intent but wrong in execution**. The deduplication logic was trying to solve a real problem (duplicate combinations from an unsorted input), but the method — sorting a shared mutable list mid-recursion — introduced a subtle bug that corrupted backtracking state.

The fix doesn't just patch the dedup logic. It eliminates the *need* for deduplication entirely by sorting the input once and trusting the traversal order to enforce uniqueness by construction. That is the difference between **defensive checking** and **correct-by-design**.

The append/pop backtracking skeleton was correct all along — it is the standard memory-efficient approach, using `O(d)` space rather than allocating a new list per recursive call.