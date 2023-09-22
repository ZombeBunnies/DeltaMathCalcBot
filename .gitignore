import numpy as np

# Define the polynomial equation solver
def solve_polynomial():
    coefficients = input("Enter the coefficients of the polynomial separated by spaces (e.g., '1 -6 11 -6' for x^3 - 6x^2 + 11x - 6): ").split()
    coefficients = [float(coeff) for coeff in coefficients]
    
    # Define the initial guess for the root
    x0 = float(input("Enter the initial guess for the root: "))
    
    # Set the tolerance for convergence
    tolerance = 1e-6
    
    # Maximum number of iterations
    max_iterations = 100
    
    # Define the polynomial function
    def polynomial(x):
        return np.polyval(coefficients, x)
    
    # Define the derivative of the polynomial function
    def polynomial_derivative(x):
        return np.polyval(np.polyder(coefficients), x)
    
    # Implement the Newton-Raphson method
    x = x0
    for i in range(max_iterations):
        x_new = x - polynomial(x) / polynomial_derivative(x)
        if abs(x_new - x) < tolerance:
            break
        x = x_new
    
    # Display the result
    if i < max_iterations - 1:
        print(f"Root found at x = {x:.6f}")
    else:
        print("The method did not converge to a root within the specified tolerance.")

# Define the piecewise function solver
def solve_piecewise():
    def piecewise_function(x):
        if x < 1:
            return x**2 - 3*x + 2
        elif x >= 1 and x < 3:
            return 2*x - 1
        else:
            return x**3 - 6
    
    # Define the initial guess for the root and tolerance
    x0 = float(input("Enter the initial guess for the root: "))
    tolerance = 1e-6
    max_iterations = 100
    
    # Implement the Newton-Raphson method
    x = x0
    roots = []
    
    for i in range(max_iterations):
        x_new = x - piecewise_function(x) / (2 * x - 3)  # Derivative for the first segment
        if abs(x_new - x) < tolerance:
            roots.append(x_new)
            break
        x = x_new
    
    x = x0  # Reset initial guess for the next segment
    
    for i in range(max_iterations):
        x_new = x - piecewise_function(x) / 2  # Derivative for the second segment
        if abs(x_new - x) < tolerance:
            roots.append(x_new)
            break
        x = x_new
    
    x = x0  # Reset initial guess for the next segment
    
    for i in range(max_iterations):
        x_new = x - piecewise_function(x) / (3 * x**2)  # Derivative for the third segment
        if abs(x_new - x) < tolerance:
            roots.append(x_new)
            break
        x = x_new
    
    # Display the results
    if len(roots) > 0:
        for i, root in enumerate(roots):
            print(f"Root {i + 1} found at x = {root:.6f}")
    else:
        print("No roots found within the specified tolerance.")

# Define a function to add future options
def future_option():
    print("This is a future option.")

# Main menu using a dictionary
menu_options = {
    '1': solve_polynomial,
    '2': solve_piecewise,
    '3': future_option,
    '4': exit
}

while True:
    print("\nChoose an option:")
    print("1. Solve Polynomial Equation")
    print("2. Solve Piecewise Function")
    print("3. Future Option")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Invalid choice. Please enter a valid option.")
