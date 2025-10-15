<h1 align="center">🧩 Week 3 – More Loops & User Input Validation</h1>

<img src="../assets/weekly_pre_session_tasks.png" alt="Pre-Session Tasks" width="100%" />

- Watch lecture videos on `for` loops and input validation.
- Review Week 2’s material on conditionals and iteration.
- Read the lecture notes accompanying this lab sheet.

<img src="../assets/learning_objectives.png" alt="Learning Objectives" width="100%" />

- Understand how to use and control `for` loops in Python.
- Learn how to validate both textual and numeric user input.
- Apply `try-except` blocks for safe error handling.
- Practice combining loops and conditionals for input validation.
- Use Python’s `calendar` and `datetime` libraries for real-world tasks.

<img src="../assets/key_concepts.png" alt="Key Concepts" width="100%" />

| Concept | Example | Description |
|----------|----------|-------------|
| `for` loop | `for i in range(1, 11):` | Iterates over a sequence of numbers or items. |
| `end=' '` | `print(i, end=', ')` | Prints output on one line separated by a character. |
| Input validation | `while True: ... break` | Ensures user input meets criteria before proceeding. |
| `try-except` | `try: int(x)` | Catches and handles invalid user input safely. |
| `calendar.monthrange()` | `calendar.monthrange(2011, 10)` | Returns the number of days in a specific month/year. |
| `datetime.strftime()` | `datetime(2023,10,1).strftime("%B")` | Converts date to readable month/day names. |

<img src="../assets/examples.png" alt="Examples" width="100%" />

### Example 1 – Printing Numbers on One Line
```python
for i in range(1, 11):
    print(i, end=', ')
```

### Example 2 – Validating Yes/No Input
```python
while True:
    choice = input("Are you sure you want to delete the record? (y/n) ").lower()
    if choice in ('y', 'n'):
        break
    print("Sorry, you must answer 'y' or 'n'.")
```

### Example 3 – Validating Numeric Input
```python
while True:
    try:
        year = int(input("Enter your birth year: "))
        if 1900 <= year <= 2011:
            break
        else:
            print("Please enter a year between 1900 and 2011.")
    except ValueError:
        print("That’s not a number, please try again.")
```

### Example 4 – Using the Calendar Library
```python
import calendar

year = int(input("Enter a year: "))
for month in range(1, 13):
    days = calendar.monthrange(year, month)[1]
    print(f"Month {month}\n{days} days\n")
```

<img src="../assets/weekly_tasks.png" alt="Weekly Tasks" width="100%" />

- [ ] Write a `for` loop displaying numbers 1–10 on one line.
- [ ] Display odd numbers (9–49) and even numbers (100–50, reverse).
- [ ] Create a Yes/No input validation program.
- [ ] Implement numeric input validation for a year of birth.
- [ ] Build a simple calculator with validated inputs and multiple operations.
- [ ] Create a prototype calendar program using `calendar` and `datetime`.
- [ ] Stretch Goal: Add a feature to determine the day of the week you were born.

<img src="../assets/weekly_lab_notes.png" alt="Weekly Lab Notes" width="100%" />

- Watch out for infinite loops when validating inputs.
- Remember to use `.lower()` to normalize Yes/No responses.
- `try-except` is essential for catching non-numeric inputs.
- Use `break` carefully — ensure your exit conditions are clear.
- Always test with invalid inputs to “break” your program safely.

<img src="../assets/resources.png" alt="Resources" width="100%" />

- Python documentation: [`calendar`](https://docs.python.org/3/library/calendar.html)
- Python documentation: [`datetime`](https://docs.python.org/3/library/datetime.html)
- Week 3 lecture slides and code samples.
- PyCharm IDE for testing and debugging.

<img src="../assets/weekly_summary.png" alt="Weekly Summary" width="100%" />

**Summary:**  
- Practiced iteration with complex `for` loops.  
- Implemented input validation using `while` loops and exception handling.  
- Built a more interactive calculator program with error-checking.  
- Explored Python’s built-in libraries for date and time processing.  

<img src="../assets/weekly_post_session_tasks.png" alt="Post-Session Tasks" width="100%" />

- Finalize and test all programs thoroughly.
- Push your completed work to GitHub.
- Review code comments for clarity and style.