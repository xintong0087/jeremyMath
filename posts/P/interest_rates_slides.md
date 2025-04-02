---
marp: true
theme: default
paginate: true
header: "Understanding Interest Rates"
footer: "Financial Mathematics"
---

# Interest Rates

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

| Notation | Payment Frequency | Effective Rate per Payment |
|----------|-------------------|--------------------------|
| $i^{(12)}$ pa | 12 times per year | 1% (12% ÷ 12) |
| $i^{(4)}$ pa | 4 times per year | 3% (12% ÷ 4) |
| $i^{(1)}$ pa | Once per year | 12% (12% ÷ 1) |

---

# Payment Schedule Comparison

| Month | Monthly ($i^{(12)}$) | Quarterly ($i^{(4)}$) | Yearly ($i^{(1)}$) |
|-------|---------------------|----------------------|-------------------|
| 1     | 1% payment         | No payment          | No payment       |
| 2     | 1% payment         | No payment          | No payment       |
| 3     | 1% payment         | 3% payment          | No payment       |
| 4     | 1% payment         | No payment          | No payment       |
| 5     | 1% payment         | 3% payment          | No payment       |
| 6     | 1% payment         | 3% payment          | No payment       |
| 7     | 1% payment         | No payment          | No payment       |
| 8     | 1% payment         | 3% payment          | No payment       |
| 9     | 1% payment         | 3% payment          | No payment       |
| 10    | 1% payment         | No payment          | No payment       |
| 11    | 1% payment         | 3% payment          | No payment       |
| 12    | 1% payment         | 3% payment          | 12% payment      |

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

## Example: 12% per annum, monthly payments

1. Effective rate per payment = 1% (12% ÷ 12)
2. Compound 12 times per year:
   $$
   (1 + 0.01)^{12} = 1.1268
   $$
3. Equivalent effective rate = 12.68% per annum

---

# Practice Problems

Calculate the equivalent effective rate per annum for:

1. 6% per annum, monthly payments
2. 8% per annum, quarterly payments
3. 10% per annum, yearly payments

*Hint: Use the formula $(1 + \frac{r}{n})^n - 1$ where:*
- r = nominal rate
- n = number of payments per year

---

# Key Takeaways

1. **Effective Rates**
   - Interest paid once per period
   - Used for calculations
   - Actual rate of return

2. **Nominal Rates**
   - Interest paid multiple times per period
   - Must be converted to effective rates
   - Common in banking and finance

3. **Conversion Formula**
   $$
   i_{eff} = (1 + \frac{i^{(n)}}{n})^n - 1
   $$ 