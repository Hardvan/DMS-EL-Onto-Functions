
# ? Problem Statement
# * Calculate the number of onto functions from a
# * set S to a set T, where S and T are finite sets of
# * various sizes. List all of them.

from itertools import permutations, product


def calculate_onto_functions(S, T, repeated=False):

    # Calculate the number of onto functions from S to T
    n = len(S)
    m = len(T)
    num_onto_functions = m ** n

    # List all of the onto functions from S to T
    onto_functions = []
    if not repeated:
        for t in permutations(T, n):
            onto_functions.append(dict(zip(S, t)))
    else:
        for t in product(T, repeat=n):
            onto_functions.append(dict(zip(S, t)))

    return num_onto_functions, onto_functions


# Example Usage
S = {1, 2, 3}
T = {'a', 'b', 'c', 'd'}

repeated = input(
    "Do you want to allow repeated elements in the onto functions? (y/n): ")
repeated = repeated.lower() == 'y'

num_onto_functions, onto_functions = calculate_onto_functions(S, T, repeated)

print("Number of onto functions from S to T:", num_onto_functions)

# Display all of the onto functions
print("All of the onto functions from S to T:")
for f in onto_functions:
    print(f)
