import streamlit as st
st.set_page_config(page_title="Virtual Labs NSSCE", page_icon="🐍", layout= "wide")
st.title("Tutorials")

import streamlit as st

topics = (
    'Strings', "Arithematic Operations", "Conditional Statements" , "For Loop", "While Loop", "Functions"
)

selected_topic = st.selectbox('**Select a Topic You Wish To Learn**', topics)
st.divider()

if selected_topic == "Strings":

    st.markdown("# String Basics in Python")

    st.write("In Python, a string is a sequence of characters enclosed within single ('), double (\"), or triple "
             "(''' or \"\"\") quotes. It can include letters, numbers, symbols, and spaces.")
    st.write("")
    st.markdown("### Various Aspects of Strings in Python")

    st.write("1. **String Creation and Basics:**")
    st.write("Strings are created using single ('), double (\"), or triple (''' or \"\"\") quotes.")
    st.write("Strings are immutable, meaning you cannot change individual characters once a string is created.")
    st.code(
        '''
        string_single = 'Hello'
        string_double = "Python"
    ''')
    st.divider()

    st.write("2. **Indexing and Slicing:**")
    st.write("Access individual characters using indexing (zero-based).")
    st.write("Slicing allows you to extract a portion of the string.")
    st.code(
        '''
        text = "Python"
        first_char = text[0] # P
        substring = text[1:4] # yth
        '''
    )
    st.divider()

    st.write("3. **String Operations:**")
    st.write("Concatenation: Combine strings using the + operator.")
    st.write("Repetition: Repeat a string using the * operator.")
    st.code(
        '''
        str1 = "Hello"
        str2 = "World"
        result = str1 + " " + str2 # Hello World
        repeated_str = str1 * 3 # HelloHelloHello
        '''
    )
    st.divider()

    st.write("4. **String Methods:**")
    st.write("Python provides numerous built-in methods for string manipulation.")
    st.write("Examples include upper(), lower(), len(), replace(), find(), count(), split(), strip(), and more.")
    st.code(
        '''
        message = "Hello, Python!"
        uppercase_message = message.upper() # HELLO, PYTHON!
        replaced_message = message.replace('o', '0') # Hell0, Pyth0n!
        '''
    )
    st.divider()

    st.write("5. **Escape Characters:**")
    st.write("Use escape characters to include special characters in strings.")
    st.code(
        '''
        special_string = "This is a line.\\nThis is a new line."
        '''
    )
    st.divider()

    st.write("6. **String Formatting:**")
    st.write("Format strings using the format() method or f-strings (formatted string literals).")
    st.code(
        '''
        name = "Alice"
        age = 25
        formatted_string = "My name is {} and I am {} years old.".format(name, age)
        # or using f-string
        f_string = f"My name is {name} and I am {age} years old."
        '''
    )
    st.divider()

if selected_topic == "Arithematic Operations":

    st.markdown("# Arithmetic Operations in Python")
    st.write("")
    st.write(
        "Python provides a variety of arithmetic operators that you can use to perform basic arithmetic operations.")
    st.write("")
    st.write("Here are the main arithmetic operators in Python:")

    arithmetic_operators = [
        ("Addition (+)", "Adds two numbers.", '''Python\nresult = 10 + 5\n'''),
        ("Subtraction (-)", "Subtracts the right operand from the left operand.", '''Python\nresult = 10 - 5\n'''),
        ("Multiplication (*)", "Multiplies two numbers.", '''Python\nresult = 10 * 5\n'''),
        ("Division (/)", "Divides the left operand by the right operand.", '''Python\nresult = 10 / 5\n'''),
        ("Floor Division (//)",
         "Divides the left operand by the right operand and returns the largest integer less than or equal to the result.",
         '''Python\nresult = 10 // 3\n'''),
        ("Modulus (%)", "Returns the remainder when the left operand is divided by the right operand.",
         '''Python\nresult = 10 % 3\n'''),
        ("Exponentiation (**)", "Raises the left operand to the power of the right operand.",
         '''Python\nresult = 2 ** 3 # 2 raised to the power of 3\n'''),
    ]

    for operator, description, example in arithmetic_operators:
        st.write(f"**{operator}:** {description}")
        st.code(example)

    st.write("Here's a simple example combining these operators:")
    st.code('''
    python
    a = 10
    b = 3
    addition_result = a + b
    subtraction_result = a - b
    multiplication_result = a * b
    division_result = a / b
    floor_division_result = a // b
    modulus_result = a % b
    exponentiation_result = a ** b
    print("Addition:", addition_result)
    print("Subtraction:", subtraction_result)
    print("Multiplication:", multiplication_result)
    print("Division:", division_result)
    print("Floor Division:", floor_division_result)
    print("Modulus:", modulus_result)
    print("Exponentiation:", exponentiation_result)
    ''')

    st.write("This will be the output:")
    st.code('''
    Addition: 13
    Subtraction: 7
    Multiplication: 30
    Division: 3.3333333333333335
    Floor Division: 3
    Modulus: 1
    Exponentiation: 1000
    ''')

