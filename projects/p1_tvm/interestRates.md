---
marp: true
theme: default
paginate: true
header: "Understanding Interest Rates"
footer: "Financial Mathematics"
---

# Interest Rates

## How to Compare Different Interest Rates

---

## Types of Interest Rates

- **Effective Rates**
  - Compound rates with interest paid once per unit time
  - Interest is paid at the end of the period
  - Used for future value and present value calculations

- **Nominal Rates**
  - Compound rates with interest paid multiple times per unit time
  - Example: Annual rate with monthly payments

---

# Common Nominal Rate Notations

| Notation | Meaning | Payment Frequency |
|----------|---------|-------------------|
| $i^{(12)}$ pa | Nominal annual rate | Monthly payments |
| $i^{(4)}$ pa | Nominal annual rate | Quarterly payments |
| $i^{(1)}$ pa | Nominal annual rate | Yearly payments |

---

# Nominal Rate Example: 12% per annum

Assume you have $1000 in the bank and the bank offers a **nominal interest rate of 12% per annum**.

| Notation | Payment Frequency | Effective Rate per Payment |
|----------|-------------------|--------------------------|
| $i^{(12)}$ pa | 12 times per year | 1% (12% ÷ 12) |
| $i^{(4)}$ pa | 4 times per year | 3% (12% ÷ 4) |
| $i^{(1)}$ pa | Once per year | 12% (12% ÷ 1) |

---

| Month | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|----------|----------|----------|
| Monthly ($i^{(12)}$) | 1% | 1% | 1% | 1% | 1% | 1% | 1% | 1% | 1% | 1% | 1% | 1% |
| Quarterly ($i^{(4)}$) | - | - | 3% | - | - | 3% | - | - | 3% | - | - | 3% |
| Yearly ($i^{(1)}$) | - | - | - | - | - | - | - | - | - | - | - | 12% |

If your have $1000 initially, how much will you have in 6 months?

| Month | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| Monthly ($i^{(12)}$) | $1010.00 | $1020.10 | $1030.30 | $1040.60 | $1051.01 | $1061.52 |
| Quarterly ($i^{(4)}$) | $1000.00 | $1000.00 | $1030.00 | $1030.00 | $1030.00 | $1060.90 |
| Yearly ($i^{(1)}$) | $1000.00 | $1000.00 | $1000.00 | $1000.00 | $1000.00 | $1000.00 |

---

# Interest Accumulation on $1,000

| Time Period | Monthly ($i^{(12)}$) | Quarterly ($i^{(4)}$) | Yearly ($i^{(1)}$) |
|-------------|---------------------|----------------------|-------------------|
| Initial     | $1,000.00          | $1,000.00           | $1,000.00        |
| 3 months    | $1,030.42          | $1,030.00           | $1,000.00        |
| 6 months    | $1,061.52          | $1,060.90           | $1,000.00        |
| 9 months    | $1,093.33          | $1,092.73           | $1,000.00        |
| 12 months   | $1,126.83          | $1,125.51           | $1,120.00        |

---

# Converting Nominal to Effective Rates

With **$1** in the bank and the bank offers a **nominal interest rate of 12% per annum**.


1. Effective rate per payment = (12% ÷ 12) → 1% 
2. Compound 12 times per year:
   $$
   (1 + 0.01)^{12} = 1.1268
   $$
3. Equivalent effective rate = 12.68% per annum

**Conclusion**: 12% pa nominal with monthly payments ($i^{(12)}$) is equivalent to an annual effective rate of 12.68%.

---

# Practice Problems

Calculate the equivalent effective rate per annum for:

1. 6% per annum, monthly payments (once per month, $i^{(12)}$)
2. 8% per annum, quarterly payments (once per quarter, $i^{(4)}$)
3. 10% per annum, semiannual payments (once per 6 months, $i^{(2)}$)
4. 12% per annum, yearly payments (once per year, $i^{(1)}$)

*Hint: Use the formula $(1 + \frac{r}{n})^n - 1$ where:*
- r = nominal rate
- n = number of payments per year

---

# Key Takeaways

1. **Effective Rates**
   - Interest paid once per period
   - Actual rate of return

2. **Nominal Rates**
   - Interest paid multiple times per period
   - Must be converted to effective rates
   - Common in banking and finance

3. **Conversion Formula**
   $$
   i_{eff} = (1 + \frac{i^{(n)}}{n})^n - 1
   $$