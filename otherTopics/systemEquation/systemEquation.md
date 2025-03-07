---
marp: true
theme: default
---

# System of Equations

A system of equations is a set of two or more equations that are solved simultaneously.

---

## Example 1

$$
\begin{cases}
x + y = 3 \quad \text{(1)} \\
x - y = 1 \quad \text{(2)}
\end{cases}
$$

The curly brace means that the equations need to be **simultaneously satisfied**.

---

$$
\begin{cases}
x + y = 3 \quad \text{(1)} \\
x - y = 1 \quad \text{(2)}
\end{cases}
$$

## Solution

To solve the system of equations, we need to find the values of $x$ and $y$ that satisfy both equations.

We can solve the system of equations by **substitution** or **elimination**.

---

## Substitution Method

1. Solve one of the equations for one of the variables.
2. Substitute the expression for this variable into the other equation.
3. Solve the resulting equation.
4. Substitute the value found in step 3 into one of the original equations to find the value of the other variable.

---

### Step 1

Solve one of the equations for one of the variables.

$$
x + y = 3 \quad \text{(1)}
$$

Solve for $x$:

$$
x = 3 - y \quad \text{(3)}
$$

---

### Step 2

Substitute the expression for this variable into the other equation.

Substitute $x = 3 - y$ into equation (2):

$$
(3 - y) - y = 1
$$

Simplify the equation:

$$
3 - 2y = 1
$$

---

### Step 3

Solve the resulting equation.

$$
3 - 2y = 1
$$

Subtract 3 from both sides:

$$
-2y = 1 - 3
$$

Simplify the equation:

$$
-2y = -2
$$


Therefore, $y = 1$.

---

### Step 4

Substitute the value found in step 3 into one of the original equations to find the value of the other variable.

Substitute $y = 1$ into equation (1):

$$
x + 1 = 3
$$

Solve for $x$:

$$
x = 3 - 1
$$

Therefore, $x = 2$.

---

### Final Answer

The solution to the system of equations is $x = 2$ **and** $y = 1$.

### Review of the Substitution Method

1. Solve one of the equations for one of the variables.
2. Substitute the expression for this variable into the other equation.
3. Solve the resulting equation.
4. Substitute the value found in step 3 into one of the original equations to find the value of the other variable.

---

## Elimination Method

1. Multiply one or both equations by a constant so that the coefficients of one of the variables are opposites.

2. Add the equations together to eliminate one of the variables.
3. Solve the resulting equation for the remaining variable.
4. Substitute the value found in step 3 into one of the original equations to find the value of the other variable.

---

## Example 2

$$
\begin{cases}
x + 2y = 3 \quad \text{(1)} \\
x - y = 1  \quad \text{(2)}
\end{cases}
$$

### Step 1

Multiply one or both equations by a constant so that the coefficients of one of the variables are opposites.

Multiply equation (2) by 2:

$$
2(x - y) = 2 \quad \text{(3)}
$$

Simplify the equation:

$$
2x - 2y = 2 \quad \text{(3)}
$$

---

$$
\begin{cases}
x + 2y = 3 \quad \text{(1)} \\
2x - 2y = 2 \quad \text{(3)}
\end{cases}
$$


### Step 2

Add the equations together to eliminate one of the variables.

Add equation (1) and equation (3):

$$
(x + 2y) + (2x - 2y) = 3 + 2
$$

Simplify the equation:

$$
3x = 5
$$

---

### Step 3

Solve the resulting equation for the remaining variable.

$$
3x = 5
$$

Therefore, $x = \frac{5}{3}$.

---

### Step 4

Substitute the value found in step 3 into one of the original equations to find the value of the other variable.

Substitute $x = \frac{5}{3}$ into equation (1):

$$
\frac{5}{3} + 2y = 3
$$

Solve for $y$:

$$
2y = 3 - \frac{5}{3}
$$

Therefore, $y = \frac{4}{3}$.

---

### Final Answer

The solution to the system of equations is $x = \frac{5}{3}$ and $y = \frac{4}{3}$.

### Review of the Elimination Method

1. Multiply one or both equations by a constant so that the coefficients of one of the variables are opposites.
2. Add the equations together to eliminate one of the variables.
3. Solve the resulting equation for the remaining variable.
4. Substitute the value found in step 3 into one of the original equations to find the value of the other variable.

---

## Practice Questions

1. Solve the following system of equations using the substitution method:

$$
\begin{cases}
2x + y = 5 \quad \text{(1)} \\
x - y = 1  \quad \text{(2)}
\end{cases}
$$

2. Solve the following system of equations using the elimination method:

$$
\begin{cases}
5x + 2y = 10 \quad \text{(1)} \\
3x - 4y = 2  \quad \text{(2)}
\end{cases}
$$

---

## Practice Questions

3. Solve the following system of equations using both the substitution and elimination methods. Which method is easier?

$$
\begin{cases}
2.5x + 3y = 10 \quad \text{(1)} \\
1.5x - 2y = 5 \quad \text{(2)}
\end{cases}
$$


4. Solve the following system of equations using both the substitution and elimination methods. Which method is easier?

$$
\begin{cases}
6x + 2y = 10 \quad \text{(1)} \\
3x - 4y = 2  \quad \text{(2)}
\end{cases}
$$


---

## Checking your answers

Verify your answers by substituting them back into the original equations. For example, if you solve the system of equations and get $x = 2$ and $y = 1$, you can substitute these values back into the original equations to check if they satisfy both equations.

Can you check the answers for Problem 3 and Problem 4?

**Problem 3**
$$
\begin{cases}
2.5x + 3y = 10 \quad \text{(1)} \\
1.5x - 2y = 5 \quad \text{(2)}
\end{cases}
$$

**Problem 4**
$$
\begin{cases}
6x + 2y = 10 \quad \text{(1)} \\
3x - 4y = 2  \quad \text{(2)}
\end{cases}
$$

---

## More Problems

In the following problems, we have real examples of systems of equations. 
Please proceed by **first setting up the system of equations** and **then solving it.**

1. A school has 100 students. The number of girls is 10 more than the number of boys. How many boys and girls are there in the school?

2. Ben is running a lemonade stand. He sells lemonade for $2 per cup and water for $1 per cup. He made $100 yesterday, and he used 75 cups. How many cups of lemonade and water did he sell?



---

## More Problems

#### AMC 10 2024A - Problem 8 

Amy, Bomani, Charlie, and Daria work in a chocolate factory. On Monday Amy, Bomani, and Charlie started working at $1:00 PM$ and were able to pack $4$, $3$, and $3$ packages, respectively, every $3$ minutes. At some later time, Daria joined the group, and Daria was able to pack $5$ packages every $4$ minutes. Together, they finished packing $450$ packages at exactly $2:45 PM$. At what time did Daria join the group?

$\textbf{(A) }1:25\text{ PM}\qquad\textbf{(B) }1:35\text{ PM}\qquad\textbf{(C) }1:45\text{ PM}$

$\textbf{(D) }1:55\text{ PM}\qquad\textbf{(E) }2:05\text{ PM}$


---

## Going Beyond Linear Equations

#### AMC 10 2024A - Problem 23

Integers $a$, $b$, and $c$ satisfy $ab + c = 100$, $bc + a = 87$, and $ca + b = 60$. What is $ab + bc + ca?$

$\textbf{(A) }212 \qquad \textbf{(B) }247 \qquad \textbf{(C) }258 \qquad \textbf{(D) }276 \qquad \textbf{(E) }284 \qquad$
