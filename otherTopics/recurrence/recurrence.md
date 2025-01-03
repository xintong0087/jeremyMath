---
marp: true
theme: default
---

# Understanding Recurrence Relations

---

# What is a Recurrence Relation? 🤔

- A recurrence relation is an equation that defines a sequence
- It relates each term to previous **terms**
- Example: Fibonacci sequence
  - $f(n) = f(n-1) + f(n-2)$
  - $f(1) = 1, f(2) = 1$

---

# How to Solve Recurrence Relations 🧠

- Find the first few terms of the sequence
- Set up the recurrence relation
- Going back in the sequence until you get to the terms you know
- Going forward in the sequence until you get to the term you want

---

# Example: Fibonacci Sequence 🔥

- $f(n) = f(n-1) + f(n-2)$
- $f(1) = 1, f(2) = 1$

**Question:** What is $f(5)$?

---

# Example: Fibonacci Sequence 🔥
Going back in the sequence:
- In the sequence, $f(5) = f(4) + f(3)$
- $f(4) = f(3) + f(2)$
- $f(3) = f(2) + f(1)$
- $f(2) = 1$
- $f(1) = 1$

---

# Example: Fibonacci Sequence 🔥

Going forward in the sequence:
- $f(3) = f(2) + f(1) = 1 + 1 = 2$
- $f(4) = f(3) + f(2) = 2 + 1 = 3$
- $f(5) = f(4) + f(3) = 3 + 2 = 5$

**Answer:** $f(5) = 5$

---

# Exam Question 📝

Everyday at school, Jo climbs a flight of $6$ stairs. Jo can take the stairs $1$, $2$, or $3$ at a time. For example, Jo could climb $3$, then $1$, then $2$. In how many ways can Jo climb the stairs?

---
## Finding the Recurrence Relation 📝

The question is asking for the number of ways to climb the stairs. We can use a recurrence relation to solve this problem.

Let $f(n)$ be the number of ways to climb $n$ stairs.The recurrence relation is 

$$f(n) = f(n-1) + f(n-2) + f(n-3)$$

Here is why: 

When there are $n$ stairs left, Jo can either:
- Take $1$ step, then $f(n-1)$ ways to climb the remaining stairs
- Take $2$ steps, then $f(n-2)$ ways to climb the remaining stairs
- Take $3$ steps, then $f(n-3)$ ways to climb the remaining stairs

So, $f(n) = f(n-1) + f(n-2) + f(n-3)$

---

# Finding the first few terms 📝


We just need to know the first three terms:
- When there is $1$ stair left, there is $1$ way to climb it
- When there is $2$ stairs left, there are $2$ ways to climb it (1+1, 2)
- When there is $3$ stairs left, there are $4$ ways to climb it (1+1+1, 1+2, 2+1, 3)

So, $f(1) = 1, f(2) = 2, f(3) = 4$

---

# Finding the number of ways to climb $6$ stairs 📝


We can use the recurrence relation to find the number of ways to climb $6$ stairs:
- $f(4) = f(3) + f(2) + f(1) = 4 + 2 + 1 = 7$
- $f(5) = f(4) + f(3) + f(2) = 7 + 4 + 2 = 13$
- $f(6) = f(5) + f(4) + f(3) = 13 + 7 + 4 = 24$

**Answer:** $f(6) = 24$






