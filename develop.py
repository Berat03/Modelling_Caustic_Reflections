from sympy import *

def find_cusps(function_str):
    x, y = symbols('x y')
    f = sympify(function_str)

    # Calculate first and second derivatives
    f_prime = diff(f, x)
    f_double_prime = diff(f_prime, x)

    # Find points where f_prime is zero and f has a defined value
    critical_points = []

    x_vals = solve(f_prime, x)

    for x_val in x_vals:
        y_val = f.subs(x, x_val)
        if y_val.is_real:
            if f_double_prime.subs(x, x_val) != 0 and f_double_prime.subs(x, x_val).is_real:
                critical_points.append((x_val, y_val))

    return critical_points

# Example Usage:
cusp_points = find_cusps('x**2')
print("Cusp Points:", cusp_points)
