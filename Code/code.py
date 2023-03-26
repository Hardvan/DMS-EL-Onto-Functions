
# ? Problem Statement
# * Calculate the number of onto functions from a
# * set A to a set B, where A and B are finite sets of
# * various sizes. List all of them.

from itertools import product


def fact(n):
    """Returns the factorial of n.
    """

    if n <= 1:
        return 1
    return n * fact(n - 1)


def nCr(n, r):
    """Returns C(n, r)
    """

    return (fact(n) / (fact(r) * fact(n - r)))


def calculate_onto(A, B):
    """Calculate the number of onto functions from A to B.
    """

    # Calculate the number of onto functions from A to B
    m = len(A)
    n = len(B)
    # m >= n for valid onto function
    if m < n:
        print("There are no onto functions from A to B.")
        return 0, []

    num_onto = 0
    # n! * Sterlings Formula of the Second Kind
    for k in range(0, n):  # 0 to n-1
        num_onto += ((-1)**k) * nCr(n, n-k) * ((n-k)**m)

    # List all of the onto functions from A to B
    onto = []
    for b in product(B, repeat=m):  # Combinations with repetition
        if len(set(b)) == n:  # b contains all elements of B (range = co-domain)
            onto.append(dict(zip(A, b)))

    # product here generates all possible combinations
    # of elements in set B with length m.
    # Eg: B = {1, 2}, m = |A| = 3
    # product(B, repeat=m)
    # = {(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2),
    # (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)}

    return int(num_onto), onto


def calc_and_display(A, B):
    """Calculate and then display the number of onto functions from A to B and lists all of them.
    """

    num_onto, onto = calculate_onto(A, B)

    print("\nNumber of onto functions from A to B:", num_onto)

    if num_onto == 0:
        print("There are no onto functions from A to B.")
        return

    print("All of the onto functions from A to B:\n")
    for i, f in enumerate(onto):
        print(f"{i+1}: {f}")


# Example Usage
A = {1, 2, 3, 4}
B = {'a', 'b', 'c'}

print("A:", A)
print("B:", B)

calc_and_display(A, B)

print("---------------------------------")

print("Try with your own sets of integers!\n")

print("Enter a set A of integers separated by spaces:")
A = set(map(int, input().split()))
print("Enter a set B of characters separated by spaces:")
B = set(input().split())

calc_and_display(A, B)
