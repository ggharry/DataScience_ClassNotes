import itertools
import operator
from collections import defaultdict

v = [1,2,3,4]
w = [5,6,7,8]

print list(itertools.izip(v, w))

# Most basic functions in python will have i in the front

# itertools.starmap(operator.mul, itertools.izip(v, w))

# list comprehension

assert cols_a == rows_b # returns an exception if it's false

# tree will be defaultdict of a dictionary recursively
tree = lambda: defaultdict(tree)
data = tree()