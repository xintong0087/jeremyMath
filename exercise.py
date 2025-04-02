# Exercise 11
s = 0
m = 20
lower = 1
upper = 2

for i in range(m):
    s += upper / lower
    lower, upper = upper, lower + upper

print(f"The sum of the first {m} terms of the series is {s}")

# Exercise 12
def calculate_height(n):
    s = 0
    h = 100
    for i in range(n):
        s += h + h * 0.5
        h *= 0.5
    return s

bouncing_times = 100
print(f"The total distance traveled by the ball starting from 100 meters bouncing {bouncing_times} times is {calculate_height(bouncing_times)} meters")

# Exercise 13   
def find_sqrt(a, x):
    
    last_a = 0
    
    while abs(a - last_a) > 0.00001:
        last_a = a
        a = (a + x / a) / 2
    return a

x = 4
a = 25
print(f"The square root of {a} approximated by parameter {x} is {find_sqrt(x, a)}")

# Exercise 14

def draw_triangle(n):
    for i in range(n):
        print("*" * (i + 1))

    for i in range(n - 1):
        print("*" * (n - i - 1))

n = 5
draw_triangle(n)


