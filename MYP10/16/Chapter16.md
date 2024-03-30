# Number Sequences Tutorial

In mathematics, a number sequence is a list of numbers arranged in a specific order. Number sequences can be finite or infinite, and they can follow different patterns or rules.

**Examples of a number sequence:**

1. The sequence of natural numbers: 1, 2, 3, 4, 5, ...
2. The sequence that starts with 2 and increases by 3 each time: 2, 5, 8, 11, 14, ...
3. The sequence that has an explicit formula for $n = 1, 2, 3, 4, ...$
        $$u_n = 2n + 3$$ 
    * $u_n$ is the $n^{th}$ term of the sequence.
    * What is the 5th term of the sequence?
4. The sequence that has a recursive formula. For $n = 1$
        $$u_1 = 2,$$
        and the following terms are given by the recursive formula:
        $$u_{n+1} = u_n + 3$$
    * $u_n$ is the $n^{th}$ term of the sequence.
    * What is the 5th term of the sequence?

![ExerciseA](ExerciseA.png)

**Fibonacci Sequence:**

The Fibonacci sequence is a famous sequence of numbers in which each term is the sum of the two preceding terms. It starts with 1 and 1, and after that, each term is the sum of the two preceding terms.

The Fibonacci sequence can be written as:

$$1, 1, 2, 3, 5, 8, 13, 21, ...$$

* What is the 10th term of the Fibonacci sequence?
* Can you come up with a recursive formula for the Fibonacci sequence?

$$u_1 = 1, u_2 = 1, ~~ u_n = u_{n-1} + u_{n-2} ~~\text{for}~~ n \geq 3 $$

* I can't even come up with the explicit formula for the Fibonacci sequence. Strange things happen in mathematics.

$$ u_n = \frac{1}{\sqrt{5}} \left( \left( \frac{1 + \sqrt{5}}{2} \right)^n - \left( \frac{1 - \sqrt{5}}{2} \right)^n \right) $$

For the rest of the chapter, we will use **explicit formulas** or **recursive formulas** to describe a sequence, whichever is **more convenient**.

## Arithmetic Sequences

An arithmetic sequence is a sequence of numbers in which the difference between any two consecutive terms is constant. The constant difference is called the common difference.

The general form of an arithmetic sequence is:

$$u_1, u_1 + d, u_1 + 2d, u_1 + 3d, ...$$

where $u_1$ is the first term and $d$ is the common difference.

The $n^{th}$ term of an arithmetic sequence can be found using the **explicit formula**:

$$u_n = u_1 + (n - 1)d$$

where $u_n$ is the $n^{th}$ term, $u_1$ is the first term, $d$ is the common difference, and $n$ is the term number.

The $n^{th}$ term of an arithmetic sequence can also be found using the **recursive formula**:

$$u_1 = a, ~~~ u_{n+1} = u_n + d$$

where $u_1$ is the first term, $a$ is the first term, $d$ is the common difference, and $n$ is the term number.

![ExerciseB](ExerciseB.png)

**Think about them:** 

1. what is the sum of the first 100 terms of the arithmetic sequence with the first term 1 and the common difference 1?
2. what is the sum of the first k terms of the arithmetic sequence with the first term $u_1$ and the common difference $d$?

## Geometric Sequences

A geometric sequence is a sequence of numbers in which each term is found by multiplying the previous term by a constant ratio. The constant ratio is called the common ratio.

The general form of a geometric sequence is:

$$u_1, u_1r, u_1r^2, u_1r^3, ...$$

where $u_1$ is the first term and $r$ is the common ratio.


## Conclusion

Number sequences are an important concept in mathematics and have various applications in different fields. Understanding different types of sequences can help in solving mathematical problems and analyzing patterns.
