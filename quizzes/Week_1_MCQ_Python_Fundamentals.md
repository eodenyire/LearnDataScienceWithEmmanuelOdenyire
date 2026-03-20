# Week 1 MCQ Quiz: Python Fundamentals

**Phase 1 | Month 1 | Week 1**  
**Format:** Multiple Choice Questions (MCQ)  
**Questions:** 35 | **Time:** 60 minutes  
**Passing Score:** 70% (25/35)

---

## Instructions

- Read each question carefully
- Choose the BEST answer
- Answers are at the bottom of this file
- Review the relevant notebook for any questions you get wrong

---

## Section A: Variables and Data Types (Questions 1–10)

**1.** What is the output of the following code?
```python
x = 5
y = 2
print(x // y, x % y)
```
- A) `2 1`
- B) `2.5 1`
- C) `2 0`
- D) `3 1`

**2.** Which of the following correctly declares a float in Python?
- A) `x = 5`
- B) `x = 5.0`
- C) `x = '5.0'`
- D) `x = int(5)`

**3.** What is the type of `result` after: `result = 3 + 4.0`?
- A) `int`
- B) `float`
- C) `str`
- D) `complex`

**4.** What does `type([1, 2, 3])` return?
- A) `list`
- B) `<class 'list'>`
- C) `array`
- D) `tuple`

**5.** Which operator is used for **exponentiation** in Python?
- A) `^`
- B) `**`
- C) `^^`
- D) `exp()`

**6.** What is the value of `bool(0)` in Python?
- A) `True`
- B) `False`
- C) `0`
- D) `None`

**7.** Which of the following is a **valid** Python variable name?
- A) `2score`
- B) `score-2`
- C) `score_2`
- D) `score 2`

**8.** What is the output of: `print(10 != 10)`?
- A) `True`
- B) `False`
- C) `10`
- D) `Error`

**9.** What is `type(None)` in Python?
- A) `<class 'NoneType'>`
- B) `<class 'null'>`
- C) `<class 'undefined'>`
- D) `<class 'void'>`

**10.** Which statement correctly swaps `a` and `b`?
- A) `temp = a; a = b; b = temp`
- B) `a, b = b, a`
- C) Both A and B
- D) Neither

---

## Section B: Control Flow (Questions 11–20)

**11.** What is the output of:
```python
x = 10
if x > 5:
    print('big')
elif x > 0:
    print('small')
else:
    print('zero')
```
- A) `big`
- B) `small`
- C) `zero`
- D) `big` and `small`

**12.** What does `range(1, 10, 2)` produce?
- A) `[1, 3, 5, 7, 9]`
- B) `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- C) `[2, 4, 6, 8, 10]`
- D) `[1, 3, 5, 7]`

**13.** What keyword immediately exits a loop?
- A) `exit`
- B) `stop`
- C) `break`
- D) `return`

**14.** What does `continue` do in a loop?
- A) Exits the loop
- B) Skips to the next iteration
- C) Pauses the loop
- D) Restarts the loop

**15.** What is the output of:
```python
for i in range(3):
    if i == 1:
        continue
    print(i)
```
- A) `0 1 2`
- B) `0 2`
- C) `1 2`
- D) `0`

**16.** Which is the correct syntax for a while loop?
- A) `while x > 0 do:`
- B) `while(x > 0):`
- C) `while x > 0:`
- D) `loop while x > 0:`

**17.** What is the output of:
```python
x = 0
while x < 3:
    x += 1
print(x)
```
- A) `0`
- B) `2`
- C) `3`
- D) `4`

**18.** What is a list comprehension that generates `[0, 2, 4, 6, 8]`?
- A) `[x for x in range(10)]`
- B) `[x for x in range(10) if x % 2 == 0]`
- C) `[2*x for x in range(5)]`
- D) Both B and C

**19.** What does the `pass` statement do?
- A) Exits the function
- B) Does nothing (placeholder)
- C) Skips to next iteration
- D) Prints nothing

**20.** What is the output of `print(5 > 3 and 2 < 1)`?
- A) `True`
- B) `False`
- C) `Error`
- D) `None`

---

## Section C: Strings and I/O (Questions 21–28)

**21.** What is the output of `'hello'.upper()`?
- A) `hello`
- B) `HELLO`
- C) `Hello`
- D) `hELLO`

**22.** Which method splits a string into a list?
- A) `str.cut()`
- B) `str.divide()`
- C) `str.split()`
- D) `str.break()`

**23.** What is the output of `f'{3 * 4}'`?
- A) `3 * 4`
- B) `12`
- C) `'12'`
- D) Error

**24.** What does `'  hello  '.strip()` return?
- A) `'  hello  '`
- B) `'hello'`
- C) `' hello '`
- D) `'hello  '`

**25.** What is the length of `'data science'`?
- A) `11`
- B) `12`
- C) `13`
- D) `10`

**26.** What is `'abc'[1]`?
- A) `a`
- B) `b`
- C) `c`
- D) Error

**27.** What is `'hello'[-1]`?
- A) `h`
- B) `e`
- C) `o`
- D) Error

**28.** What does `','.join(['a', 'b', 'c'])` return?
- A) `'a b c'`
- B) `'a,b,c'`
- C) `['a,b,c']`
- D) Error

---

## Section D: Python Concepts (Questions 29–35)

**29.** Which function returns the number of items in a list?
- A) `count()`
- B) `size()`
- C) `len()`
- D) `num()`

**30.** What is `print(type(3.14))`?
- A) `int`
- B) `float`
- C) `<class 'float'>`
- D) `number`

**31.** Which is the correct way to get user input in Python 3?
- A) `x = raw_input()`
- B) `x = input()`
- C) `x = scanf()`
- D) `x = read()`

**32.** What is the result of `max([3, 1, 4, 1, 5, 9, 2, 6])`?
- A) `1`
- B) `3`
- C) `9`
- D) `6`

**33.** What does `sorted([3, 1, 2], reverse=True)` return?
- A) `[1, 2, 3]`
- B) `[3, 2, 1]`
- C) `[2, 1, 3]`
- D) Error

**34.** What is `sum([1, 2, 3, 4, 5])`?
- A) `10`
- B) `15`
- C) `12`
- D) `5`

**35.** What does `enumerate(['a', 'b', 'c'])` give?
- A) `[0, 1, 2]`
- B) `[('a', 0), ('b', 1), ('c', 2)]`
- C) `[(0, 'a'), (1, 'b'), (2, 'c')]`
- D) `['a', 'b', 'c']`

---

## Answer Key

| Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A | 8 | B | 15 | B | 22 | C | 29 | C |
| 2 | B | 9 | A | 16 | C | 23 | B | 30 | C |
| 3 | B | 10 | C | 17 | C | 24 | B | 31 | B |
| 4 | B | 11 | A | 18 | D | 25 | B | 32 | C |
| 5 | B | 12 | A | 19 | B | 26 | B | 33 | B |
| 6 | B | 13 | C | 20 | B | 27 | C | 34 | B |
| 7 | C | 14 | B | 21 | B | 28 | B | 35 | C |

---

## Score Interpretation

| Score | Percentage | Interpretation |
|-------|------------|----------------|
| 32–35 | 91–100% | 🏆 Excellent — Ready to advance |
| 28–31 | 80–90% | ✅ Good — Minor review needed |
| 25–27 | 71–79% | ⚠️ Pass — Review key areas |
| Below 25 | <70% | ❌ Retake — Review all of Week 1 |

**Review Resources:** [Week 1 Notebooks](../Phase_1_Foundations_Python_and_Math/Month_01_Python_Basics/Week_1_Python_Fundamentals/)
