from scipy.optimize import fsolve
import numpy as np

e = np.e


# Define the function from the equation
def equation_func(r):
    e = np.e
    return e**(-0.5*r) + e**(-r)+e**(-1.5*r)+101*(e**(-2*r))-99.0252


# return的东西为0，即为方程

# Use fsolve to find the root, providing an initial guess for r
initial_guess = 0.05
r_solution = fsolve(equation_func, initial_guess)

print(r_solution)
