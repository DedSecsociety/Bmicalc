import google.generativeai as genai

import streamlit as st

genai.configure(api_key="AIzaSyD3s5JLhwLcdLvpH2FSARsuN-0EQLeSLCI")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Based BMI Calculator")
name = st.text_input("Enter your name:")
wt = st.number_input("Enter your weight in kg:")
ht = st.slider("Enter your height in cm:",50,250)
age=st.number_input("Enter your age:")
gender=st.text_input("Enter your gender:")
bmi = round(wt/(ht/100)**2,2)

st.write(f"{name}, your bmi is : {bmi}")

prompt = f"Act like an expert nutritionist, comment on the bmi with the following data: height as{ht}, weight as{wt}, age as{age}, gender as{gender} and bmi as{bmi}"
response = model.generate_content(prompt)
print(response.text)
st.markdown(response.text)