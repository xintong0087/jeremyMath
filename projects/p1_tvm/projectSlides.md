---
marp: true
theme: default
paginate: true
---

# Time Value of Money Project
## Handling Multiple Cash Flows

---

# Types of Cash Flow Series

1. **Single Payment**
   - One-time payment
   - Simple FV/PV calculation

2. **Multiple Payments**
   - Different amounts at different times
   - Need to handle each payment separately

3. **Regular Series**
   - Annuities (equal periodic payments)
   - Structured payment patterns

---

# Handling Multiple Cash Flows

Example Cash Flow Series:
- $100 today
- $150 in 2 years
- $200 in 5 years
- $75 in 7 years

We need to:
1. Create a timeline
2. Calculate each flow separately
3. Sum the results

---

# Python Data Structure for Cash Flows

```python
# Using a list of dictionaries
cash_flows = [
    {"amount": 100, "time": 0},
    {"amount": 150, "time": 2},
    {"amount": 200, "time": 5},
    {"amount": 75, "time": 7}
]

# Or using pandas DataFrame
import pandas as pd
df = pd.DataFrame({
    'amount': [100, 150, 200, 75],
    'time': [0, 2, 5, 7]
})
```

---

# Calculating Future Value of Multiple Flows

```python
def calculate_future_values(cash_flows, rate, target_time):
    """
    Calculate future value of multiple cash flows
    
    Args:
        cash_flows: List of dicts with amount and time
        rate: Interest rate per period
        target_time: Future point to calculate value
    """
    total_fv = 0
    for flow in cash_flows:
        time_difference = target_time - flow['time']
        fv = flow['amount'] * (1 + rate) ** time_difference
        total_fv += fv
    return total_fv
```

---

# Calculating Present Value of Multiple Flows

```python
def calculate_present_values(cash_flows, rate):
    """
    Calculate present value of multiple cash flows
    
    Args:
        cash_flows: List of dicts with amount and time
        rate: Interest rate per period
    """
    total_pv = 0
    for flow in cash_flows:
        pv = flow['amount'] / (1 + rate) ** flow['time']
        total_pv += pv
    return total_pv
```

---

# Using Pandas for Calculations

```python
import pandas as pd
import numpy as np

def analyze_cash_flows(df, rate):
    """Analyze cash flows using pandas"""
    # Calculate PV for each flow
    df['present_value'] = df['amount'] / (1 + rate) ** df['time']
    
    # Calculate FV at the latest time
    max_time = df['time'].max()
    df['future_value'] = df['amount'] * (1 + rate) ** (max_time - df['time'])
    
    return df
```

---

# Visualizing Cash Flows

```python
import matplotlib.pyplot as plt

def plot_cash_flows(cash_flows):
    times = [flow['time'] for flow in cash_flows]
    amounts = [flow['amount'] for flow in cash_flows]
    
    plt.figure(figsize=(10, 6))
    plt.stem(times, amounts)
    plt.title('Cash Flow Timeline')
    plt.xlabel('Time (years)')
    plt.ylabel('Amount ($)')
    plt.grid(True)
    plt.show()
```

---

# Example Analysis

```python
# Define cash flows
flows = [
    {"amount": 1000, "time": 0},
    {"amount": -500, "time": 2},
    {"amount": 750, "time": 3},
    {"amount": 1200, "time": 5}
]

# Calculate values
rate = 0.05  # 5% interest
pv = calculate_present_values(flows, rate)
fv = calculate_future_values(flows, rate, 5)

print(f"Present Value: ${pv:.2f}")
print(f"Future Value at year 5: ${fv:.2f}")
```

---

# Handling Different Scenarios

1. **Mixed Cash Flows**
   - Both positive and negative flows
   - Investments and returns

2. **Irregular Intervals**
   - Varying time periods
   - Non-standard payment dates

3. **Multiple Interest Rates**
   - Different rates for different periods
   - Rate changes over time

---

# Advanced Features

1. **Interest Rate Sensitivity**
   ```python
   def sensitivity_analysis(cash_flows, rates):
       results = {}
       for rate in rates:
           results[rate] = calculate_present_values(cash_flows, rate)
       return results
   ```

2. **NPV and IRR Calculations**
   ```python
   from scipy.optimize import newton
   def calculate_irr(cash_flows):
       # Implementation of IRR calculation
   ```

---

# Error Handling and Validation

```python
def validate_cash_flows(cash_flows):
    """Validate cash flow data structure"""
    if not cash_flows:
        raise ValueError("Cash flows cannot be empty")
    
    for flow in cash_flows:
        if 'amount' not in flow or 'time' not in flow:
            raise ValueError("Invalid cash flow format")
        if flow['time'] < 0:
            raise ValueError("Time cannot be negative")
```

---

# Project Implementation Steps

1. **Data Structure Setup**
   - Define cash flow format
   - Create input validation

2. **Core Calculations**
   - PV/FV functions
   - Timeline handling

3. **Analysis Tools**
   - Sensitivity analysis
   - Visualization
   - Summary statistics

---

# Testing Your Implementation

```python
def test_multiple_flows():
    flows = [
        {"amount": 100, "time": 0},
        {"amount": 200, "time": 2}
    ]
    rate = 0.05
    
    # Test PV calculation
    pv = calculate_present_values(flows, rate)
    assert abs(pv - 281.86) < 0.01
    
    # Test FV calculation
    fv = calculate_future_values(flows, rate, 2)
    assert abs(fv - 310.25) < 0.01
```

---

# Practical Applications

1. **Investment Analysis**
   - Compare investment options
   - Calculate returns

2. **Project Evaluation**
   - Capital budgeting
   - Project comparison

3. **Financial Planning**
   - Retirement planning
   - Education funding

---

# Resources and Tools

1. **Python Libraries**
   - NumPy Financial
   - Pandas
   - Matplotlib/Plotly

2. **Documentation**
   - Financial mathematics
   - Python financial libraries

3. **Online Calculators**
   - Verification tools
   - Quick checks

---

# Questions?

Thank you for your attention!

Contact: [Your Contact Information]
