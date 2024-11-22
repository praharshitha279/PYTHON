import streamlit as st

def Elec_Para(V, R, T):
    I = V / R
    P = I**2 * R
    H = P * T
    return I, P, H

st.title("Electrical Parameter Calculator")
st.write("This application calculates current through a load, power drawn by the load, and heat energy generated.")

try:
    voltage = float(st.text_input("Enter the Voltage (V):", value="0"))
    resistance = float(st.text_input("Enter the Resistance (R) in ohms:", value="0"))
    time = float(st.text_input("Enter the Time (T) in hours:", value="0"))

    if st.button("Compute"):
        if resistance > 0 and time >= 0:
            current, power, heat_energy = Elec_Para(voltage, resistance, time)
            st.write(f"Load Current (I): {current:.2f} A")
            st.write(f"Power Drawn by Load (P): {power:.2f} W")
            st.write(f"Heat Energy (H): {heat_energy:.2f} Wh")
        else:
            st.error("Resistance must be positive, and time must be non-negative!")
except ValueError:
    st.error("Invalid input! Please enter numeric values.")
    
st.write("Developed using Streamlit.")