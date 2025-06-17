# streamlit_fuselage_sizing.py
import streamlit as st
import math

st.set_page_config(page_title="Hybrid VTOL Fuselage Sizing", layout="centered")

st.title("Hybrid VTOL Drone - Fuselage Sizing Tool")
st.markdown("Estimate fuselage dimensions based on payload, battery, and design requirements.")

# --- Input Section ---
st.subheader("Input Parameters")
payload_kg = st.number_input("Payload Mass (kg)", min_value=0.1, value=5.0, step=0.1)
battery_mass_kg = st.number_input("Battery Mass (kg)", min_value=0.1, value=2.0, step=0.1)
avionics_mass_kg = st.number_input("Avionics Mass (kg)", min_value=0.1, value=0.5, step=0.1)
structure_mass_kg = st.number_input("Structure Mass Estimate (kg)", min_value=0.1, value=2.0, step=0.1)
density_structure = st.number_input("Material Density (kg/m³)", min_value=50.0, value=100.0, step=10.0)

# --- Calculation Logic ---
total_mass = payload_kg + battery_mass_kg + avionics_mass_kg + structure_mass_kg
mass_allowance = total_mass * 1.2  # 20% margin for design tolerance

# Assume cylindrical fuselage approximation
# Volume = mass / density, Volume = pi * r^2 * L => L = Volume / (pi * r^2)
fuselage_radius_m = st.slider("Assumed Fuselage Radius (m)", min_value=0.05, max_value=0.5, value=0.15, step=0.01)
fuselage_volume_m3 = mass_allowance / density_structure
fuselage_length_m = fuselage_volume_m3 / (math.pi * fuselage_radius_m ** 2)

# --- Output Section ---
st.subheader("Estimated Fuselage Dimensions")
st.write(f"**Total Design Mass Allowance:** {mass_allowance:.2f} kg")
st.write(f"**Estimated Fuselage Volume:** {fuselage_volume_m3:.3f} m³")
st.write(f"**Estimated Fuselage Length:** {fuselage_length_m:.2f} m")

# Optional: Export to Excel (future feature)
# TODO: Add export to Excel or CSV
