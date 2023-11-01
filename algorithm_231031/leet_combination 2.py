import itertools
from pprint import pprint
n, k = [4, 2]


def combine(n, k):
    return list(itertools.combinations(range(1, n + 1), k))


print(combine(n, k))
