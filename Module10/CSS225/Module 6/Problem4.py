import math

def leibniz_pi_approximation(n):
    approximation = 0
    for k in range(n):
        approximation += (-1)**k / (2*k + 1)
    return 4 * approximation


n_terms = 100000
approximation = leibniz_pi_approximation(n_terms)

# Print the approximation and the value of math.pi
print(f"Approximation of pi: {approximation}")
print(f"Value of math.pi: {math.pi}")
