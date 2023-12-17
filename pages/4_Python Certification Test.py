import streamlit as st
st.set_page_config(page_title="Virtual Labs NSSCE", page_icon="🐍", layout= "wide")

# Define the questions and answer options
questions = [
    {"question": "1.What is the correct way to define a variable in Python?",
     "options": ["var name = value", "name = value", "define name = value"],
     "answer": "name = value"},
    {"question": "2.What is the difference between a single quote and a double quote in Python?",
     "options": ["Single quotes are used for strings, while double quotes are used for integers", "Single quotes are used for strings, while double quotes are used for characters", "Single quotes and double quotes are used interchangeably for strings"],
     "answer": "Single quotes are used for strings, while double quotes are used for characters"},
    {"question": "3.What is the correct way to concatenate two strings?",
     "options": ["string1 + string2", "string1.concat(string2)", "string1 + string2 = new_string"],
     "answer": "string1 + string2"},
    {"question": "4.What is the correct way to access the value of a key in a dictionary?",
     "options": ["dictionary['key']", "dictionary.get('key')", "dictionary.key"],
     "answer": "dictionary['key']"},
    {"question": "5.What is the purpose of the 'None' value in Python?",
     "options": ["To represent an empty value", "To represent a boolean value", "To represent a numerical value"],
     "answer": "To represent an empty value"},
    {"question": "6.What is the difference between an 'if' statement and an 'elif' statement?",
     "options": ["'if' statements are used for conditional execution, while 'elif' statements are used for alternative conditional execution", "'if' statements are used for single conditions, while 'elif' statements are used for multiple conditions", "'if' statements are used for true conditions, while 'elif' statements are used for false conditions"],
     "answer": "'if' statements are used for conditional execution, while 'elif' statements are used for alternative conditional execution"},
    {"question": "7.What is the purpose of the 'for' loop?",
     "options": ["To iterate over a sequence", "To perform a conditional check", "To exit a loop"],
     "answer": "To iterate over a sequence"},
    {"question": "8.What is the difference between a list comprehension and a for loop?",
     "options": ["List comprehensions are more concise and readable than for loops", "List comprehensions are less efficient than for loops", "List comprehensions are used for mathematical operations"],
     "answer": "List comprehensions are more concise and readable than for loops"},
    {"question": "9.What is the purpose of the 'range()' function?",
     "options": ["To generate a sequence of numbers", "To create a list of numbers", "To perform arithmetic operations on numbers"],
     "answer": "To generate a sequence of numbers"},
    {"question": "10.What is the difference between a function and a method?",
     "options": ["Functions are defined independently, while methods are associated with classes", "Functions are used for general tasks, while methods are used for object-oriented programming", "Functions are slower than methods"],
     "answer": "Functions are defined independently, while methods are associated with classes"},
    {"question": "11.How do you comment a single line in Python?",
     "options": ["# This is a comment", "// This is a comment", "/* This is a comment */"],
     "answer": "# This is a comment"},
    {"question": "12.What is the purpose of the 'pass' statement in Python?",
     "options": ["To skip the execution of a block of code", "To indicate the end of a function",
                 "To define a variable"],
     "answer": "To skip the execution of a block of code"},

    {"question": "13.How do you open a file in Python for reading?",
     "options": ["open('file.txt', 'w')", "open('file.txt', 'r')", "read('file.txt')"],
     "answer": "open('file.txt', 'r')"},

    {"question": "14.What is the difference between '==' and 'is' operators in Python?",
     "options": ["'==' checks for equality, while 'is' checks for identity",
                 "'==' checks for identity, while 'is' checks for equality", "'==' and 'is' are interchangeable"],
     "answer": "'==' checks for equality, while 'is' checks for identity"},

    {"question": "15.How do you remove an element from a list in Python?",
     "options": ["list.remove(element)", "list.pop(index)", "del list[index]"],
     "answer": "list.pop(index)"},

    {"question": "16.What is the purpose of the 'try' and 'except' blocks in Python?",
     "options": ["To define a function", "To handle exceptions and errors", "To create a conditional statement"],
     "answer": "To handle exceptions and errors"},

    {"question": "17.How do you convert a string to lowercase in Python?",
     "options": ["string.upper()", "string.lower()", "string.capitalize()"],
     "answer": "string.lower()"},

    {"question": "18.What is the difference between 'append()' and 'extend()' methods for lists?",
     "options": ["'append()' adds a single element, while 'extend()' adds multiple elements",
                 "'append()' is used for strings, while 'extend()' is used for numbers",
                 "'append()' and 'extend()' are interchangeable"],
     "answer": "'append()' adds a single element, while 'extend()' adds multiple elements"},

    {"question": "19.How do you import a module in Python?",
     "options": ["import module", "include module", "from module import *"],
     "answer": "import module"},

    {"question": "20.What is the purpose of the 'lambda' function in Python?",
     "options": ["To define a class", "To create anonymous functions", "To handle exceptions"],
     "answer": "To create anonymous functions"},

    {"question": "21.What is the result of the expression 5 + 3 * 2?",
     "options": ["16", "11", "26"],
     "answer": "11"},

    {"question": "22.How do you perform integer division in Python?",
     "options": ["/", "//", "%"],
     "answer": "//"},

    {"question": "23.What is the purpose of the 'pow()' function in Python?",
     "options": ["To perform division", "To calculate powers", "To round numbers"],
     "answer": "To calculate powers"},
    {"question": "24.What is the correct syntax for exponentiation in Python?",
     "options": ["a ^ b", "a ** b", "pow(a, b)"],
     "answer": "a ** b"},

    {"question": "25.How do you increment a variable by 1 in Python?",
     "options": ["variable++", "variable += 1", "increment(variable)"],
     "answer": "variable += 1"},

    {"question": "26.What is the result of the expression 3 * (2 + 5)?",
     "options": ["21", "27", "17"],
     "answer": "21"},

    {"question": "27.How do you calculate the square root of a number in Python?",
     "options": ["sqrt(number)", "number^0.5", "math.sqrt(number)"],
     "answer": "math.sqrt(number)"},

    {"question": "28.What does the 'abs()' function do in Python?",
     "options": ["Converts a number to absolute value", "Calculates the average of numbers",
                 "Finds the maximum value in a list"],
     "answer": "Converts a number to absolute value"},

    {"question": "29.How do you round a floating-point number to the nearest integer in Python?",
     "options": ["round(number)", "floor(number)", "ceil(number)"],
     "answer": "round(number)"},

    {"question": "30.Are Lists Mutable ?",
     "options": ["Yes", "No"],
     "answer": "Yes"},
]

# Initialize the score counter
score = 0
user_responses = []

# Create the Streamlit app
st.title("Test Yourself")
st.divider()

# Display each question with answer options and collect user input
for question in questions:
    st.markdown(f"**{question['question']}**")
    answer = st.radio("Select the correct answer:", question["options"])
    user_responses.append({"question": question["question"], "user_answer": answer, "correct_answer": question["answer"]})
    st.divider()

    # Check if the user's answer is correct
    if answer == question["answer"]:
        score += 1

# Add a submit button and evaluate the score when clicked
submit_button = st.button("Submit Quiz")

if submit_button:
    st.warning(f"Your final score is {score} out of {len(questions)}")
    st.markdown("### Your Responses:")
    for response in user_responses:
        is_correct = response["user_answer"] == response["correct_answer"]
        if is_correct:
            st.warning(f"**{response['question']} ✅**")
            st.warning(f"Your answer: {response['user_answer']}")
            st.warning(f"Correct answer: {response['correct_answer']}")
            st.divider()
        else:
            st.warning(f"**{response['question']} ❌**")
            st.warning(f"Your answer: {response['user_answer']}")
            st.warning(f"Correct answer: {response['correct_answer']}")
            st.divider()