import cProfile


def prime(n):
    primes = []
    counter = 0

    for i in range(2, 100 * n):
        flag = True

        if i < 3:
            primes.append(i)
            counter += 1

        for item in primes:
            if i % item == 0:
                flag = False

        if flag:
            primes.append(i)
            counter += 1

        if counter == n:
            return primes[n - 1]

# -------- timeit -------------------------
# prime(10)"
# 1000 loops, best of 5: 11.4 usec per loop
#
# prime(20)"
# 1000 loops, best of 5: 41.4 usec per loop
#
# prime(50)"
# 1000 loops, best of 5: 277 usec per loop
#
# prime(100)"
# 1000 loops, best of 5: 1.26 msec per loop


# -------- cProfile -------------------------
# cProfile.run("prime(10)")
# 1    0.000    0.000    0.000    0.000 task_2_1.py:4(prime)
#
# cProfile.run("prime(100)")
# 1    0.001    0.001    0.002    0.002 task_2_1.py:4(prime)
#
# cProfile.run("prime(1000)")
# 1    0.225    0.225    0.225    0.225 task_2_1.py:4(prime)
#
# cProfile.run("prime(10000)")
# 1   27.834   27.834   27.835   27.835 task_2_1.py:4(prime)
