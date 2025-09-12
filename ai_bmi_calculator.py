import google.generativeai as genai

import streamlit as st

genai.configure(api_key="AIzaSyD3s5JLhwLcdLvpH2FSARsuN-0EQLeSLCI")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Based BMI Calculator")
name = st.text_input("Enter your name:")
wt = st.number_input("Enter your weight in kg:")
ht = st.slider("Enter your height in cm:",50,250)
age=st.number_input("Enter your age:")
gender = st.selectbox("Select your gender:", ["", "Male", "Female"])
if st.button("Calculate BMI & Get Advice"):
 if name and wt > 0 and ht > 0 and age > 0 and gender:
  bmi = round(wt/(ht/100)**2,2)

  st.success(f" {name}, your **BMI is: {bmi}** ")

  prompt = f"Act like an expert nutritionist, comment on the bmi with the following data: height as{ht}, weight as{wt}, age as{age}, gender as{gender} and   bmi as{bmi}"
  response = model.generate_content(prompt)
  print(response.text)

  st.markdown(response.text)
else:
    st.warning("⚠️ Please fill in **all details** before submitting.")