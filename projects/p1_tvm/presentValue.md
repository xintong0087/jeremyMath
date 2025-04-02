---
marp: true
theme: default
---

# Understanding Present Value
## How to Compare Different Cash Flow Streams

---

# Example: Which Investment is Better?


**Investment A:**
- Year 0: -$1,000 (initial investment)
- Year 1: +$350
- Year 2: +$500
- Year 3: +$500

**Investment B:**
- Year 0: -$1,000 (initial investment)
- Year 1: +$50
- Year 2: +$450
- Year 3: +$900

Which investment is better at different interest rates?

---

# The Concept of Present Value

Present Value (PV) tells us how much a future amount of money is worth today.

For multiple cash flows, we calculate the present value of each cash flow and sum them:
```
PV = CF₀ + CF₁/(1 + r) + CF₂/(1 + r)² + CF₃/(1 + r)³ + ...
```
Where:
- CF₀ = Cash flow at time 0 (today)
- CF₁, CF₂, CF₃ = Future cash flows
- r = Interest rate (as a decimal)

---

# Why Present Value Matters for Cash Flows

1. **Investment Decisions**: Helps compare projects with different cash flow patterns
2. **Fair Comparison**: Converts all future cash flows to today's dollars
3. **Net Present Value**: The sum of all present values tells us if an investment is worthwhile

---

# Comparing at 0% Interest Rate

When interest rate = 0%, money doesn't change value over time.

**Investment A:**
- PV = -$1,000 + $350 + $500 + $500 = $350

**Investment B:**
- PV = -$1,000 + $50 + $450 + $900 = $400

**Best choice: Investment B** (PV = $400)

---

# Comparing at 5% Interest Rate

Let's calculate the present value of each investment.

**Investment A:**
- PV = -$1,000 + $350/(1.05) + $500/(1.05)² + $500/(1.05)³
- PV = -$1,000 + $333.33 + $453.51 + $432.38
- PV = $219.22

**Investment B:**
- PV = -$1,000 + $50/(1.05) + $450/(1.05)² + $900/(1.05)³
- PV = -$1,000 + $47.62 + $408.16 + $778.41
- PV = $234.19

---

# Comparison at 5% Interest Rate

| Investment | Initial Cost | PV of Future Cash Flows | Net Present Value |
|------------|--------------|-------------------------|-------------------|
| A | -$1,000 | $1,219.22 | $219.22 |
| B | -$1,000 | $1,234.19 | $234.19 |

**Best choice: Investment B** (NPV = $234.19)

---

# Comparing at 10% Interest Rate

Let's calculate the present value of each investment.

**Investment A:**
- PV = -$1,000 + $350/(1.10) + $500/(1.10)² + $500/(1.10)³
- PV = -$1,000 + $318.18 + $413.22 + $375.66
- PV = $107.06

**Investment B:**
- PV = -$1,000 + $50/(1.10) + $450/(1.10)² + $900/(1.10)³
- PV = -$1,000 + $45.45 + $371.90 + $677.14
- PV = $94.49

---

# Comparison at 10% Interest Rate

| Investment | Initial Cost | PV of Future Cash Flows | Net Present Value |
|------------|--------------|-------------------------|-------------------|
| A | -$1,000 | $1,107.06 | $107.06 |
| B | -$1,000 | $1,094.49 | $94.49 |

**Best choice: Investment A** (NPV = $107.06)

---

# Comparing at 15% Interest Rate

Let's calculate the present value of each investment.

**Investment A:**
- PV = -$1,000 + $350/(1.15) + $500/(1.15)² + $500/(1.15)³
- PV = -$1,000 + $304.35 + $377.85 + $328.76
- PV = $10.96

**Investment B:**
- PV = -$1,000 + $50/(1.15) + $450/(1.15)² + $900/(1.15)³
- PV = -$1,000 + $43.48 + $340.26 + $591.77
- PV = -$24.49

---

# Comparison at 15% Interest Rate

| Investment | Initial Cost | PV of Future Cash Flows | Net Present Value |
|------------|--------------|-------------------------|-------------------|
| A | -$1,000 | $1,010.96 | $10.96 |
| B | -$1,000 | $975.51 | -$24.49 |

**Best choice: Investment A** (NPV = $10.96)

---

# How Interest Rate Changes Our Decision

| Interest Rate | Best Investment | Net Present Value |
|---------------|-----------------|-------------------|
| 0% | B | $400.00 |
| 5% | B | $234.19 |
| 10% | A | $107.06 |
| 15% | A | $10.96 |

---

# Key Insights from This Example


1. **Interest Rate Impact**:
   - At low rates (0-5%), Investment B's higher total return wins
   - At higher rates (10-15%), Investment A's earlier cash flows win
   - Investment B becomes unprofitable at 15% (negative NPV)

2. **Decision Making**:
   - Low interest rates favor higher total returns
   - High interest rates favor earlier cash flows
   - The crossover occurs between 5% and 10% in this example

---

# Exercise 1: Compare Investments

**Investment X:**
- Year 0: -$2,000
- Year 1: +$1,000
- Year 2: +$1,000
- Year 3: +$1,000

**Investment Y:**
- Year 0: -$2,000
- Year 1: +$500
- Year 2: +$1,000
- Year 3: +$1,500


---

# Exercise 1: Compare Investments

1. Calculate the Net Present Value of each investment at:
    1. 3%
    2. 8%
    3. 12%

2. Which investment is better at different interest rates?

3. What is rate when they are equal?


**Hint**: To solve for #3, you can try using trial and error (plug in different rates). It can be difficult to solve by hand, but you have Python!

---

# Exercise 2: Find the Rate

This is a practical problem. Let's say you want to save $\$y$ for your college tuition. You have $t$ years to save. You can invest in a savings account that pays $x\%$ interest. How much do you need to save each year?

1. Find your $x$, $y$, and $t$
    - $x$ can be found on the internet (Bank websites, CD rate quotes, etc.)
    - $y$ is the total cost of your education, or is it?
    - $t$ is the number of years until you start college.
2. Calculate how much you need to save each year



