import streamlit as st
 
st.title("Calculator App using Streamlit")
 
# creates a horizontal line
st.write("---")
 
# input 1
num1 = st.number_input(label="Enter first number")
 
# input 2
num2 = st.number_input(label="Enter second number")
 
st.write("Operation")
operation = st.radio("Select an operation to perform:",("+", "-", "*", "/"))
st.snow()
ans = 0
#Function for calculated the inputs
def calculate():
    if operation == "+":
        ans = num1 + num2
    elif operation == "-":
        ans = num1 - num2
    elif operation == "*":
        ans = num1 * num2
    elif operation=="/" and num2!=0:
        ans = num1 / num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        ans = "Not defined"
 
    st.success(f"Answer = {ans}")
 
if st.button("Calculate result"):
    calculate()

    