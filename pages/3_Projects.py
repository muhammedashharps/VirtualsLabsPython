import streamlit as st
st.set_page_config(page_title="Virtual Labs NSSCE", page_icon="🐍", layout= "wide")

st.title("Projects")

st.divider()

import streamlit as st
import random


st.title("Project 1: Interactive Greeting")
name = st.text_input("Enter your name:")
st.write(f"**Output: Hello, {name}!**")
st.info(
    """
    **Algorithm 1: Interactive Greeting**
    1. Get the user's name as input.
    2. Display a personalized greeting.
    """
)

st.divider()

st.title("Project 2: Number Guessing Game")
secret_number = random.randint(1, 10)
guess = st.number_input("Guess a number between 1 and 10:")
if st.button("Check"):
    if guess == secret_number:
        st.write(f"**Output: Congratulations! You guessed the correct number.**")
    else:
        st.write(f"**Output: Sorry, the correct number was {secret_number}. Try again!**")
st.info(
    """
    **Algorithm 2: Number Guessing Game**
    1. Generate a random number between 1 and 10.
    2. Get the user's guess.
    3. Check if the guessed number is correct.
    4. Display a message indicating correctness.
    """
)
st.divider()

st.title("Project 3: BMI Calculator")
weight = st.number_input("Enter your weight (kg):")
height = st.number_input("Enter your height (cm):")
if st.button("Calculate BMI"):
    bmi = weight / ((height / 100) ** 2)
    st.write(f"**Output: Your BMI is: {bmi:.2f}**")
st.info(
    """
    **Algorithm 3: BMI Calculator**
    1. Get the user's weight and height.
    2. Calculate BMI using the formula `weight / (height / 100)^2`.
    3. Display the calculated BMI.
    """
)
st.divider()

st.title("Project 5: To-Do List")
tasks = st.text_input("Enter a task:")
task_list = st.button("Add Task")
if task_list:
    st.write("**Tasks:**")
    st.write(f"- {tasks}")
st.info(
    """
    **Algorithm 5: To-Do List**
    1. Get the user's task.
    2. Display the entered task.
    """
)
st.divider()

st.title("Project 6: Dice Roller")
if st.button("Roll Dice"):
    result = random.randint(1, 6)
    st.write(f"**Output: The result is: {result}**")
st.info(
    """
    **Algorithm 6: Dice Roller**
    1. Generate a random number between 1 and 6.
    2. Display the result.
    """
)

st.divider()

st.title("Project 7: Color Palette Generator")
if st.button("Generate Color"):
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    st.write(f"**Output:** Generated Color: {color}")
    st.markdown(f'<div style="background-color:{color}; width:50px; height:50px;"></div>', unsafe_allow_html=True)
st.info(
    """
    **Algorithm 7: Color Palette Generator**
    1. Generate a random color code.
    2. Display the color code.
    """
)
st.divider()

st.title("Project 8: Text Reverser")
text_to_reverse = st.text_input("Enter text to reverse:")
reversed_text = text_to_reverse[::-1]
st.write(f"**Output**: Reversed Text: {reversed_text}")
st.info(
    """
    **Algorithm 8: Text Reverser**
    1. Get the user's text.
    2. Reverse the text using string slicing.
    3. Display the reversed text.
    """
)

st.divider()

st.title("Project 9: Temperature Converter")
celsius_temp = st.number_input("Enter temperature in Celsius:")
converted_temp = (celsius_temp * 9/5) + 32
st.write(f"**Output: Temperature in Fahrenheit: {converted_temp:.2f}°F**")
st.info(
    """
    **Algorithm 9: Temperature Converter**
    1. Get the temperature in Celsius.
    2. Convert Celsius to Fahrenheit.
    3. Display the converted temperature.
    """
)

st.divider()

st.title("Project 10: Currency Converter")
usd_amount = st.number_input("Enter amount in USD:")
selected_currency = st.selectbox("Select currency:", ["EUR", "GBP", "JPY", "CAD"])
conversion_rates = {"EUR": 0.85, "GBP": 0.74, "JPY": 113.41, "CAD": 1.28}
converted_amount = usd_amount * conversion_rates[selected_currency]
st.write(f"**Output: {usd_amount} USD is approximately {converted_amount:.2f} {selected_currency}**")
st.info(
    """
    **Algorithm 10: Currency Converter**
    1. Get the amount in USD and select the target currency.
    2. Convert the amount to the selected currency using predefined conversion rates.
    3. Display the converted amount.
    """
)
st.divider()