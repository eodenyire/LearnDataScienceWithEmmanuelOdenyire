# Month 1 Continuous Assessment Test (CAT): Python Basics

**Phase 1 | Month 1 | Bootcamp Days 25–28**  
**Type:** Continuous Assessment Test (CAT)  
**Duration:** 4 hours  
**Total Marks:** 100  
**Passing Score:** 60/100

---

## Instructions

1. Complete all sections
2. Write clean, well-documented Python code
3. Test your code before submitting
4. Submit as a Jupyter Notebook (`.ipynb` file)
5. Include your name, student ID, and date in the first cell

---

## Section A: Theory Questions (20 marks)

Answer the following in 2–4 sentences each.

**A1 (4 marks):** What is the difference between a **list** and a **tuple** in Python? When would you prefer to use each?

**A2 (4 marks):** Explain the concept of **scope** in Python. What is the difference between local and global scope? Provide a code example.

**A3 (4 marks):** What is **Object-Oriented Programming (OOP)**? List and briefly explain the 4 pillars of OOP.

**A4 (4 marks):** What is the purpose of exception handling? Explain `try`, `except`, `else`, and `finally` blocks with examples.

**A5 (4 marks):** What is the difference between `==` and `is` operators in Python? Provide examples where they give different results.

---

## Section B: Code Analysis (20 marks)

**B1 (5 marks):** What is the output of the following code? Explain each step.
```python
def mystery(n):
    if n <= 0:
        return 0
    return n + mystery(n - 1)

print(mystery(5))
```

**B2 (5 marks):** What is the output? Identify the design pattern used.
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Done: {result}')
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 4)
```

**B3 (5 marks):** Spot and fix the bug in this code:
```python
class Circle:
    PI = 3.14159
    
    def __init__(radius):  # Bug here
        self.radius = radius
    
    def area():  # Bug here
        return Circle.PI * self.radius ** 2

c = Circle(5)
print(c.area())
```

**B4 (5 marks):** What does the following generator do? Explain step by step.
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
result = [next(gen) for _ in range(10)]
print(result)
```

---

## Section C: Programming Tasks (60 marks)

**C1 (20 marks): Data Science Student Registry**

Build a Python class-based system to manage bootcamp students:

**Requirements:**
1. `Student` class with: `name`, `student_id`, `email`, `join_date`, `scores` (dict of subject→score)
2. `StudentRegistry` class with:
   - `add_student(student)` method
   - `get_student(student_id)` method
   - `top_performers(n=5)` returns top N students by average score
   - `phase_summary(phase)` returns stats for a given phase's scores
   - `export_to_json(filepath)` saves all student data to JSON
   - `load_from_json(filepath)` loads student data from JSON

**Test your implementation with at least 10 students.**

```python
# Your implementation here
```

---

**C2 (20 marks): Text Analysis Pipeline**

Create a functional-style text analysis pipeline using functions, lambda, map/filter:

**Requirements:**
1. `load_text(text)` - receives raw text string
2. `clean_text(text)` - removes punctuation, converts to lowercase
3. `tokenize(text)` - splits into words
4. `remove_stopwords(words, stopwords)` - filters common words
5. `word_frequency(words)` - returns Counter of word frequencies
6. `top_keywords(freq_dict, n=10)` - returns top N words
7. `summarize(text)` - orchestrates the full pipeline

**Test with a data science article excerpt (at least 100 words).**

```python
# Your implementation here
```

---

**C3 (20 marks): Mini Data Analyzer Class**

Build a `MiniDataAnalyzer` class that:

**Requirements:**
1. `load_csv(filepath)` - loads CSV data into a list of dicts
2. `describe(column)` - returns count, mean, median, std, min, max for numeric column
3. `value_counts(column)` - returns frequency of each value in a categorical column
4. `filter_rows(column, condition)` - filters rows based on a lambda condition
5. `sort_by(column, ascending=True)` - sorts data by column
6. `to_json(filepath)` - saves processed data as JSON
7. A `__repr__` showing dataset name, rows, columns

**Use the provided `datasets/sample_sales.csv` dataset.**

```python
# Your implementation here
```

---

## Submission Format

Submit a Jupyter notebook named: `Month01_CAT_[YourStudentID].ipynb`

**Notebook structure:**
1. Cell 1: Student info (name, ID, date)
2. Cell 2+: Theory answers (Section A)
3. Cell 3+: Code analysis (Section B)
4. Cell 4+: Programming tasks (Section C) with markdown explaining your approach

---

## Marking Rubric

### Code Quality (10% of each task)
- Clean, readable code
- Appropriate variable names
- Proper docstrings
- Edge case handling

### Correctness (70% of each task)
- Code runs without errors
- Produces correct output
- All requirements met

### Documentation (20% of each task)
- Markdown cells explaining the approach
- Inline comments where needed
- Test cases included

---

## Resources Allowed
- All Week 1–4 notebooks
- Python official documentation
- Your own notes
- No sharing with other students

*Good luck! Remember: data scientists solve problems with code — show your thinking process.*
