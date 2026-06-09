# Infix to Postfix

In the code you'll see this block 
```
while stack and stack[-1] != '(' and self.precidence(stack[-1])>=self.precidence(char) and not self.IsRightAssociative(char): 
                    result.append(stack.pop())
                stack.append(char)
```

the condition `not self.IsRightAssociative(char)` is strange but amazing as so

This specific `while` loop condition is the heart of the Shunting-Yard algorithm. It decides whether an operator currently sitting at the top of the stack (`st[-1]`) should be popped and executed **before** the incoming operator (`c`) is allowed to join the stack.

To understand why `and not isRightAssociative(c)` is written this way, we have to look at how **left-associative** and **right-associative** operators behave when they clash with an operator of the *exact same precedence*.

---

### The Fundamental Rule of Associativity

When two operators have the **same precedence**, the tie-breaker is their associativity:

1. **Left-Associative ($+, -, *, /$):** Process from left to right. The older operator on the stack runs first.
2. **Right-Associative ($\wedge$ or exponents):** Process from right to left. The newer incoming operator runs first.

Let's look at how this maps directly to your code's `or` condition when `prec(st[-1]) == prec(c)` (same precedence):

---

### Case 1: Left-Associative Operators (e.g., `+` and `-`)

Imagine your expression is `a - b + c`.

* **Stack contains:** `[-]`
* **Incoming operator `c`:** `+`
* **Precedence:** Both have a precedence of `1` (`prec('-') == prec('+')`).

Because they are left-associative, `a - b` must happen first. Therefore, the `-` on the stack **must be popped** to the result before `+` can be pushed.

Let's plug this into your code's condition:

* `prec(st[-1]) == prec(c)` $\rightarrow$ `1 == 1` (**True**)
* `not isRightAssociative('+')` $\rightarrow$ `not False` (**True**)
* `True and True` evaluates to **True** $\rightarrow$ **The loop runs, and `-` is popped.** (Correct!)

---

### Case 2: Right-Associative Operators (e.g., `^` and `^`)

Imagine your expression is `a ^ b ^ c`. Mathematically, this means $a^{(b^c)}$. The rightmost power has to happen first.

* **Stack contains:** `[^]`
* **Incoming operator `c`:** `^`
* **Precedence:** Both have a precedence of `3` (`prec('^') == prec('^')`).

Because it is right-associative, the incoming `^` needs to evaluate *before* the one already on the stack. Therefore, the `^` on the stack **should stay on the stack** and NOT be popped yet.

Let's plug this into your code's condition:

* `prec(st[-1]) == prec(c)` $\rightarrow$ `3 == 3` (**True**)
* `not isRightAssociative('^')` $\rightarrow$ `not True` (**False**)
* `True and False` evaluates to **False** $\rightarrow$ **The loop skips, nothing is popped.** The incoming `^` is simply pushed on top of the old `^`. (Correct!)

---

### Why don't we explicitly check if they have the *same* associativity?

You asked a great question: *Why not check `isRightAssociative(st[-1]) == isRightAssociative(c)`?*

We don't need to check if they match because **operators with the same precedence in standard mathematics always share the same associativity.**

* `+` and `-` both have precedence 1 and are both left-associative.
* `*` and `/` both have precedence 2 and are both left-associative.
* `^` has precedence 3 and is right-associative.

Because any two operators with matching precedence will automatically have the exact same associativity, we only have two possible scenarios when `prec(st[-1]) == prec(c)`:

1. They are both left-associative (so we **should** pop).
2. They are both right-associative (so we **should NOT** pop).

Therefore, writing `and not isRightAssociative(c)` acts as a perfect gatekeeper. It says: *"If the precedence is equal, only pop if we are dealing with left-associative operators."*


The whole condition `stack[-1] != '(' and self.precidence(stack[-1])>=self.precidence(char) and not self.IsRightAssociative(char)` as a whole pops from the stack as long as the operator on the stack has "priority" over the incoming one or till the stack in empty (`while stack`)