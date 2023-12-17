import streamlit as st
st.set_page_config(page_title="Virtual Labs NSSCE", page_icon="🐍", layout= "wide")
st.title("Practice Session")
st.info("Repetition is the Mother Of All Skills")
st.divider()

questions = [
    "Character Input 🔍",
    "Odd Or Even 🔍",
    "List Less Than Ten 🔍🔍",
    "Divisors 🔍🔍",
    "List Overlap 🔍🔍",
    "String Lists 🔍🔍",
    "List Comprehensions 🔍🔍",
    "Rock Paper Scissors 🔍🔍🔍",
    "Guessing Game One 🔍🔍🔍",
    "Check Primality Functions 🔍🔍🔍",
    "List Ends 🔍",
    "Fibonacci 🔍🔍",
    "List Remove Duplicates 🔍🔍",
    "Reverse Word Order 🔍🔍🔍",
    "Password Generator 🔍🔍🔍🔍",
    "Decode A Web Page 🔍🔍🔍🔍",
    "Element Search 🔍",
]



python_exercises = [
    "Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.",
    "Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.",
    "Take a list and write a program that prints out all the elements of the list that are less than 5.",
    "Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)",
    "Write a function that takes an ordered list of numbers and another number, deciding whether or not the given number is inside the list and returns an appropriate boolean.",
    "Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards)",
    "Write one line of Python that takes a list and makes a new list that has only the even elements of this list in it.",
    "Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)",
    "Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.",
    "Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.)",
    "Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.",
    "Write a program that asks the user how many Fibonacci numbers to generate and then generates them.",
    "Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.",
    "Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.",
    "Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.",
    "Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.",
    "Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean."]





for i in range(0, len(questions)):
    with st.expander(f"**{questions[i]}**"):
         st.write(f"**{python_exercises[i]}**")


st.divider()
st.warning("'🔍' implies the difficulty of the question for a beginner")
