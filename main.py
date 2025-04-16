import streamlit as st

# Dictionary of unit conversions
unit_categories = {
    "Length": {
        "units": ["meters", "kilometers", "miles", "feet", "inches"],
        "conversion": {
            "meters": 1,
            "kilometers": 1000,
            "miles": 1609.34,
            "feet": 0.3048,
            "inches": 0.0254
        }
    },
    "Weight": {
        "units": ["grams", "kilograms", "pounds", "ounces"],
        "conversion": {
            "grams": 1,
            "kilograms": 1000,
            "pounds": 453.592,
            "ounces": 28.3495
        }
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"]
    }
}

def convert_units(category, value, from_unit, to_unit):
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    else:
        base = value * unit_categories[category]["conversion"][from_unit]
        result = base / unit_categories[category]["conversion"][to_unit]
        return result

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert from source to Celsius
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        value = value - 273.15

    # Convert from Celsius to target
    if to_unit == "Fahrenheit":
        return value * 9/5 + 32
    elif to_unit == "Kelvin":
        return value + 273.15
    return value

# Streamlit UI
st.set_page_config(page_title="Google-Style Unit Converter", layout="centered")
st.title("🔁 Google-Style Unit Converter")

# Choose category
category = st.selectbox("Select Unit Category", list(unit_categories.keys()))

# Choose units
units = unit_categories[category]["units"]
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# Input value
value = st.number_input("Enter value to convert", value=0.0)

# Convert
if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
