# A lambda function is a small anonymous function. that can take any number of arguments,
# but can only have one expression.

# Syntax - [ lambda arguments : expression ]

# 1. perform a simple addition using a lambda function
from functools import reduce

add = lambda x, y: x + y
print(add(1, 2))
# result - 3

# 2. given a list perform a simple sort operation to find the values greater than 5
seq = [2, 7, 8, 4, 0, 3, 10, 13, 23, 1]
sort = filter (lambda x : (x > 5), seq)
print(list(sort))
# result - [7, 8, 10, 13, 23]

# 3. use map function in lambda functions to per form the square oparation on each element of a given sequence
seq = [2, 7, 8, 4]
sort = map (lambda x : (x * x), seq)
print(list(sort))
# result - [4, 49, 64, 16]

# 4. use reduce function in lambda function to multiply some numbers given in a list
seq = [2, 7, 8, 4]
sort = reduce (lambda x , y: (x * y), seq)
print(sort)
# result - 448
