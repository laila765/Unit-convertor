import streamlit as st

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {"meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084}
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274}
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

# Streamlit UI
st.title("🔢  Unit Converter")

unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

if unit_type == "Length":
    from_unit = st.selectbox("From", ["meters", "kilometers", "miles", "feet"])
    to_unit = st.selectbox("To", ["meters", "kilometers", "miles", "feet"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif unit_type == "Weight":
    from_unit = st.selectbox("From", ["grams", "kilograms", "pounds", "ounces"])
    to_unit = st.selectbox("To", ["grams", "kilograms", "pounds", "ounces"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif unit_type == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter Value", format="%.2f")
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
