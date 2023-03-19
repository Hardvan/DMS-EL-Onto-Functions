
# ? Problem Statement
# * Calculate the number of onto functions from a
# * set S to a set T, where S and T are finite sets of
# * various sizes. List all of them.

from itertools import product


def fact(n):

    if n <= 1:
        return 1
    return n * fact(n - 1)


def nCr(n, r):

    return (fact(n) / (fact(r) * fact(n - r)))


def calculate_onto_functions(A, B):
    """Calculate the number of onto functions from A to B.

    Args:
        A: A set of integers.
        B: A set of integers.

    Returns:
        num_onto: The number of onto functions from A to B.
        onto: A list of all of the onto functions from A to B.
    """

    # Calculate the number of onto functions from A to B
    m = len(A)
    n = len(B)
    if m < n:
        print("There are no onto functions from A to B.")
        return 0, []

    num_onto = 0
    for k in range(0, n):  # 0 to n-1
        num_onto += ((-1)**k) * nCr(n, n-k) * ((n-k)**m)

    # List all of the onto functions from A to B
    onto = []
    for b in product(B, repeat=m):
        if len(set(b)) == n:
            onto.append(dict(zip(A, b)))

    return int(num_onto), onto


# Example Usage
S = {1, 2, 3, 4}
T = {'a', 'b', 'c'}

print("S:", S)
print("T:", T)

num_onto, onto = calculate_onto_functions(S, T)

print("\nNumber of onto functions from S to T:", num_onto)

# Display all of the onto functions
print("All of the onto functions from S to T:\n")
for i, f in enumerate(onto):
    print(f"{i+1}: {f}")

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
for i, f in enumerate(onto):
    print(f"{i+1}: {f}")
