'''
https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/mathison-and-the-funny-substring-b3f58587/

This problem can thought as demonstration of dict data structure in python3 (haskeys function which is in python 2 is 
deprecated in keys function in python3)

here funny substring is define as a string whose first number and last number are same


This problem belongs to greedy paradigm since we have to find max length of funny substring 
so we store first occurance of number( which is treated as key) and index is value for that key
next time that number appear we can calculate the length

'''
N = int(input())
l = {}
# strating with zero is not alloud
i=0
maxxfun = 1
p = list(map(int, input().split(' ')))
while i<N:
    a = p[i]
    
    if a not in l.keys():
        l[a] = i
        
    else:
        maxxfun = max(maxxfun, (i-l[a]+1))
        #print(maxxfun)
    i += 1
print(maxxfun)
