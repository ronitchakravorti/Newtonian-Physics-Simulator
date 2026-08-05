import math

def calculate_projectile(u, theta_degrees):
    g = 9.81
    # Convert angle to radians
    theta = math.radians(theta_degrees)
    
    # Calculate metrics
    time_of_flight = (2 * u * math.sin(theta)) / g
    max_height = (u**2 * (math.sin(theta)**2)) / (2 * g)
    range_covered = (u**2 * math.sin(2 * theta)) / g
    
    return time_of_flight, max_height, range_covered

def main():
    while True:
        print("=================================================")
        print(" NEWTONIAN PHYSICS SIMULATOR: PROJECTILE MOTION")
        print("=================================================")
        print("\nThis program calculates Range, Max Height, and Flight Time.\n")
        
        try:
            u = float(input("Enter Initial Velocity (u) in m/s:  > "))
            theta = float(input("Enter Angle of Projection (theta) in degrees: > "))
            
            t, h, r = calculate_projectile(u, theta)
            
            print("\n---------------- RESULTS ------------------------")
            print(f"Total Time of Flight:      {t:.2f} seconds")
            print(f"Maximum Height Reached:    {h:.2f} meters")
            print(f"Horizontal Range Covered:  {r:.2f} meters")
            print("-------------------------------------------------\n")
            
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            
        restart = input("Run another simulation? (Press 'y' for yes, or any other key to exit): ")
        if restart.lower() != 'y':
            break

if __name__ == "__main__":
    main()
