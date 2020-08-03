import random
import cProfile


def counter(n):
    array = [random.randint(0, n // 5) for i in range(n)]
    number_dict = {}

    for item in set(array):
        number_dict[item] = 0

    for item in array:
        number_dict[item] += 1

    max_count = 0
    max_key = 0

    for key in number_dict:
        if number_dict[key] > max_count:
            max_count = number_dict[key]
            max_key = key

    return max_key


# -------- timeit -------------------------
# counter(10)"
# 1000 loops, best of 5: 11.1 usec per loop
#
# counter(20)"
# 1000 loops, best of 5: 21.3 usec per loop
#
# counter(50)
# 1000 loops, best of 5: 49.4 usec per loop
#
# counter(100)"
# 1000 loops, best of 5: 94.9 usec per loop

# -------- cProfile -------------------------
# cProfile.run("counter(10)")
# 1    0.000    0.000    0.000    0.000 task_1_2.py:5(counter)
#
# cProfile.run("counter(100)")
# 1    0.000    0.000    0.000    0.000 task_1_2.py:5(counter)
#
# cProfile.run("counter(1000)")
# 1    0.000    0.000    0.002    0.002 task_1_2.py:5(counter)
#
# cProfile.run("counter(10000)")
# 1    0.002    0.002    0.023    0.023 task_1_2.py:5(counter)

# A lot faster than the first one
