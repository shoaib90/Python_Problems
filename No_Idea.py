# #problem

# There is an array of n integers. There are also 2 disjoint sets,A  and B, each containing m integers. 
# You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
# For each i integer in the array, if i∈A, you add 1 to your happiness. If i∈B, you add -1 to your happiness. 
# Otherwise, your happiness does not change. Output your final happiness at the end.

# Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Input Format

# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.

# Output Format

# Output a single integer, your total happiness.

# Sample Input

# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output

# 1

#solutions

# 1st way

n,m = input().split()
arr = input().split()
A = set(map(str,input().split()))
B = set(map(str,input().split()))
happiness = 0
for i in arr:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1


print(happiness)


# Second Way
n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))
