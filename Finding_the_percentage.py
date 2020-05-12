# Sample Input 0:													

# 3																
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output 0:
# 56.00

# Explanation:
# Marks for Malika {52,56,60} are  whose average is  52+56+60/3 => 56

# Sample Input :1						Sample Output:1  
# 2										26.50
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh

#Answers :-

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    count = 0
    for i in student_marks[query_name]:
        count = count + i

    avg = count / len(student_marks[query_name])

    print("{:.2f}".format(avg))
