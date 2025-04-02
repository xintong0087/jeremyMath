# Project 1: Time Value of Money

In this project, you will learn how to compare different investment options using the time value of money.

## Learning Objectives

- Understand the concept of the time value of money.
- Understand the relationship between present value and future value.

## Instructions

This document contains the material for the first project.

You will be given a series of questions on the time value of money. 
Each question will have a description of the problem and a set of options. 
You will need to select the correct option to answer the question.

## Future Value

The future value (FV) of a present sum of money is the value of that sum at a specified point in the future, assuming a certain rate of return or interest rate. 

### Example

Let's say you can choose between 

1. receiving $100 today or 
2. receiving $100 in 5 years. 

The interest rate is 5% per annum, compounded annually.

Which option should you choose?

- If you choose to receive $100 today, you can invest it at a 5% interest rate. At the end of 5 years, you will have 
    $$
    \$100 \times (1 + 0.05)^5 = \$127.63
    $$
- If you choose to receive $100 in 5 years, the future value at time 5 is $100.

Comparing the two options, receiving $100 today is better because it has a higher future value at time 5 ($127.63 > $100).

### Exercise

For all the following exercises, assume the interest rate is 5% per annum, compounded annually.

1. Choose among the following options:
    - receiving $100 today
    - receiving $125 in 5 years
    - receiving $150 in 10 years

2. Choose among the following options:
    - receiving $100 today
    - receiving $50 today and $63 in 5 years
    - receiving $75 in 1 year and $51 in 5 years

## Present Value

The present value (PV) of a future sum of money is the current value of that sum, discounted to account for the time value of money. 

### Example

Let's say you can choose between 

1. receiving $100 today or 
2. receiving $100 in 5 years. 

The interest rate is 5% per annum, compounded annually.

Which option should you choose?

- If you choose to receive $100 today, the present value is $100.
- If you choose to receive $100 in 5 years, the present value is 
    $$
    \frac{100}{(1 + 0.05)^5} = \$78.35
    $$

Comparing the two options, receiving $100 today is better because it has a higher present value ($100 > $78.35).


### Exercise

For all the following exercises, assume the interest rate is 5% per annum, compounded annually.

1. Choose among the following options:
    - receiving $100 today
    - receiving $50 today and $63 in 5 years
    - receiving $75 in 1 year and $51 in 5 years

2. Choose among the following options:
    - receiving $100 today
    - receiving $11 every year for 10 years

## Interest Rates

### Effective Rates

- **Effective rates**: compound rates that have interest paid once per unit time
- **Paid at the end of the period** → effective interest

Effective rates are the actual rates we use to calculate the future value and present value of money.

### Nominal Rates

- **Nominal rates**: compound rates that have interest paid multiple times per unit time
- E.g., banks may quote the annual interest rate (one-year unit time), but interest is actually added more frequently than once per unit year, say, each month

We need to convert nominal rates to effective rates to use them in our calculations.

The most common nominal rates are:

- $i^{(12)}$ pa is the nominal interest rate payable **monthly**

- $i^{(4)}$ pa is the nominal interest rate payable **quarterly**

- $i^{(1)}$ pa is the nominal interest rate payable **yearly**

---

### Nominal Interest Rate Examples

Let's say you have a nominal interest rate of 12% per annum of **different payment frequencies**.

| Notation | Meaning | Payment Frequency | Effective Rate per Payment |
|----------|---------|-------------------|--------------------------|
| $i^{(12)}$ pa | Nominal annual rate, monthly payments | 12 times per year | 1% |
| $i^{(4)}$ pa | Nominal annual rate, quarterly payments | 4 times per year | 3% |
| $i^{(1)}$ pa | Nominal annual rate, yearly payments | Once per year | 12% |

To calculate the effective rate per payment, we need to divide the nominal rate by the number of payments per year.

