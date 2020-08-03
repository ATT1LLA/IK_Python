# Решето Эратосфена быстрее чем первый алгоритм
import cProfile


def prime(n):
    primes = [i for i in range(2, 10 * n)]
    count = 0

    for item in primes:
        i = 2

        if item != 0:
            count += 1
            if count == n:
                return item

            while item * i - 2 < 5 * n:
                try:
                    primes[item * i - 2] = 0
                except IndexError:
                    pass
                i += 1

# -------- timeit -------------------------
# prime(10)"
# 1000 loops, best of 5: 16.2 usec per loop
#
# prime(20)"
# 1000 loops, best of 5: 31.8 usec per loop
#
# prime(50)"
# 1000 loops, best of 5: 91.5 usec per loop
#
# prime(100)"
# 1000 loops, best of 5: 252 usec per loop


# -------- cProfile -------------------------
# cProfile.run("prime(10)")
# 1    0.000    0.000    0.000    0.000 task_2_2.py:4(prime)
#
# cProfile.run("prime(100)")
# 1    0.000    0.000    0.000    0.000 task_2_2.py:4(prime)
#
# cProfile.run("prime(1000)")
# 1    0.004    0.004    0.005    0.005 task_2_2.py:4(prime)
#
# cProfile.run("prime(10000)")
# 1    0.044    0.044    0.049    0.049 task_2_2.py:4(prime)
