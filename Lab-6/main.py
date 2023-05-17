import math
from decimal import Decimal, getcontext
import time
import matplotlib.pyplot as plt


def calculate_pi_gauss_legendre(n):
    # Set the decimal precision
    getcontext().prec = n + 2  # Additional precision to ensure accuracy

    # Initialize variables
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(0.25)
    p = Decimal(1)

    # Iterate to converge to the desired precision
    for _ in range(n):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    # Calculate pi using the converged values
    pi = (a + b) ** 2 / (4 * t)

    return pi


def calculate_pi_bbp(n):
    # Set the decimal precision
    getcontext().prec = n + 2  # Additional precision to ensure accuracy

    # Calculate pi using the BBP algorithm
    pi = Decimal(0)
    for k in range(n + 1):
        pi += (Decimal(1) / 16 ** k) * (
                (Decimal(4) / (8 * k + 1)) -
                (Decimal(2) / (8 * k + 4)) -
                (Decimal(1) / (8 * k + 5)) -
                (Decimal(1) / (8 * k + 6))
        )

    return pi


# calculate the nth pi number using ramanujan's formula
def calculate_pi_ramanujan(n):
    # Set the decimal precision
    getcontext().prec = n + 2  # Additional precision to ensure accuracy

    # Calculate pi using Ramanujan's formula
    pi = Decimal(0)
    for k in range(n + 1):
        pi += (Decimal(math.factorial(4 * k)) / (Decimal(math.factorial(k)) ** 4)) * (
                Decimal(1103) + Decimal(26390) * k) / (Decimal(99) ** (4 * k))

    pi *= Decimal(1) / (Decimal(2) * Decimal(2).sqrt() / Decimal(9801))

    return pi


# create a function to calculate the time taken to calculate pi for each algorithm
def calculate_time_taken(n):
    # Calculate the time taken to calculate pi using the Gauss-Legendre algorithm
    start_time = time.time()
    pi_gauss_legendre = calculate_pi_gauss_legendre(n)
    end_time = time.time()
    time_taken_gauss_legendre = end_time - start_time

    # Calculate the time taken to calculate pi using the BBP algorithm
    start_time = time.time()
    pi_bbp = calculate_pi_bbp(n)
    end_time = time.time()
    time_taken_bbp = end_time - start_time

    # Calculate the time taken to calculate pi using Ramanujan's formula
    start_time = time.time()
    pi_ramanujan = calculate_pi_ramanujan(n)
    end_time = time.time()
    time_taken_ramanujan = end_time - start_time

    return time_taken_gauss_legendre, time_taken_bbp, time_taken_ramanujan


# create a function to plot the time taken to calculate pi for each algorithm using matplotlib
def plot_time_taken(n):
    # Calculate the time taken to calculate pi for each algorithm
    time_taken_gauss_legendre, time_taken_bbp, time_taken_ramanujan = calculate_time_taken(n)

    # Create a list of algorithm names
    algorithms = ['Gauss-Legendre', 'BBP', 'Ramanujan']

    # Create a list of time taken for each algorithm
    times = [time_taken_gauss_legendre, time_taken_bbp, time_taken_ramanujan]

    # Plot the time taken to calculate pi for each algorithm
    plt.bar(algorithms, times)
    plt.ylabel('Time taken (s)')
    plt.xlabel('Algorithm')
    plt.title(f'Time taken to calculate pi for n={n}')
    plt.show()


# Example usage
n = 1000  # Choose the desired digit position or precision

# Call the function to plot the time taken
plot_time_taken(n)
