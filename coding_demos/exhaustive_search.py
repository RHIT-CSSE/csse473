"""
Exhaustive search: 
Assignment Problem and Knapsack Problem. 

Practice generating combinatorial objects. 

Author: Ian Ludden
Date: 2025-03-06
Course: CSSE/MA 473
"""

def generate_all_permutations(n):
    """
    Generate all permutations of n elements. 
    
    Args: 
        n (int): Number of elements to permute. 
        
    Returns: 
        list: List of all permutations of n elements, 
        each represented by a list. 
    """
    # TODO 1: Implement this function. 
    # You can use the simple recursive strategy 
    # discussed in class, or if you're feeling adventurous, 
    # you can implement the Johnson-Trotter algorithm 
    # described in Levitin Section 4.3.
    return [[i for i in range(1, n + 1)]]


def generate_all_subsets(n):
    """
    Generate all subsets of n elements. 
    
    Args: 
        n (int): Number of elements to choose from. 
        
    Returns: 
        list: List of all subsets of n elements, 
        each represented by a Python set object. 
    """
    # TODO 3: Implement this function.
    # You can use the simple recursive strategy
    # discussed in class, or if you're feeling adventurous,
    # you can implement the binary reflexive Gray code algorithm
    # described in Levitin Section 4.3. 
    return [set([i for i in range(1, n + 1)])]


def solve_assignment(C):
    """
    Solves the assignment problem using exhaustive search.

    Args:
        C (list): Cost matrix, where C[i - 1][j - 1] is the cost of
        assigning worker 1 <= i <= n to task 1 <= j <= n.

    Returns:
        tuple: Tuple (cost, assignment), where 
        cost is the minimum possible cost and 
        assignment is a list of length n, 
        where assignment[i-1] is the task assigned to worker i.
    """
    # TODO 2: Implement this function. Use generate_all_permutations. 
    return (0, [0])


def solve_knapsack(weights, values, W):
    """
    Solves the knapsack problem using exhaustive search.

    Args:
        weights (list): List of weights of items.
        values (list): List of values of items.
        W (int): Capacity of the knapsack.

    Returns:
        tuple: Tuple (value, items), where value is the maximum
        value that can be obtained and items is the subset of items
        that achieves this maximum value. 
    """
    # TODO 4: Implement this function. Use generate_all_subsets. 
    return (0, set())


if __name__ == '__main__':
    # Construct assignment problem cost matrix
    C = [[9, 2, 7, 8],
         [6, 4, 3, 7],
         [5, 8, 1, 8],
         [7, 6, 9, 4]]

    # Solve assignment problem
    cost, assignment = solve_assignment(C)
    print(f'Assignment problem cost: {cost}')
    print(f'Assignment: {assignment}')

    # Construct knapsack problem data
    weights = [7, 3, 4, 5]
    values = [42, 12, 40, 25]
    W = 10

    # Solve knapsack problem
    value, items = solve_knapsack(weights, values, W)
    print(f'Knapsack problem value: {value}')
    print(f'Items: {items}')
