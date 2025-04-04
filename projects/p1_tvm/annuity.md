---
marp: true
theme: default
paginate: true
---

# Understanding Annuities
## Regular Payments Over Time

---

# What is an Annuity?

An annuity is a series of equal payments made at regular intervals:

| Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|--------|--------|--------|--------|--------|
| $1000  | $1000  | $1000  | $1000  | $1000  |


Each payment is:
- The same amount
- Made at regular intervals
- For a specified period

---

# Present Value of an Annuity

The present value (PV) is what all future payments are worth today.

For each payment, we need to:
1. Discount it back to today
2. Add up all discounted values

$$PV = PMT × \frac{1 - (1 + r)^{-n}}{r},$$

where:
- PMT = Payment amount
- r = Interest rate per period
- n = Number of payments

---

# Understanding the Formula

If you receive $1000 annually for 3 years at 5% interest:

1. First payment (1 year): $\frac{1000}{(1.05)^1} = 952.38$
2. Second payment (2 years): $\frac{1000}{(1.05)^2} = 907.03$
3. Third payment (3 years): $\frac{1000}{(1.05)^3} = 863.84$

Total Present Value = $2,723.25

---

# Geometric Series

A geometric series has the form:

$$S = a + ar + ar^2 + ar^3 + ... + ar^{n-1}$$

Where:
- $a$ is the first term
- $r$ is the common ratio
- $n$ is the number of terms

The sum of this finite geometric series is:

$$S = a \times \frac{1 - r^n}{1 - r}$$


---

For an annuity, we're calculating the present value of future payments:

$$PV = \frac{PMT}{(1+r)^1} + \frac{PMT}{(1+r)^2} + \frac{PMT}{(1+r)^3} + ... + \frac{PMT}{(1+r)^n}$$

This is a geometric series where:
- $a = \frac{PMT}{(1+r)}$ (first term)
- Common ratio = $\frac{1}{(1+r)}$
- $n$ = number of payments

Applying the geometric series formula:

$$PV = PMT \times \frac{1 - (1+r)^{-n}}{r}$$

Which is our standard present value of an annuity formula.




---

# Payment Formula

To find how much each payment should be:

$$PMT = PV × \frac{r}{1 - (1 + r)^{-n}}$$

This is useful for:
- Planning savings goals
- Calculating loan payments
- Determining retirement withdrawals

---

# Types of Annuities

1. **Ordinary Annuity (Annuity Immediate)**
   - Payments at END of each period
   - Example: Most loan payments
   
2. **Annuity Due**
   - Payments at START of each period
   - Example: Rent payments
   - Worth more because payments made earlier

---

# Payment Frequency Matters!

Annual vs Monthly Payments:
- Annual: 1 payment per year
- Monthly: 12 payments per year

Need to adjust:
1. Interest rate: r → r/12
2. Number of periods: n → n×12

Example: 5% annual = 0.417% monthly

---

# Basic Python Implementation

```python
def calculate_pv_annuity(payment, rate, periods):
    """Calculate present value of an ordinary annuity"""
    if rate == 0:
        return payment * periods
    return payment * (1 - (1 + rate)**-periods) / rate

def calculate_payment(pv, rate, periods):
    """Calculate payment given present value"""
    if rate == 0:
        return pv / periods
    return pv * rate / (1 - (1 + rate)**-periods)
```

---

# College Planning and Student Loans

---

# Example 1: College Tuition Planning

Calculate monthly savings needed for future college expenses:
- Expected college cost: $200,000 in 10 years
- Annual interest rate: 5%
- Monthly savings plan

---

# College Cost Considerations

1. **Rising Tuition Costs**
   - Average annual increase: 7-8%
   - Outpaces general inflation
   - Varies by institution type

2. **Additional Expenses**
   - Room and board
   - Books and supplies
   - Technology fees
   - Living expenses

---

# Python Implementation

```python
future_college_cost = 200000
rate_annual = 0.05
rate_monthly = rate_annual/12
periods = 10 * 12  # 10 years of monthly savings

# Calculate present value needed
pv = future_college_cost / (1 + rate_monthly)**periods
# Calculate required monthly savings
monthly_savings = calculate_payment(pv, rate_monthly, periods)

print(f"Required monthly savings: ${monthly_savings:.2f}")
```

---

# Example 2: Student Loan Payments

Calculate monthly payment for a $50,000 student loan:
- Federal loan rate: 4.99% (2023-2024), this is nominal rate, compounded monthly 
    $$i^{(12)} = 4.99\%$$
- Standard repayment term: 10 years
- Monthly payments

---

# Python Implementation


```python
loan_amount = 50000
rate_annual = 0.0499
rate_monthly = rate_annual/12
periods = 10 * 12  # 10 years of monthly payments

monthly_payment = calculate_payment(loan_amount, 
                                 rate_monthly, 
                                 periods)
print(f"Monthly payment: ${monthly_payment:.2f}")
```


---

# Questions for YOU to Consider

1. How much should your parents save monthly to afford your tuition?
2. How much should you borrow?
3. What's a reasonable monthly payment for your loan?

The above questions are based on making assumptions about the future, like:
- Which school you will attend?
- When do you first start college?
- Tuition amount (inflation?)
- Interest rate on loan
- Interest rate on savings
- Do you have other things to consider?

---

# Making Assumptions

Making assumptions about the future is a key part of financial planning. It is a trade-off between:

- Oversimplifying and ignoring important details
- Overcomplicating and making it impossible to make a decision