- For $i^{(12)}$ pa, the effective rate per payment is 1% because 12% / 12 = 1%.
- For $i^{(4)}$ pa, the effective rate per payment is 3% because 12% / 4 = 3%.
- For $i^{(1)}$ pa, the effective rate per payment is 12% because 12% / 1 = 12%.

### Exercise

Calculate the effective rate per payment for the following nominal interest rates:

- 6% per annum, monthly payments
- 8% per annum, quarterly payments
- 10% per annum, yearly payments

---

### Comparison of Payment Schedules

| Month | $i^{(12)}$ pa = 12% | $i^{(4)}$ pa = 12% | $i^{(1)}$ pa = 12% |
|-------|------------------|-----------------|-----------------|
| 1     | 1% payment       | No payment      | No payment      |
| 2     | 1% payment       | No payment      | No payment      |
| 3     | 1% payment       | 3% payment      | No payment      |
| 4     | 1% payment       | No payment      | No payment      |
| 5     | 1% payment       | 3% payment      | No payment      |
| 6     | 1% payment       | 3% payment      | No payment      |
| 7     | 1% payment       | No payment      | No payment      |
| 8     | 1% payment       | 3% payment      | No payment      |
| 9     | 1% payment       | 3% payment      | No payment      |
| 10    | 1% payment       | No payment      | No payment      |
| 11    | 1% payment       | 3% payment      | No payment      |
| 12    | 1% payment       | 3% payment      | 12% payment     |

---

### Interest Accumulation on $1,000 Investment

| Time Period | $i^{(12)}$ pa = 12% | $i^{(4)}$ pa = 12% | $i^{(1)}$ pa = 12% |
|-------------|------------------|-----------------|-----------------|
| Initial     | $1,000.00        | $1,000.00       | $1,000.00       |
| 3 months    | $1,030.42        | $1,030.00       | $1,000.00       |
| 6 months    | $1,061.52        | $1,060.90       | $1,000.00       |
| 9 months    | $1,093.33        | $1,092.73       | $1,000.00       |
| 12 months   | $1,126.83        | $1,125.51       | $1,120.00       |

For $i^{(12)}$ pa = 12%, the interest is added 12 times per year (at the end of each month).  


### From Nominal to Equivalent Effective Rates

For example, if you have a nominal interest rate of 12% per annum, compounded monthly.
We want to find the equivalent effective rate per annum.

We know that the effective rate per payment is 1% because 12% / 12 = 1%.

Compound the effective rate per payment 12 times per year for 1 year.

$$
(1 + 0.01)^{12} = 1.1268
$$

Therefore, the equivalent effective rate per annum is 12.68%.

### Exercise

Calculate the equivalent effective rate per annum for the following nominal interest rates:

- 6% per annum, monthly payments
- 8% per annum, quarterly payments
- 10% per annum, yearly payments


## Annuity Formula

An annuity is a series of equal payments made at regular intervals.
People often use annuities for retirement income, that is, they want to receive a fixed amount of money each year for the rest of their lives.

The present value of an annuity is the sum of the present values of each payment.

### Example

John, at the age of 60, wants to receive a fixed amount of money every year for the rest of his life.
He wants to receive $2000 every month for the next 30 years.
The interest rate is 6% per annum, compounded monthly.

What is the present value of these payments?

First, we need to convert the annual interest rate to a monthly interest rate.
$$
r = \frac{6\%}{12} = 0.5\%
$$

- For the first payment, the present value is $2000.
- For the second payment, the present value is 
$$
\frac{2000}{(1 + 0.005)^1} = \$1990.05
$$
- For the third payment, the present value is 
$$
\frac{2000}{(1 + 0.005)^2} = \$1980.10
$$
- ...
- For the 360th payment, the present value is 
$$
\frac{2000}{(1 + 0.005)^{360}} = \$1000
$$

The present value of the annuity is the sum of the present values of each payment.

$$
PV = \frac{2000}{(1 + 0.005)^1} + \frac{2000}{(1 + 0.005)^2} + ... + \frac{2000}{(1 + 0.005)^{360}}
$$

