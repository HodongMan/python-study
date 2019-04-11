from functools import reduce
from operator import add
from factorial import factorial

if __name__ == "__main__":

    print( reduce(add, range(100)) )
    print( sum(range(100)) )
    print( list(map(factorial, filter(lambda n: n % 2, range(6)))) )