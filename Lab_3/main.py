import time
import matplotlib.pyplot as plt
import math

def alg1(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        if c[i]:
            j = 2 * i
            while j <= n:
                c[j] = False
                j += i
        i += 1
    return c


def alg2(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1
    return c


def alg3(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1
    return c


def alg4(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        j = 1
        while j < i:
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    return c


def alg5(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while i <= n:
        j = 2
        while j <= int(math.sqrt(i)):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    return c


def plot_results(results):
    fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))
    ax1.set_title('Execution Time')
    ax1.set_xlabel('Input Size')
    ax1.set_ylabel('Time (Seconds)')
    ax1.plot(results.keys(), [res[0] for res in results.values()], label='Algorithm 1')
    ax1.plot(results.keys(), [res[1] for res in results.values()], label='Algorithm 2')
    ax1.plot(results.keys(), [res[2] for res in results.values()], label='Algorithm 3')
    ax1.plot(results.keys(), [res[3] for res in results.values()], label='Algorithm 4')
    ax1.plot(results.keys(), [res[4] for res in results.values()], label='Algorithm 5')
    ax1.legend()
    plt.show()

if __name__ == '__main__':
    results = {}
    for i in range(1000, 10000, 2000):
        t1 = time.time()
        alg1(i)
        t2 = time.time()
        alg2(i)
        t3 = time.time()
        alg3(i)
        t4 = time.time()
        alg4(i)
        t5 = time.time()
        alg5(i)
        t6 = time.time()
        results[i] = (t2 - t1, t3 - t2, t4 - t3, t5 - t4, t6 - t5)
    plot_results(results)