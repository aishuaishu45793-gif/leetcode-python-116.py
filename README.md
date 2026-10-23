# 🐍 LeetCode Python Practice Programs (116–120)

## 📌 Project Overview

Welcome to my **LeetCode Python Practice Series (116–120)**! 🚀

This repository contains five Python programming exercises designed to improve problem-solving skills, logical thinking, and understanding of fundamental Python concepts.

Each program focuses on a different problem, including character frequency, mathematical operations, list manipulation, and string comparison.

## 🎯 Objectives

* Improve Python programming skills.
* Practice problem-solving and logical thinking.
* Understand lists, strings, dictionaries, and sets.
* Learn mathematical operations in Python.
* Develop clean and readable code.
* Build a consistent coding practice portfolio.

## 📂 Projects Included

| No. | Project Name                           | Description                                             | Main Concepts                |
| --- | -------------------------------------- | ------------------------------------------------------- | ---------------------------- |
| 116 | Count Occurrences of Each Character    | Counts the frequency of each character in a string.     | Strings, dictionaries, loops |
| 117 | GCD of Two Numbers                     | Finds the Greatest Common Divisor of two integers.      | Math module, functions       |
| 118 | Remove Duplicates from a List          | Removes repeated numbers while preserving their order.  | Lists, loops, conditions     |
| 119 | Second Smallest Distinct Number        | Finds the second smallest unique number in a list.      | Sets, sorting, lists         |
| 120 | Check Whether Two Strings Are Anagrams | Checks whether two strings contain the same characters. | Strings, sorting, conditions |

---

# 🟢 Project 116: Count Occurrences of Each Character

### Description

This program counts how many times each character appears in a given string using a Python dictionary.

### Python Code

```python
text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character occurrences:")

for char, count in frequency.items():
    print(char, ":", count)
```

### Example Output

```text
Enter a string: hello
Character occurrences:
h : 1
e : 1
l : 2
o : 1
```

### Concepts Learned

* Strings
* Dictionaries
* Loops
* Conditional statements
* Dictionary methods

---

# 🟢 Project 117: GCD of Two Numbers

### Description

This program calculates the Greatest Common Divisor (GCD) of two integers using Python's built-in `math.gcd()` function.

### Python Code

```python
import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = math.gcd(num1, num2)

print("GCD is:", result)
```

### Example Output

```text
Enter the first number: 48
Enter the second number: 18
GCD is: 6
```

### Concepts Learned

* User input
* Integer conversion
* Importing Python modules
* Mathematical operations
* `math.gcd()`

---

# 🟢 Project 118: Remove Duplicates from a List

### Description

This program removes duplicate numbers from a list while maintaining the original order of the elements.

### Python Code

```python
numbers = list(
    map(int, input("Enter numbers separated by spaces: ").split())
)

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)
```

### Example Output

```text
Enter numbers separated by spaces: 1 2 2 3 4 3 5
List after removing duplicates: [1, 2, 3, 4, 5]
```

### Concepts Learned

* Lists
* Loops
* Conditions
* `map()` and `split()`
* List membership
* `append()`

---

# 🟢 Project 119: Second Smallest Distinct Number

### Description

This program finds the second smallest distinct number in a list.

Duplicate values are removed before sorting the numbers.

### Python Code

```python
numbers = list(
    map(int, input("Enter numbers separated by spaces: ").split())
)

unique_numbers = sorted(set(numbers))

if len(unique_numbers) < 2:
    print("There is no second smallest distinct number.")
else:
    print("Second smallest number:", unique_numbers[1])
```

### Example Output

```text
Enter numbers separated by spaces: 4 2 2 1 3
Second smallest number: 2
```

### Concepts Learned

* Lists
* Sets
* Sorting
* Indexing
* Conditional statements
* Duplicate removal

---

# 🟢 Project 120: Check Whether Two Strings Are Anagrams

### Description

This program checks whether two strings are anagrams.

Anagrams are words or phrases that contain the same characters with the same frequencies, regardless of their order.

For this exercise, spaces and letter case are ignored.

### Python Code

```python
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
```

### Example Output

```text
Enter the first string: Listen
Enter the second string: Silent
The strings are anagrams.
```

### Concepts Learned

* String manipulation
* `lower()`
* `replace()`
* `sorted()`
* Conditional statements
* String comparison

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Code Editor:** Visual Studio Code
* **Version Control:** Git
* **Repository Hosting:** GitHub

## ⚙️ How to Run the Programs

### Step 1: Install Python

Install Python on your computer if it is not already installed.

### Step 2: Open the Project

Open your project folder in Visual Studio Code.

### Step 3: Create Python Files

Create these five files:

```text
116.py
117.py
118.py
119.py
120.py
```

Copy the corresponding program into each file.

### Step 4: Open the Terminal

In VS Code, select **Terminal → New Terminal**.

### Step 5: Run a Program

To run Project 116:

```bash
python 116.py
```

To run Project 117:

```bash
python 117.py
```

To run Project 118:

```bash
python 118.py
```

To run Project 119:

```bash
python 119.py
```

To run Project 120:

```bash
python 120.py
```

Enter the requested input when prompted.

## 📈 Learning Outcomes

By completing these five projects, I have practiced:

* Counting character frequencies using dictionaries.
* Calculating the GCD of two numbers.
* Removing duplicate elements from lists.
* Finding the second smallest distinct number.
* Checking whether strings are anagrams.
* Working with Python's built-in functions and modules.
* Improving logical thinking and debugging skills.

## 🚀 Future Improvements

* Solve more Python and LeetCode problems.
* Explore alternative solutions for each problem.
* Learn data structures and algorithms.
* Improve time and space complexity.
* Practice more string, list, dictionary, and mathematical problems.

## 👩‍💻 Author

**Aishwarya**

Python Programming | LeetCode Practice | Problem Solving

## ⭐ Conclusion

These projects are part of my continuous Python learning journey. Each exercise helps me strengthen my programming fundamentals and prepare for more advanced coding challenges.

I will continue adding new projects as I improve my Python and problem-solving skills.
