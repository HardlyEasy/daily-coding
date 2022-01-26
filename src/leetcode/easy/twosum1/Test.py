import random
import time

from leetcode.easy.twosum1.Solution import Solution

my_solution = Solution()

bigArray = []
for i in range(0, 2000000):
    bigArray.append(random.randint(0, 1000000))
startTime = time.time()
answer = my_solution.twoSum(bigArray, 500)
endTime = time.time()
print(round(endTime - startTime, 2), 'seconds')
print('indexes:', answer)
print('numbers:', bigArray[answer[0]], bigArray[answer[1]])