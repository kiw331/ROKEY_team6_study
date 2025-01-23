import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())

plusQ = PriorityQueue()
minusQ = PriorityQueue()
one = 0
zero = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    if (num > 1):
        plusQ.put(num * -1)
    elif (num == 1):
        one += 1
    elif (num == 0):
        zero += 1
    else:
        minusQ.put(num)

result = 0

while (plusQ.qsize() > 1):
    num1 = plusQ.get()
    num2 = plusQ.get()
    result += num1 * num2

if (plusQ.qsize() > 0):
    result += plusQ.get() * -1

while (minusQ.qsize() > 1):
    num1 = minusQ.get()
    num2 = minusQ.get()
    result += num1 * num2

if (minusQ.qsize() > 0):
    if (zero == 0):
        result += minusQ.get()

result += one
print(result)