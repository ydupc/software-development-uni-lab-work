<p align="center">
  <img src="./assets/banner.png" alt="Week Banner" width="100%" />
</p>

<h1 align="center">🧩 Week 2 – Variables, Operators, and Conditions</h1>

<img src="./assets/learning_objectives.png" alt="Learning Objectives" width="100%" />

- Understand what variables are and how to use them.
- Learn about data types: integers, floats, strings, and booleans.
- Use arithmetic and comparison operators.
- Build logic using `if`, `elif`, and `else` statements.
- Combine expressions with logical operators: `and`, `or`, `not`.

<img src="./assets/key_concepts.png" alt="Key Concepts" width="100%" />

| Concept | Example | Description |
|----------|----------|-------------|
| Variable assignment | `x = 10` | Stores data in memory |
| Arithmetic operators | `+`, `-`, `*`, `/`, `//`, `%` | Perform math operations |
| Comparison operators | `==`, `!=`, `<`, `>`, `<=`, `>=` | Compare values |
| Logical operators | `and`, `or`, `not` | Combine conditions |
| Conditional structure | `if x > 0: print("Positive")` | Controls program flow |

<img src="./assets/examples.png" alt="Examples" width="100%" />

### 1) Basic Calculator
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
```

### 2) Even or Odd Checker
```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### 3) Temperature Classification
```python
temp = float(input("Enter temperature: "))

if temp > 30:
    print("It's hot!")
elif temp > 20:
    print("Nice weather.")
else:
    print("It's cold.")
```

<img src="./assets/weekly_tasks.png" alt="Weekly Tasks" width="100%" />

- [ ] Rework the “tax calculator” to compute 20% tax and multiply by quantity.
- [ ] Write a small program that prints the largest of three numbers.
- [ ] Stretch: add input validation (reject non-numeric input).

<img src="./assets/weekly_lab_notes.png" alt="Weekly Lab Notes" width="100%" />

- Tested input casting with `int()` vs `float()`.
- Noted integer division `//` vs true division `/`.
- Common error: forgetting to convert `input()` to a number.

<img src="./assets/weekly_summary.png" alt="Weekly Summary" width="100%" />

By the end of Week 2, you should be able to:
- Store and manipulate user input with variables.
- Perform mathematical and logical operations.
- Use conditional statements to make decisions.
- Write small, functional programs using control flow.

<img src="./assets/weekly_reflection.png" alt="Weekly Reflection" width="100%" />

- What went well?
- What was tricky?
- What will you try next week?
