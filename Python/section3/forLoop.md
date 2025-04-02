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

**Output:**
```
Current fruit: apple
Current fruit: banana
Current fruit: cherry
```

---

## Range()

- The `range()` function generates a sequence of numbers.
- This sequence can be used to iterate over a loop.

---

## Using Range()

```python
# Iterate through numbers 0-4
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

---

## Specify start/end

```python
# Iterate through numbers 2-5
for x in range(2, 6):
    print(x)
```

**Output:**
```
2
3
4
5
```

---

## Specify step

```python
# Iterate through numbers 0-10 by 2
for y in range(0, 11, 2):
    print(y)
```

**Output:**
```
0
2
4
6
8
10
```

---

## Example1: Sum numbers from 1 to 10

```python
# Sum numbers from 1 to 10
total = 0
for number in range(1, 11):
    total = total + number
print(f"Sum of numbers: {total}")
```
**Output:**  
`Sum of numbers: 55`  
*Demonstrates range with step parameter to process every 2nd number*

---

## Example2: Generate list of squares

```python
# Generate list of squares
squares = []
for n in range(5):
    squares.append(n ** 2)
print(f"Squares: {squares}")
```
**Output:**  
`Squares: [0, 1, 4, 9, 16]`  
*Shows how range can build complex data structures through iteration*

---


## Practice Exercises

1. Basic: Print numbers 1-10
2. Intermediate: Print even numbers 2-20
3. Advanced: Print cubes of numbers 1-5




