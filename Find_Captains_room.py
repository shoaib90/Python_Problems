# For problem refer to this below url:
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

#Solution

k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))

We simply calculate the difference in what the sum would be if there were K elements of all groups. We will have k-1*captains room number left, we simply didve by k-1 to get the answer.