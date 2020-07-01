#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import Generator
import math


def slow_primes(max: int) -> Generator[int, None, None]:
    numbers: Generator = (i for i in range(1, (max + 1)))
    for i in (n for n in numbers if n > 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            yield i


def primes(max: int) -> Generator[int, None, None]:
    numbers: Generator = (i for i in range(1, (max + 1)))
    for i in (n for n in numbers if n > 1):
        # only need to check for factors up to sqrt(i)
        bound = int(math.sqrt(i)) + 1
        for j in range(2, bound):
            if (i % j) == 0:
                break
        else:
            yield i


if __name__ == "__main__":
    number = int(input("Calculate primes up to:\n>> ").strip())
    for ret in primes(number):
        print(ret)

