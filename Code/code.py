
# ? Problem Statement
# * Calculate the number of onto functions from a
# * set S to a set T, where S and T are finite sets of
# * various sizes. List all of them.

from itertools import product


def calculate_onto_functions(S, T):
    """Calculate the number of onto functions from S to T.

    Args:
        S: A set of integers.
        T: A set of integers.

    Returns:
        num_onto: The number of onto functions from S to T.
        onto: A list of all of the onto functions from S to T.
    """

    # Calculate the number of onto functions from S to T
    n = len(S)
    m = len(T)
    num_onto = m ** n

    # List all of the onto functions from S to T
    onto = []

    for t in product(T, repeat=n):
        onto.append(dict(zip(S, t)))

    return num_onto, onto


# Example Usage
S = {1, 2, 3, 4}
T = {'a', 'b', 'c'}

print("S:", S)
print("T:", T)

num_onto, onto = calculate_onto_functions(S, T)

print("\nNumber of onto functions from S to T:", num_onto)

# Display all of the onto functions
print("All of the onto functions from S to T:\n")
for f in onto:
    print(f)

print("---------------------------------")

print("Try with your own sets of integers!\n")

print("Enter a set S of integers separated by spaces:")
S = set(map(int, input().split()))
print("Enter a set T of integers separated by spaces:")
T = set(map(int, input().split()))

num_onto, onto = calculate_onto_functions(S, T)

print("\nNumber of onto functions from S to T:", num_onto)

# Display all of the onto functions
print("All of the onto functions from S to T:\n")
for f in onto:
    print(f)
