import streamlit as st

st.title("Unit Converter App")
st.markdown("### Convert  Lenght , Time And Weight Instantly ")

category = st.selectbox("Choose a Category" , ["Time" , "Length" , "Weight"])

def convert_unit(category , value , unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "miles to kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
           return value / 2.20462
        
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hour to minutes":
            return value * 60
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24
        
if category == "Length":
    unit = st.selectbox("Select Conversion" , ["kilometers to miles", "miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select Conversion" , ["kilograms to pounds", "pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversion" , ["seconds to minutes", "minutes to seconds", "minutes to hours", "hour to minutes", "hours to days", "days to hours"])            
        
value = st.number_input("Enter The Value To Convert")

if st.button("convert"):
    result = convert_unit(category,value,unit)
    st.success(f"The Result is {result:.2f}")