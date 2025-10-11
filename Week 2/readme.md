<h1 align="center">🧩 Week 2 ``day 1`` – Variables, Operators, and Conditions</h1>

<img src="../assets/weekly_pre_session_tasks.png" alt="Pre-Session Tasks" width="100%" />

- Review lecture notes on variables, operators, and conditional logic.
- Watch the “Intro to Python Variables” and “If Statements” mini-lectures.
- Read through Week 1 reflection and prepare questions for Week 2.
- Install and test PyCharm or your preferred Python IDE. (I am using VS Code instead since I'm petty :3 )

<img src="../assets/learning_objectives.png" alt="Learning Objectives" width="100%" />

- Understand what variables are and how to use them.
- Learn about data types: integers, floats, strings, and booleans.
- Use arithmetic and comparison operators.
- Build logic using `if`, `elif`, and `else` statements.
- Combine expressions with logical operators: `and`, `or`, `not`.

<img src="../assets/key_concepts.png" alt="Key Concepts" width="100%" />

| Concept | Example | Description |
|----------|----------|-------------|
| Variable assignment | `x = 10` | Stores data in memory |
| Arithmetic operators | `+`, `-`, `*`, `/`, `//`, `%` | Perform math operations |
| Comparison operators | `==`, `!=`, `<`, `>`, `<=`, `>=` | Compare values |
| Logical operators | `and`, `or`, `not` | Combine conditions |
| Conditional structure | `if x > 0: print("Positive")` | Controls program flow |

<img src="../assets/examples.png" alt="Examples" width="100%" />

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

<img src="../assets/weekly_tasks.png" alt="Weekly Tasks" width="100%" />

### 🧩 Stage 1 – Core Exercises
- [ ] **Fix the Tax Calculator:**  
  Correct syntax, calculate 20% tax, ask for quantity, and display total:  
  `The price for 4 items is 57.60`
- [ ] **Leap Year Checker:** Add conditions for leap year and same-year comparison.
- [ ] **Integer Division:** Investigate `int(1/2)` issue and fix using floats.

### 🧩 Stage 2 – Extended Tasks
- [ ] **Temperature Conversion:** Convert Celsius → Fahrenheit (`F = C * (9/5) + 32`).
- [ ] **Currency Conversion:** Convert between £ and $, allowing user input for exchange rate.
- [ ] **Maximum Number:** Find the largest of 5 integers using `if` statements.
- [ ] **Sorting Challenge:** Sort 5 integers using only `if` and `if-else` conditions.

<img src="../assets/weekly_lab_notes.png" alt="Weekly Lab Notes" width="100%" />

- Fixed syntax errors in the original tax calculator program so it ran correctly.  
- Updated the code to calculate 20% tax dynamically based on the item price.  
- Added input for the number of items and calculated the total price.  
- Tested different price and quantity combinations to confirm the output was correct.  
- Worked on the **Leap Year** exercise and added an `else` condition for non-leap years.  
- Extended the leap year code to compare the user’s birth year with my own.  
- Experimented with integer vs. float division to understand the `int(1/2)` problem.  
- Completed the **Fahrenheit → Celsius** and **Currency Converter** exercises.  
- Attempted the **Maximum Number** task and started thinking through the sorting logic.  
- Pushed my final working files to my GitHub classroom repository for submission.

<img src="../assets/resources.png" alt="Resources" width="100%" />

- Lecture Notes: *Week 2 – Variables, Operators, and Conditions*
- Python Documentation: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- Real Python: [Python Basics: Variables and Data Types](https://realpython.com/python-variables/)

<img src="../assets/weekly_summary.png" alt="Weekly Summary" width="100%" />

By the end of Week 2, you should be able to:
- Store and manipulate data with variables.
- Use arithmetic and logical operations.
- Implement control flow using `if`, `elif`, and `else`.
- Apply debugging to solve basic errors.
- Structure simple interactive programs.

<img src="../assets/weekly_post_session_tasks.png" alt="Post-Session Tasks" width="100%" />

- Complete any unfinished Stage 2 exercises.
- Refactor code for clarity (add comments, remove redundancy).
- Push your final solutions to your GitHub repository before the next class.
- Review feedback from your tutor and note key improvement points.
