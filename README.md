# Newtonian-Physics-Simulator
A Python-based Newtonian Physics Simulator that automates Class 12 projectile motion calculations. It takes initial velocity and angle as inputs to instantly compute Time of Flight, Maximum Height, and Range.
# 🐍⚛️ Newtonian Physics Simulator: Projectile Motion

## Overview
This Python application automates standard Class 12 Physics calculations for two-dimensional projectile motion. By taking the Initial Velocity ($u$) and Angle of Projection ($\theta$) as user inputs, the simulator instantly computes key flight metrics. This project bridges the gap between theoretical kinematics and practical, modular programming logic.

## 🖥️ Application Preview
![Console Output](image_7040c6.jpg)

## 🔧 Features & Capabilities
*   **Time of Flight:** Calculates the total time the projectile remains in the air.
*   **Maximum Height:** Computes the peak vertical altitude reached during the trajectory.
*   **Horizontal Range:** Determines the total horizontal distance traveled before impact.
*   **Interactive Loop:** Allows the user to run continuous simulations without restarting the program.

## 🧮 The Physics Engine
The simulator utilizes core kinematic equations and the Python `math` library, assuming standard gravity ($g = 9.81 \, \text{m/s}^2$):

*   **Time of Flight ($T$):** $$T = \frac{2u \sin(\theta)}{g}$$
*   **Maximum Height ($H$):** $$H = \frac{u^2 \sin^2(\theta)}{2g}$$
*   **Horizontal Range ($R$):** $$R = \frac{u^2 \sin(2\theta)}{g}$$

## 💡 Project Learnings
Translating mathematical formulas into Python functions provided hands-on experience with:
*   Importing and utilizing the standard `math` library for trigonometric conversions (degrees to radians).
*   Designing modular, reusable functions for individual calculations to keep code DRY (Don't Repeat Yourself).
*   Formatting console outputs and utilizing `while` loops for a clean, interactive user experience.

## 🚀 How to Run Locally
1. Clone this repository.
2. Ensure Python 3.x is installed on your system.
3. Run 'newtonian_physics_simulator.py` in your terminal.
