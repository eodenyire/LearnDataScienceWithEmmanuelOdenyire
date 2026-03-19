# Phase 1 Quiz: Python & Math

**Instructions**: 25 questions. Time: open book.

---

## Section A: Python (Multiple Choice, 1 point each)

**1.** What is the output of `[x**2 for x in range(5) if x % 2 != 0]`?
- a) `[1, 9, 25]`
- b) `[1, 4, 9, 16]`
- c) `[0, 4, 16]`
- d) `[1, 9]`

**2.** Which data structure offers O(1) average-case lookup by key?
- a) List
- b) Tuple
- c) Dictionary
- d) Set

**3.** What does `@staticmethod` indicate in a Python class?
- a) The method modifies class state
- b) The method takes no instance or class argument
- c) The method is inherited
- d) The method is private

**4.** What is the output of `{'a': 1, 'b': 2}.get('c', 0)`?
- a) `None`
- b) `KeyError`
- c) `0`
- d) `'c'`

---

## Section B: NumPy & Pandas (2 points each)

**5.** What does `np.array([1,2,3]).reshape(3,1)` produce?

**6.** Write a Pandas command to find the mean of column 'price' grouped by column 'category'.

**7.** What is broadcasting in NumPy? Give a brief example.

**8.** How do you select rows where `age > 30` and `city == 'Nairobi'` in a Pandas DataFrame?

---

## Section C: Statistics (3 points each)

**9.** Define Type I and Type II errors in hypothesis testing.

**10.** What is the Central Limit Theorem and why is it important in data science?

**11.** Calculate the Z-score of a value of 75, given mean=60 and std=10.

**12.** Explain the difference between correlation and causation with a real-world example.

---

## Section D: Code (5 points each)

**13.** Write a Python function that takes a list of numbers and returns a dictionary with keys: `mean`, `median`, `std`, `q1`, `q3`.

**14.** Write a Pandas pipeline that reads a CSV, drops rows with missing values in column 'salary', converts 'salary' to log scale, and returns the top 10 highest earners.

---

*Total: 25 points*
