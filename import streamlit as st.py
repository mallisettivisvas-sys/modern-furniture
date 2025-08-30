import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("🚀 My First Streamlit App")

# Text input
name = st.text_input("What's your name?", "World")

# Display greeting
st.write(f"Hello, {name}!")

# Slider
age = st.slider("How old are you?", 0, 100, 25)
st.write(f"You're {age} years old.")

# Line chart example
st.subheader("📈 Random Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Show a data table
st.subheader("📊 Data Table")
st.dataframe(chart_data)

# Button example
if st.button("Click Me"):
    st.success("🎉 You clicked the button!")