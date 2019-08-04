
import timeit

for x in range(10):

  for y in range(5):
    ans = 3+3
    time = timeit.timeit(ans)
    print (time)


