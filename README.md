import math

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


def run_simulator():
    print("🐍⚛️ Newtonian Physics Simulator: Projectile Motion 🐍⚛️")
    while True:
        try:
            print("\n--- New Simulation ---")
            u = float(input("Enter Initial Velocity (u) in m/s: "))
            theta_deg = float(input("Enter Angle of Projection (θ) in degrees: "))

            # Validate inputs
            if u <= 0:
                print("⚠️ Velocity must be a positive number.")
                continue
            if not (0 <= theta_deg <= 90):
                print("⚠️ Angle must be between 0 and 90 degrees.")
                continue

            # Convert degrees to radians for Python math functions
            theta_rad = math.radians(theta_deg)

            # Perform calculations
            t_flight = calculate_time_of_flight(u, theta_rad)
            max_h = calculate_max_height(u, theta_rad)
            h_range = calculate_range(u, theta_rad)

            # Output Results
            print("\n📊 Simulation Results:")
            print(f" • Time of Flight (T) : {t_flight:.2f} s")
            print(f" • Maximum Height (H) : {max_h:.2f} m")
            print(f" • Horizontal Range (R): {h_range:.2f} m")

        except ValueError:
            print("⚠️ Invalid input. Please enter numerical values.")
            continue

        again = input("\nRun another simulation? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting Simulator. Goodbye! 🚀")
            break


if __name__ == "__main__":
    try:
        run_simulator()
    except KeyboardInterrupt:
        print("\nExiting Simulator. Goodbye! 🚀")
