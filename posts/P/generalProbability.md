# Question 1
An insurer offers a health plan to the employees of a large company. As part of this plan, the individual employees may choose exactly two of the supplementary converages A, B, and C, or they may choose no supplementary coverage. The proportions of the company's employees that choose coverages A, B, and C and 1/4, 1/3, and 5/12, respectively.

Determine the probability that a randomly chosen employee will choose no supplementary coverage.

# Solution 1

Let's analyze this step by step:

1) Given information:
   - Employees can choose exactly two coverages from A, B, and C, or choose no coverage
   - Proportion choosing coverage A: 1/4
   - Proportion choosing coverage B: 1/3
   - Proportion choosing coverage C: 5/12

2) Let's denote events:
   - Let event A = "employee chooses coverage A"
   - Let event B = "employee chooses coverage B"
   - Let event C = "employee chooses coverage C"
   - Let event N = "employee chooses no supplementary coverage"

3) We need to find P(N) = probability of choosing no supplementary coverage

4) Since an employee chooses either exactly 2 coverages or no coverage:
   - The only possible combinations are:
     * A and B together
     * A and C together
     * B and C together
     * No coverage at all

5) We can use the inclusion-exclusion principle for the probability of choosing any coverage:
   P(A ∪ B ∪ C) = P(A) + P(B) + P(C) - P(A ∩ B) - P(A ∩ C) - P(B ∩ C) + P(A ∩ B ∩ C)

6) Since an employee can choose at most 2 coverages, P(A ∩ B ∩ C) = 0

7) Let's denote:
   - P(A ∩ B) = probability of choosing both A and B
   - P(A ∩ C) = probability of choosing both A and C
   - P(B ∩ C) = probability of choosing both B and C

8) These intersections represent the possible pairs, and since every employee with coverage must choose exactly 2, we have:
   P(A ∩ B) + P(A ∩ C) + P(B ∩ C) = 1 - P(N)

9) We also know that:
   - P(A) = 1/4 = P(A ∩ B) + P(A ∩ C)
   - P(B) = 1/3 = P(A ∩ B) + P(B ∩ C)
   - P(C) = 5/12 = P(A ∩ C) + P(B ∩ C)

10) Adding these three equations:
    P(A) + P(B) + P(C) = 2[P(A ∩ B) + P(A ∩ C) + P(B ∩ C)]
    
    1/4 + 1/3 + 5/12 = 2(1 - P(N))
    
    Converting to a common denominator:
    3/12 + 4/12 + 5/12 = 2(1 - P(N))
    12/12 = 2(1 - P(N))
    1 = 2(1 - P(N))
    1/2 = 1 - P(N)
    P(N) = 1 - 1/2 = 1/2

Therefore, the probability that a randomly chosen employee will choose no supplementary coverage is 1/2 or 0.5.






