# Python Fundamentals

## Why Python?
Python is one of the world's most popular programming languages in recent years, so why Python?

- Python has a simple syntax relative to most programming languages making it perfect for beginners
- Python is open-source, meaning that it is free to use for both individuals and enterprises
- Python can be used for a wide range of applications, such as web development, data analysis, and machine learning
- Python has an active community of developers, making it likely that one can find support on any problem

## Python Installation
Before you can start programming in Python, you first need to install it on your local machine.

1. **Download Python:**
   - Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - The website will automatically detect your operating system and offer the appropriate download

2. **Run the Installer:**
   - Once the download is complete, open the installer
   - Follow the installation prompts

3. **Confirm Python version:**
    - If on windows, open the powershell app and type:
   ```bash
     python --version
     ```

## PyCharm IDE

To code in Python, you must first install an Integrated Development Environment (IDE). 
In this example we use PyCharm as it is specifically developed for Python code.

### Downloading & Installing PyCharm

1. **Download PyCharm:**
   - Visit the PyCharm website: [https://www.jetbrains.com/pycharm/download/?section=windows](https://www.jetbrains.com/pycharm/download/?section=windows)
   - Download the PyCharm Community Edition for your operating system. You may need to scroll down for this

2. **Run the Installer:**
   - Once the download is complete, open the installer
   - Follow the installation prompts

### How to create a PyCharm Project

Before you start coding, you first want to create a project in PyCharm. This will be where your Python scripts will be held.

- In the top left of the window, there should be 4 horizontal parallel lines
- Click the lines and select "New Project"
- Here you can change the name of your project: "C:\Users\username\PycharmProjects\ProjectName"
- Once the project is created you can right-click the project file on the left to create a new Python file

### Running your first code

Now that you have a Python file, named however you'd like, you can start coding.

- Select the new Python (.py) file, and an area to type text will appear
- The most common introduction to running Python code is a "Hello World!" script:
```python
print("Hello World!")
```

## Commenting code
In Programming, comments are extremely important as they add clarity to your code. This is very helpful for both you and others who may read your code in the future.

- The simplest kind of comments are single-line comments which begin with `#`
```python
# This is a single-line comment
print("Hello World!") # You can also write on the same lines as code
```
- Another example of comments is multi-line comments which are made up of triple quotes on separate lines (`"""`)
```python
"""
This is a multi-line comment
which can be used over multiple lines.
"""
print("Hello World!") 
```
## Data Types in Python
There are several data types in Python which are used to store different kinds of values. Some examples of basic data-types in Python are:

- **Integers (`int`)** are whole numbers without any decimal point that can be positive or negative
```python
age = 25  # An integer
temperature = -5  # A negative integer
```
- **Floating-Point numbers (`float`)** are numbers with decimal points. They can represent mathematical real numbers
```python
pi = 3.14159  # A floating-point number
```
- **Strings (`str`)** are sequences of characters which are enclosed in either `'` or `"`. These usually represent text
```python
name = "Alice" # A string in double quotes
hello = 'Hello, World!'  # A string in single quotes
```
- **Booleans (`bool`)** represent either `True` or `False`. This data type is used for logical operations
```python
is_raining = True  # A boolean indicating whether it is raining
is_sunny = False  # A boolean indicating whether it is sunny
```

## Numerical Operators
Python provides the option for a variety of numerical operations. Below are some examples of these operations:

- **Addition (`+`)**: Adds two numbers together
```python
10 + 3 = 13
```
- **Subtraction (`-`)**: Subtracts one number from another
```python
10 - 3 = 7
```
- **Multiplication (`*`)**: Multiplies two numbers together
```python
10 * 3 = 30
```
- **Division (`/`)**: Divides one number by another, always resulting in a float
```python
10 / 3 = 3.3333333333333335
```
- **Modulo (`%`)**: Returns the remainder of the division of two numbers
```python
10 % 3 = 1 # As 3 goes into 10 3 times with remainder 1
```

## String Basics
In Python, it is important to know that strings are sequences of Unicode characters. For example to print `"a"` we can use the Unicode code point:
```python
print(u'\u0061') # This prints the letter 'a'
```

Since strings are ordered sequences of characters, you can utilise "indexing" to select specific parts of the sequence. Python starts counting from 0, meaning that index 0 will be the first character in the string:
```python
text = "Hello, World!"

# Accessing characters by index
first_char = text[0]   # 'H'
last_char = text[-1]   # '!' - Negative values will count backwards from the first character
illegal_char = text[15] # This will return an indexing error are no characters with index 15 here
```
Another useful aspect of strings is the `len` function, which returns the length of a string:
```python
print(len("Hello World!")) # Prints 12, as there are 12 characters, including spaces
```

## Boolean & Equality Operators
In Python, **boolean** and **equality** operators are used to work with the boolean data type (True or False). Some examples of operators are given below:

- `==`: Checks if two values are equal
```python
print(10 == 10) # Prints True
print(10 == 6) # Prints False
```
- `!=`: Checks if two values are not equal
```python
print(10 == 10) # Prints False
print(10 == 6) # Prints True
```
- `>`: Checks if the left value is greater than the right value
```python
print(10 > 10) # Prints False
print(10 > 6) # Prints True
```
- `<`: Checks if the left value is less than the right value
```python
print(10 < 10) # Prints False
print(6 < 10) # Prints True
```
- `>=`: Checks if the left value is greater than or equal to the right value
```python
print(10 >= 10) # Prints True
print(10 >= 6) # Prints True
```
- `<=`: Checks if the left value is less than or equal to the right value
```python
print(10 <= 10) # Prints True
print(10 <= 6) # Prints False
```

Another quality of booleans that is very useful is that Python recognises anything as True, except 0. To illustrate here are some examples:
```python
print(bool(0)) # Prints False
print(bool(1)) # Prints True
print(bool(-1)) # Prints True
print(bool("hi")) # Prints True
```
## Variables
In Python, a **variable** is used to store data values. Python automatically assigns data types to variables, meaning it is not mandatory to explicitly state the data type.<br>
To create a variable, simply assign a value to a name using `=`.

```python
age = 25          # Integer variable
name = "Alice"    # String variable
height = 5.9      # Float variable
is_raining = True # Boolean variable
```
There are various variable naming rules, such as:
- The names must start with letters or an underscore (`_`)
- Names can include numbers but not at the beginning
- Variable names are case-sensitive, meaning `age != Age`

As Python runs line-by-line, from top to bottom, variables can be updated by reassigning their value:
```python
x = 10
print(x) # prints 10

x = 20 # Reassigns x to 20
print(x) # prints 20
```

## More on Strings
