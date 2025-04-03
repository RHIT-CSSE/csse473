"""
Problem Reduction Demo: 
Linear Programming. 

Author: Ian Ludden
Date: 2025-04-04
Course: CSSE/MA 473
"""

from scipy.optimize import linprog

def design_combo_meal(calories, customer_prices, paunchburger_costs, max_customer_price, max_paunchburger_cost):
    """
    Objective: Maximize the calories. We negate the calories since linprog minimizes by default.

    Constraints: Ensure that the total price to customers does not exceed `max_customer_price` 
        and cost to Paunchburger stays below `max_paunchburger_cost`. 
        These constraints form the rows of matrix A and vector b. 
    Bounds: Each menu item can be selected (1) or not (0). 
        This is modeled using bounds from 0 to 1.
    Solution: Use linprog to find which items to select. 
        result.x contains which items to include, and 
        result.fun provides the total calorie count negated (since we maximized a negated objective).
    """
    # Negate calories since we are maximizing
    neg_calories = [-c for c in calories]
    
    # Inequality constraints (<= type)
    A = [customer_prices, paunchburger_costs]
    b = [max_customer_price, max_paunchburger_cost]

    # Bounds for each variable (item can't be chosen more than once, binary)
    x_bounds = [(0, 1) for _ in calories]

    # Solve the problem
    result = linprog(
        c=neg_calories, 
        A_ub=A, 
        b_ub=b, 
        bounds=x_bounds,
        method='highs'
    )

    if result.success:
        print("Optimal combination found:")
        print("Items to select:", result.x)
        print("Maximized calories:", -result.fun)
    else:
        print("No feasible solution found.")

if __name__ == '__main__':
    # Example inputs
    calories = [400, 300, 500, 200]
    customer_prices = [2, 1.5, 3, 2.5]
    paunchburger_costs = [0.8, 0.5, 1.2, 0.3]
    max_customer_price = 5
    max_paunchburger_cost = 2
    
    design_combo_meal(calories, customer_prices, paunchburger_costs, max_customer_price, max_paunchburger_cost)
