# Определить, какое число в массиве встречается чаще всего.
import random
import cProfile


def counter(n):
    array = [random.randint(0, n // 5) for i in range(n)]
    maxx, count = 0, 0

    for i in range(len(array)):

        for item in array:
            if item == array[i]:
                count += 1

    maxx = array[i] if count > maxx else maxx
    count = 0

    return maxx


# -------- timeit -------------------------
# counter(10)"
# 1000 loops, best of 5: 15.3 usec per loop
#
# counter(20)"
# 1000 loops, best of 5: 38.1 usec per loop
#
# counter(50)"
# 1000 loops, best of 5: 157 usec per loop
#
# counter(100)"
# 1000 loops, best of 5: 526 usec per loop

# -------- cProfile -------------------------
# cProfile.run("counter(10)")
# 1    0.000    0.000    0.000    0.000 task_1_1.py:6(counter)
#
# cProfile.run("counter(100)")
# 1    0.001    0.001    0.001    0.001 task_1_1.py:6(counter)
#
# cProfile.run("counter(1000)")
# 1    0.052    0.052    0.054    0.054 task_1_1.py:6(counter)
#
# cProfile.run("counter(10000)")
# 1    4.414    4.414    4.435    4.435 task_1_1.py:6(counter)
