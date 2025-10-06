# 🧩 Week 2 – Variables, Operators, and Conditions

**Module:** CO1404 / CO1456 – Introduction to Programming  
**Topic:** Core Python concepts – Variables, Operators, and Conditional Logic  

---

## 🧠 Learning Goals

- Understand what variables are and how to use them.
- Learn about data types: integers, floats, strings, and booleans.
- Use arithmetic and comparison operators.
- Build logic using `if`, `elif`, and `else` statements.
- Combine expressions with logical operators: `and`, `or`, `not`.

---

## 💻 Key Concepts

| Concept | Example | Description |
|----------|----------|-------------|
| Variable assignment | `x = 10` | Stores data in memory |
| Arithmetic operators | `+`, `-`, `*`, `/`, `//`, `%` | Perform math operations |
| Comparison operators | `==`, `!=`, `<`, `>`, `<=`, `>=` | Compare values |
| Logical operators | `and`, `or`, `not` | Combine conditions |
| Conditional structure | `if x > 0: print("Positive")` | Controls program flow |

---

## 🧮 Example Exercises

### 1. Basic Calculator
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
```

### 2. Even or Odd Checker
```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### 3. Temperature Classification
```python
temp = float(input("Enter temperature: "))

if temp > 30:
    print("It's hot!")
elif temp > 20:
    print("Nice weather.")
else:
    print("It's cold.")
```

---

## 🧩 Summary

By the end of Week 2, you should be able to:
- Store and manipulate user input with variables.
- Perform mathematical and logical operations.
- Use conditional statements to make decisions.
- Write small, functional programs using control flow.

---

✅ **Tip:** Try chaining multiple conditions using `and` / `or` for practice — it’ll help with more complex tasks later on.
