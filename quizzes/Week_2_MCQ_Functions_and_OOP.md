# Week 2 MCQ Quiz: Functions and Object-Oriented Programming

**Phase 1 | Month 1 | Week 2**  
**Format:** Multiple Choice Questions (MCQ)  
**Questions:** 30 | **Time:** 50 minutes  
**Passing Score:** 70% (21/30)

---

## Section A: Functions (Questions 1–12)

**1.** Which keyword is used to define a function in Python?
- A) `function`
- B) `func`
- C) `def`
- D) `define`

**2.** What does a function without a `return` statement return?
- A) `0`
- B) `False`
- C) `None`
- D) Error

**3.** What is the output of:
```python
def add(a, b=10):
    return a + b
print(add(5))
```
- A) `5`
- B) `10`
- C) `15`
- D) Error

**4.** What does `*args` allow in a function?
- A) Keyword arguments only
- B) Any number of positional arguments
- C) Exactly 3 arguments
- D) Named arguments

**5.** What is a lambda function?
- A) A named function
- B) An anonymous single-expression function
- C) A recursive function
- D) A generator function

**6.** What is the output of `(lambda x: x**2)(4)`?
- A) `4`
- B) `8`
- C) `16`
- D) Error

**7.** What does `map(str, [1, 2, 3])` return?
- A) `[1, 2, 3]`
- B) `['1', '2', '3']` (as iterator)
- C) `'123'`
- D) Error

**8.** What is a docstring?
- A) A comment starting with `#`
- B) A string literal as the first statement of a function
- C) A print statement inside a function
- D) A function name

**9.** What is the difference between local and global scope?
- A) Local variables are accessible everywhere; global only inside functions
- B) Global variables are accessible everywhere; local only inside functions
- C) There is no difference
- D) Python has no global scope

**10.** What is `filter(lambda x: x > 0, [-1, 2, -3, 4])`?
- A) `[-1, -3]`
- B) `[2, 4]`
- C) `[-1, 2, -3, 4]`
- D) Error

**11.** What is `@functools.wraps` used for?
- A) To time a function
- B) To preserve the original function's metadata in a decorator
- C) To convert a function to a lambda
- D) To cache function results

**12.** Which is the correct way to import `reduce`?
- A) `from builtins import reduce`
- B) `from functools import reduce`
- C) `import reduce`
- D) `from itertools import reduce`

---

## Section B: Object-Oriented Programming (Questions 13–25)

**13.** What is a class in Python?
- A) A function that returns objects
- B) A blueprint for creating objects
- C) A data type
- D) A module

**14.** What is `__init__` used for?
- A) Destroying objects
- B) Initializing object attributes
- C) Copying objects
- D) Printing objects

**15.** What is `self` in a class method?
- A) A keyword like `this` in Java/C++
- B) A reference to the current instance
- C) The class itself
- D) A global variable

**16.** What does `__str__` define?
- A) How to destroy an object
- B) How to print/display an object
- C) How to compare two objects
- D) How to copy an object

**17.** What does inheritance allow?
- A) A class to use methods and attributes of another class
- B) A function to call itself
- C) A module to import another module
- D) A variable to change type

**18.** What is `super().__init__()` used for?
- A) Calling the parent class constructor
- B) Creating a new instance
- C) Deleting the parent class
- D) Accessing class variables

**19.** What is polymorphism?
- A) Having multiple classes with different names
- B) Ability of different objects to respond to the same method name
- C) Multiple inheritance
- D) Having multiple constructors

**20.** What is encapsulation?
- A) Hiding internal data using access modifiers
- B) Wrapping code in a function
- C) Combining multiple classes
- D) Using decorators

**21.** What is the output of:
```python
class Dog:
    sound = 'Woof'
    def speak(self):
        return self.sound
d = Dog()
print(d.speak())
```
- A) `Dog`
- B) `Woof`
- C) `sound`
- D) Error

**22.** What does `@classmethod` decorator do?
- A) Makes a method static
- B) Passes the class as the first argument instead of the instance
- C) Makes a method private
- D) Makes a method a property

**23.** What is `@property` used for?
- A) To define a constant
- B) To access a method like an attribute
- C) To define a static method
- D) To make a class abstract

**24.** What keyword makes a class abstract in Python?
- A) `abstract`
- B) `interface`
- C) Using `ABC` from `abc` module
- D) Python has no abstract classes

**25.** What is `isinstance(5, int)` result?
- A) `False`
- B) `True`
- C) `int`
- D) Error

---

## Section C: Exceptions and Files (Questions 26–30)

**26.** What keyword catches exceptions?
- A) `catch`
- B) `except`
- C) `handle`
- D) `error`

**27.** What block always executes in try/except?
- A) `else`
- B) `except`
- C) `finally`
- D) `always`

**28.** How do you raise a custom exception?
- A) `throw CustomError()`
- B) `raise CustomError()`
- C) `error CustomError()`
- D) `except CustomError()`

**29.** Which is the best way to open a file?
- A) `f = open('file.txt'); f.read(); f.close()`
- B) `with open('file.txt') as f: f.read()`
- C) `file.open('file.txt')`
- D) `f = read('file.txt')`

**30.** What does `json.dumps({'key': 'val'})` return?
- A) A Python dict
- B) A JSON string
- C) A file
- D) Error

---

## Answer Key

| Q | A | Q | A | Q | A |
|---|---|---|---|---|---|
| 1 | C | 11 | B | 21 | B |
| 2 | C | 12 | B | 22 | B |
| 3 | C | 13 | B | 23 | B |
| 4 | B | 14 | B | 24 | C |
| 5 | B | 15 | B | 25 | B |
| 6 | C | 16 | B | 26 | B |
| 7 | B | 17 | A | 27 | C |
| 8 | B | 18 | A | 28 | B |
| 9 | B | 19 | B | 29 | B |
| 10 | B | 20 | A | 30 | B |
