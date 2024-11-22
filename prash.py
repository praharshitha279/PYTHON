import streamlit as st 

def Elec_Para(V, R, T): 
    I = V / R 
    P = I * V 
    H = I**2 * R * T 
    return I, P, H 

# Set the title of the app 
st.title("2205A21001-PS1") 
st.subheader("This application is useful for calculating current through a load,power drawn by the load,and heat energy generated")

col1,col2 = st.columns(2)
with col1:
    V = st.number_input("Input Voltage (V)", min_value=100) 
    R = st.number_input("Load Resistance (R)", min_value=1000) # Avoid division by zero 
    T = st.number_input("Time in hours (T)", min_value=2)
    compute=st.button("compute")
with col2:
    with st.container(border=True):
        if compute:
           I, P, H = Elec_Para(V,R,T)
           st.write(f"loadcurrent = {I:.2f} A")
           st.write(f"loadpower = {P:.2f} W")
           st.write(f"Heatenergy = {H:.2f} Wh")