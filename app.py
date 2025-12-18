# app.py
import streamlit as st

st.set_page_config(page_title="Pump Power Calculator", layout="centered")

st.title("🧮 Pump Power Calculator")
st.write("Enter the pump parameters to calculate the required hydraulic power.")

def pump_power(flow_rate, density, head, efficiency):
    g = 9.81
    eta = efficiency / 100

    if eta <= 0:
        return None, "Efficiency must be greater than 0%"

    power_watts = (flow_rate * density * g * head) / eta
    power_kw = power_watts / 1000
    return power_kw, None

flow_rate = st.number_input("Flow Rate (m³/s)", min_value=0.0)
density = st.number_input("Fluid Density (kg/m³)", value=1000.0)
head = st.number_input("Pump Head (m)", min_value=0.0)
efficiency = st.number_input(
    "Pump Efficiency (%)", min_value=1.0, max_value=100.0, value=70.0
)

if st.button("Calculate Pump Power"):
    result, error = pump_power(flow_rate, density, head, efficiency)

    if error:
        st.error(error)
    else:
        st.success(f"Required Pump Power: {result:.3f} kW")
