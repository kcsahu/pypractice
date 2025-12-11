
import timeit
import sys

print(timeit.timeit("(1,2,3,4,5)", number=1000000))
print(timeit.timeit("[1,2,3,4,5]", number=1000000))

print(sys.getsizeof((1,2,3,4,5)))
print(sys.getsizeof([1,2,3,4,5]))