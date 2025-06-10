import streamlit as st

# Title
st.title("BMI Calculator")

# Input columns
col1, col2, col3 = st.columns(3)

with col1:
    weight = st.number_input("Enter Weight (kg)", min_value=1.0, format="%.2f")

with col2:
    height_cm = st.number_input("Enter Height (cm)", min_value=1.0, format="%.2f")

with col3:
    if weight and height_cm:
        height_m = height_cm / 100  # Convert to meters
        bmi = weight / (height_m ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
            color = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
            color = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
            color = "Overweight"
        elif bmi < 35:
            category = "Obesity Class I"
            color = "Obesity Class I"
        elif bmi < 40:
            category = "Obesity Class II"
            color = "Obesity Class II"
        else:
            category = "Obesity Class III"
            color = "obesity class III"

        # Show BMI and category with color
        st.metric("Your BMI", f"{bmi:.2f}")
        st.markdown(f"### 🩺 Category: **:{color}[{category}]**")
    else:
        st.metric("Your BMI", "---")
