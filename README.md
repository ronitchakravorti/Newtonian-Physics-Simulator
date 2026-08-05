

import math
import streamlit as st

# Define Constants
G = 9.81 # Acceleration due to gravity (m/s^2)


def calculate_time_of_flight(u, theta_rad):
    """Calculates total time the projectile remains in the air."""
    return (2 * u * math.sin(theta_rad)) / G


def calculate_max_height(u, theta_rad):
    """Computes the peak vertical altitude reached."""
    return ((u ** 2) * (math.sin(theta_rad) ** 2)) / (2 * G)


def calculate_range(u, theta_rad):
    """Determines total horizontal distance traveled."""
    return ((u ** 2) * math.sin(2 * theta_rad)) / G


st.set_page_config(page_title="Projectile Motion Simulator", page_icon="🚀")

st.title("🐍⚛️ Newtonian Physics Simulator")
st.subheader("Projectile Motion")

st.write("Enter the launch conditions below to calculate the projectile's flight characteristics.")

col1, col2 = st.columns(2)
with col1:
    u = st.number_input("Initial Velocity (u) in m/s", min_value=0.1, value=20.0, step=0.5)
with col2:
    theta_deg = st.slider("Angle of Projection (θ) in degrees", min_value=0, max_value=90, value=45)

if st.button("Run Simulation", type="primary"):
    theta_rad = math.radians(theta_deg)

    t_flight = calculate_time_of_flight(u, theta_rad)
    max_h = calculate_max_height(u, theta_rad)
    h_range = calculate_range(u, theta_rad)

    st.write("### 📊 Simulation Results")
    r1, r2, r3 = st.columns(3)
    r1.metric("Time of Flight (T)", f"{t_flight:.2f} s")
    r2.metric("Maximum Height (H)", f"{max_h:.2f} m")
    r3.metric("Horizontal Range (R)", f"{h_range:.2f} m")

    # Simple trajectory plot
    import numpy as np
    t_vals = np.linspace(0, t_flight, 200)
    x_vals = u * np.cos(theta_rad) * t_vals
    y_vals = u * np.sin(theta_rad) * t_vals - 0.5 * G * t_vals ** 2

    st.write("### 🚀 Trajectory")
    st.line_chart({"Height (m)": y_vals}, x=x_vals)