if selected_topic == "Conditional Statements":
    import streamlit as st

    st.markdown("# If-Else Conditionals in Python")

    st.write("Conditional statements in Python allow you to make decisions based on certain conditions. The `if`, "
             "`elif` (else if), and `else` statements are used for this purpose.")

    st.write("Here's an example of the basic syntax:")

    st.code(
        '''python
        x = 10
        if x > 5:
            print("x is greater than 5")
        else:
            print("x is less than or equal to 5")
        '''
    )

    st.write("\n")

    st.write("1. **If Statement:**")
    st.write("`if` statements are used to execute a block of code only if the specified condition is true.")

    st.write("\n")

    st.write("2. **If-Else Statement:**")
    st.write("`else` statements are used to execute a block of code if the condition in the `if` statement is false.")

    st.write("\n")

    st.write("3. **If-Elif-Else Statement:**")
    st.write("`elif` statements are used to check multiple conditions.")
    st.divider()
    st.write("Example of multiple conditions:")

    st.code(
        '''python
        x = 10
        if x > 5:
            print("x is greater than 5")
        elif x == 5:
            print("x is equal to 5")
        else:
            print("x is less than 5")
        '''
    )

    st.write("\n")
    st.divider()
    st.write(
        "Nested `if` statements are also possible where an `if` statement is present inside another `if` or `else` block.")

    st.write("Example of nested `if` statements:")

    st.code(
        '''python
        x = 10
        if x > 5:
            if x % 2 == 0:
                print("x is greater than 5 and even")
            else:
                print("x is greater than 5 and odd")
        else:
            print("x is less than or equal to 5")
        '''
    )
    st.divider()

if selected_topic == "For Loop":
    st.markdown("# For Loops in Python")

    st.write("In Python, a `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) or "
             "other iterable objects.")
    st.divider()
    st.write("Here's an example of the basic syntax:")

    st.code(
        '''python
        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            print(fruit)
        '''
    )

    st.write("\n")

    st.write("#### 1.Iterating Through a List:")
    st.write("Using a `for` loop to iterate through the elements of a list.")

    st.write("Example:")

    st.code(
        '''python
        colors = ["red", "green", "blue"]
        for color in colors:
            print(color)
        '''
    )

    st.write("\n")
    st.divider()

    st.write("#### 2.Iterating Through a String:")
    st.write("Using a `for` loop to iterate through the characters of a string.")

    st.write("Example:")

    st.code(
        '''python
        text = "Python"
        for char in text:
            print(char)
        '''
    )

    st.write("\n")
    st.divider()

    st.write("#### 3.Using Range in For Loops:")
    st.write("Using the `range()` function to generate a sequence of numbers for iteration.")

    st.write("Example:")

    st.code(
        '''python
        for i in range(5):
            print(i)
        '''
    )

    st.write("\n")
    st.divider()

    st.write("#### 4.Nested For Loops:")
    st.write("Using multiple `for` loops, where one loop exists inside another loop.")

    st.write("Example:")

    st.code(
        '''python
        for i in range(3):
            for j in range(2):
                print(f"({i}, {j})")
        '''
    )
    st.divider()