This is a geometric series, and the sum of a geometric series is given by:

$$
S = \frac{a(1 - r^n)}{1 - r}
$$

- where $a$ is the first term, $r$ is the common ratio, and $n$ is the number of terms.

In our case, $a = 2000$, $r = 1 + 0.005$, and $n = 360$.

$$
PV = \frac{2000(1 - (1 + 0.005)^{360})}{1 - (1 + 0.005)}
$$

By calculating this, we get $PV = \$383,955.28$.

Therefore, John should deposit $383,955.28 today to receive $2000 every month for the next 30 years.

### Exercise

Jack, at the age of 60, wants to receive a fixed amount of money every year for the next 20 years.
He wants to receive $1000 every month for the next 20 years.
The interest rate is 1% per month, compounded monthly.

# Project Description

## Part 1: Formula Reference Sheet 

Create a comprehensive reference sheet that includes:

1. Future Value Formula:
    $$
    FV = PV \times (1 + r)^n
    $$
    Include examples with different interest rates and time periods

2. Present Value Formula:
    $$
    PV = FV \div (1 + r)^n
    $$
    Include examples showing how to discount future amounts

3. Annuity Formulas:
    - Future Value of Annuity: 
        $$
        FV = PMT \times \frac{(1 + r)^n - 1}{r}
        $$
    - Present Value of Annuity: 
        $$
        PV = PMT \times \frac{1 - (1 + r)^{-n}}{r}
        $$
    Include examples for regular payment scenarios

4. Loan Payment Formula:
    $$
    PMT = PV \times \frac{r}{(1 + r)^n - 1}
    $$
    Include examples for different loan amounts and terms

Your reference sheet should be neatly organized, include clear explanations of variables, and provide step-by-step examples for each formula.

## Part 2: Decision-Making Framework

Develop a structured approach to financial decision-making that includes:

1. Problem Identification:

    - What is the financial decision being made?

    - What are the available options?

    - What is the appropriate interest rate to use?

2. Time Alignment:

    - Convert all options to either present value or future value

    - Create a timeline showing when each cash flow occurs

3. Calculation Process:

    - Step-by-step procedure for calculating comparable values

    - Method for handling multiple cash flows

4. Decision Criteria:

    - How to determine which option is financially optimal

    - Considerations beyond pure financial calculations

## Part 3: Case Studies

Apply your framework to analyze at least 2 of the following scenarios:

1. Investment Comparison:

    - Option A: Receive $5,000 today

    - Option B: Receive $2,500 today and $3,000 in 2 years

    - Option C: Receive $6,500 in 3 years

    - Assume an interest rate of 6% per annum

2. Loan Decision:

    - Option A: 5-year loan at 4.5% interest with monthly payments

    - Option B: 3-year loan at 3.9% interest with monthly payments

    - Loan amount: $15,000

3. Retirement Savings:

    - Goal: $500,000 retirement fund in 30 years

    - Determine how much to save monthly with an expected 7% annual return

4. Education Fund:

    - Need $25,000 for college in 10 years

    - Compare lump sum investment today vs. regular monthly contributions

5. Home Purchase:

    - Option A: Buy now with a 30-year mortgage at 5.5%

    - Option B: Rent for 5 years while saving, then buy with a larger down payment

    - Analyze the financial implications of both options
    
For each case study, show your work clearly, explain your reasoning, and justify your conclusion.


## Part 4: Presentation and Reflection

Create a final presentation that includes:

1. Executive Summary:

    - Overview of your decision-making framework

    - Key insights from your case studies

2. Case Study Results:

    - Detailed analysis of each scenario

    - Visual aids (timelines, charts, tables) to illustrate your calculations

3. Practical Applications:

    - How your framework can be applied to everyday financial decisions

    - Limitations and considerations when using time value of money

4. Personal Reflection:

    - How this project changed your understanding of financial decisions

    - Real-life situations where you might apply these concepts







