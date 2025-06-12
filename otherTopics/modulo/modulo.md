---
marp: true
theme: default
---

# Understanding Modulo

---

# What is Modulo? 🤔

- Modulo is the remainder when you divide one number by another
- Example: $7 \mod 3 = 1$
- $7 \div 3 = 2$ remainder $1$

---

# How to Use Modulo 🧠

- Modulo is useful for checking if two numbers are congruent, i.e. they have the same remainder when divided by a certain number
- Example: $7 \mod 3 = 1$ and $10 \mod 3 = 1$
- Therefore, 
$$7 \equiv 10 \mod 3$$

---

# Example Exam Question 🔥

What is the tens digit of $7^{2011}$?

## Explanation 🧠

The tens digit of a number is the second-to-last digit of the number.

---

# Solution 🧠

- $7^1 \mod 100 = 7$
- $7^2 \mod 100 = 49$
- $7^3 \mod 100 = 343 \mod 100 = 43$
- $7^4 \mod 100 = 7 \times 343 = 2401 \mod 100 = 1$

Only the last two digits of the product are relevant, so we can ignore the rest of the digits.

- $7^5 \mod 100 = 7 \times 1 \mod 100 = 7$
- $7^6 \mod 100 = 7 \times 7 \mod 100 = 49$
- $7^7 \mod 100 = 7 \times 49 \mod 100 = 343 \mod 100 = 43$
- $7^8 \mod 100 = 7 \times 343 \mod 100 = 2401 \mod 100 = 1$

We can see that the last two digits of $7^n \mod 100$ repeat every 4 powers.

---

# Answer 🤖

- $7^{2011} \mod 100 = 7^{4 \times 502 + 3} \mod 100 = 7^3 \mod 100 = 43$
- Therefore, the tens digit of $7^{2011}$ is $\boxed{4}$

---

# Rationale Behind Repeating Patterns 🧠

When multiplying long-digit numbers:

- The last few digits of the product are only affected by the last few digits of the numbers being multiplied
- This means that the last few digits of the product will repeat in a cycle
- This cycle can be used to find the last few digits of large powers

---

# Practice Problems 📝

1. What is the last two digits of $3^{2024}$?
2. What is the last three digits of $7^{2024}$?

---

# Advanced Topics 🧠

Does the same pattern hold for other bases?

- What if we used a different base, like $12$?
- **Hint:** Try to find a pattern for $7^n \mod 12$

Further Reading:

- [Modular Arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic)
- [Modular Exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation)

