---
marp: true
theme: default
paginate: true
header: '**Python For Loops Tutorial**'
footer: 'by Xintong'
---

# For Loops
## Mastering Iteration in Python

![bg left:40%](https://images.unsplash.com/photo-1587620962725-abab7fe55159?ixlib=rb-1.2.1&auto=format&fit=crop&w=1351&q=80)

---

## What is a For Loop?

- A for loop is used to iterate over a sequence (like a list) or other iterable objects.

---

## Basic For Loop

```python
for item in sequence:
    # Code to execute for each item
```

---

## Iterating Over Lists

```python
fruits = ["apple", "banana", "cherry"]

# Basic list iteration
for fruit in fruits:
    print(f"Current fruit: {fruit}")
```

Output:
```
Current fruit: apple
Current fruit: banana
Current fruit: cherry
```

---

## Using Range()

```python
# Iterate through numbers 0-4
for i in range(5):
    print(i)

# Specify start/end
for x in range(2, 6):
    print(x)
```

---

## Nested For Loops

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
    for f in fruits:
        print(f"{a} {f}")
```

---

## Loop Control Statements

```python
# Break example
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        break
    print(num)

# Continue example
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        continue
    print(num)
```

---

## Practice Exercises

```python
colors = ["red", "green", "blue"]
matrix = [[1, 2], [3, 4], [5, 6]]
```

1. Basic: Print all colors in uppercase
2. Intermediate: Sum all numbers in matrix using nested loops
3. Advanced: Create new list with colors containing letter 'e', using loop + if
4. Challenge: Print multiplication table (1-10) using nested ranges

**Tip:** Use `str.upper()` for #1, nested loops for #2





