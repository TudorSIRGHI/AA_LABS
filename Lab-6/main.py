# import math
# from decimal import Decimal, getcontext
# import time
# import matplotlib.pyplot as plt
#
# def calculate_pi_chudnovsky(n):
#     # Set the decimal precision
#     getcontext().prec = n + 2  # Additional precision to ensure accuracy
#
#     # Calculate pi using Chudnovsky's formula
#     pi = Decimal(0)
#     for k in range(n + 1):
#         pi += (Decimal(math.factorial(6 * k)) / (
#             (Decimal(math.factorial(3 * k)) * Decimal(math.factorial(k)) ** 3))) * (
#                       Decimal(13591409) + Decimal(545140134) * k) / (Decimal(-640320) ** (3 * k))
#
#     pi *= Decimal(1) / (Decimal(12) * Decimal(640320) ** Decimal(1.5))
#
#     return pi
#
#
# def calculate_pi_borwein(n):
#     # Set the decimal precision
#     getcontext().prec = n + 2  # Additional precision to ensure accuracy
#
#     # Calculate pi using Borwein's formula
#     pi = Decimal(0)
#     for k in range(n + 1):
#         pi += (Decimal(2) ** Decimal(6 * k)) * (Decimal(math.factorial(k)) ** 3) * Decimal(
#             math.factorial(3 * k + 1)) * (
#                   Decimal(545140134 * k + 13591409)) / (
#                       Decimal(math.factorial(3 * k)) * Decimal(math.factorial(6 * k)) * Decimal(640320) ** (
#                           3 * k + Decimal(3 / 2)))
#
#     pi = Decimal(1) / pi
#
#     return pi
#
#
# def calculate_pi_machin(n):
#     # Set the decimal precision
#     getcontext().prec = n + 2  # Additional precision to ensure accuracy
#
#     # Calculate pi using Machin's formula
#     pi = Decimal(4) * (Decimal(4) * Decimal(math.atan(Decimal(1) / Decimal(5)))) - (
#         Decimal(math.atan(Decimal(1) / Decimal(239))))
#
#     return pi
#
#
# # create a function to calculate the time taken to calculate pi for each algorithm
# def calculate_time_taken(n):
#
#     start_time = time.time()
#     pi_chudnovsky = calculate_pi_chudnovsky(n)
#     end_time = time.time()
#     time_taken_chudnovsky = end_time - start_time
#
#     start_time = time.time()
#     pi_borwein = calculate_pi_borwein(n)
#     end_time = time.time()
#     time_taken_borwein = end_time - start_time
#
#     start_time = time.time()
#     pi_machin = calculate_pi_machin(n)
#     end_time = time.time()
#     time_taken_machin = end_time - start_time
#
#     return time_taken_chudnovsky, time_taken_borwein, time_taken_machin
#
#
# # create a function to plot the time taken to calculate pi for each algorithm using matplotlib
# def plot_time_taken(n):
#     # Calculate the time taken to calculate pi for each algorithm
#     time_taken_chundovsky, time_taken_borwein, time_taken_machin = calculate_time_taken(n)
#
#     # Create a list of algorithm names
#     algorithms = ['Chudnovsky', 'Borwein', 'Machin']
#
#     # Create a list of time taken for each algorithm
#     times = [time_taken_chundovsky, time_taken_borwein, time_taken_machin]
#
#     # Plot the time taken to calculate pi for each algorithm
#     plt.bar(algorithms, times)
#     plt.ylabel('Time taken (s)')
#     plt.xlabel('Algorithm')
#     plt.title(f'Time taken to calculate pi for n={n}')
#     plt.show()
#
#
# # Example usage
# n = 1000  # Choose the desired digit position or precision
#
# # Call the function to plot the time taken
# plot_time_taken(n)

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