import numpy as np

def solve_polynomial():
    coefficients = None
    while coefficients is None:
        coefficients = input("Enter the coefficients of the polynomial separated by spaces (e.g., '1 -6 11 -6' for x^3 - 6x^2 + 11x - 6): ")
        coefficients = coefficients.split(" ")
        if len(coefficients) < 2:
            print("Error: Wrong amount of coefficients")
            coefficients = None
    coefficients = [float(coeff) for coeff in coefficients]
    
    x0 = None
    while x0 is None:
      try:
        x0 = float(input("Enter the initial guess for the root: "))
      except ValueError:
        print("Error: That guess is not a valid number")
    
    # Set the tolerance for convergence and the maximum number of iterations
    tolerance = 1e-6
    max_iterations = 100
    
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
    
    # Display the results
    if i < max_iterations - 1:
        print(f"Root found at x = {x:.6f}")
    else:
        print("The method did not converge to a root within the specified tolerance.")

def solve_piecewise():
    def piecewise_function(x):
        if x < 1:
            return x**2 - 3*x + 2
        elif x >= 1 and x < 3:
            return 2*x - 1
        else:
            return x**3 - 6
    
    # Define the initial guess for the root and tolerance
    x0 = None
    while x0 is None:
      try:
        x0 = float(input("Enter the initial guess for the root: "))
      except ValueError:
        print("That is not a valid guess")
    
    tolerance = 1e-6
    max_iterations = 100
    
    # Implement the Newton-Raphson method
    x = x0
    roots = []
    
    for i in range(max_iterations):
        x_new = x - piecewise_function(x) / (2 * x - 3)
        if abs(x_new - x) < tolerance:
            roots.append(x_new)
            break
        x = x_new
    
    x = x0  # Reset initial guess for the next segment
    
    for i in range(max_iterations):
        x_new = x - piecewise_function(x) / 2
        if abs(x_new - x) < tolerance:
            roots.append(x_new)
            break
        x = x_new
    
    x = x0  # Reset initial guess for the next segment
    
    for i in range(max_iterations):
        x_new = x - piecewise_function(x) / (3 * x**2)
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