if selected_topic == "While Loop":

    st.markdown("# While Loops in Python")

    st.write("In Python, a `while` loop repeatedly executes a block of code as long as the specified condition "
             "remains True.")

    st.write("Here's an example of the basic syntax:")

    basic_syntax = '''python
    i = 1
    while i <= 5:
        print(i)
        i += 1
    '''

    st.code(basic_syntax)

    st.write("\n")

    st.write("### Exploring While Loops")

    st.write("#### 1. Basic While Loop:")
    st.write("Using a `while` loop to iterate and print numbers.")

    st.write("```python\n"
             "i = 1\n"
             "while i <= 5:\n"
             "    print(i)\n"
             "    i += 1\n"
             "```")

    st.write("\n")

    st.write("#### 2. Infinite While Loop with Break:")
    st.write(
        "An example of using a `while` loop that runs indefinitely until a condition is met to break out of the loop.")

    st.write("```python\n"
             "n = 1\n"
             "while True:\n"
             "    print(n)\n"
             "    n += 1\n"
             "    if n > 5:\n"
             "        break\n"
             "```")

    st.write("\n")

    st.write("#### 3. Using While Loop with Else Block:")
    st.write("The `else` block will execute when the while loop condition becomes false.")

    st.write("```python\n"
             "i = 1\n"
             "while i <= 3:\n"
             "    print(i)\n"
             "    i += 1\n"
             "else:\n"
             "    print('The loop condition is now False.')\n"
             "```")

    st.write("\n")

    st.write("#### 4. Nested While Loops:")
    st.write("Using one `while` loop inside another `while` loop.")

    st.write("```python\n"
             "i = 1\n"
             "while i <= 3:\n"
             "    j = 1\n"
             "    while j <= 2:\n"
             "        print(f'({i}, {j})')\n"
             "        j += 1\n"
             "    i += 1\n"
             "```")

    st.write("\n")

    st.write("#### 5. While Loop with User Input:")
    st.write("An example of a `while` loop that accepts user input until a specific condition is met.")

    st.write("```python\n"
             "password = 'streamlit'\n"
             "while True:\n"
             "    user_input = input('Enter the password: ')\n"
             "    if user_input == password:\n"
             "        print('Password correct. Access granted!')\n"
             "        break\n"
             "    else:\n"
             "        print('Password incorrect. Try again.')\n"
             "```")

    st.write("\n")

    st.write("Feel free to modify or extend these examples to explore while loops further in Python!")

if selected_topic == "Functions":
    import streamlit as st

    st.markdown("# Python Functions")

    st.write("Functions in Python are blocks of organized, reusable code used for performing a single, specific task.")

    st.write("Here's an example of defining a basic function in Python:")

    basic_function = '''python
    def greet():
        print("Hello, welcome to Python functions!")
    '''

    st.code(basic_function)

    st.write("\n")

    st.write("### Exploring Python Functions")

    st.write("#### 1. Defining a Function:")
    st.write("Syntax to define a function in Python:")

    st.write("```python\n"
             "def function_name(parameters):\n"
             "    # function body\n"
             "    # perform tasks\n"
             "    # optional return statement\n"
             "```")

    st.write("Example of a function that greets a user:")

    st.write("```python\n"
             "def greet(name):\n"
             "    print(f\"Hello, {name}! Welcome to Python functions.\")\n"
             "```")

    st.write("\n")

    st.write("#### 2. Function Call:")
    st.write("Using a defined function by calling it with appropriate arguments.")

    st.write("```python\n"
             "greet('Alice')\n"
             "```")

    st.write("\n")

    st.write("#### 3. Function with Return Statement:")
    st.write("Returning a value from a function using the `return` statement.")

    st.write("```python\n"
             "def square(num):\n"
             "    return num * num\n"
             "```")

    st.write("\n")

    st.write("#### 4. Default and Keyword Arguments:")
    st.write("Defining default values for function parameters and using keyword arguments.")

    st.write("```python\n"
             "def greet_user(name='Guest'):\n"
             "    print(f\"Hello, {name}!\")\n"
             "```")

    st.write("```python\n"
             "greet_user()\n"
             "greet_user('John')\n"
             "```")

    st.write("\n")

    st.write("#### 5. Arbitrary Arguments (*args) and Keyword Arguments (**kwargs):")
    st.write("Handling an arbitrary number of arguments and keyword arguments in functions.")

    st.write("```python\n"
             "def display_info(*args, **kwargs):\n"
             "    print('Positional Arguments (args):', args)\n"
             "    print('Keyword Arguments (kwargs):', kwargs)\n"
             "```")

    st.write("```python\n"
             "display_info('Alice', 25, country='USA', city='New York')\n"
             "```")

    st.write("\n")

    st.write("#### 6. Nested Functions:")
    st.write("Defining functions inside other functions.")

    st.write("```python\n"
             "def outer_function(x):\n"
             "    def inner_function(y):\n"
             "        return y * y\n"
             "    return inner_function(x)\n"
             "```")

    st.write("\n")

    st.write("Python functions are versatile and crucial for organizing code. Feel free to experiment and "
             "explore more functionalities!")
