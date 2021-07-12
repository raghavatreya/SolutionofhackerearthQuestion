'''
https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/motu-and-patlu-1-ab612ad8/

In this question the greedy step is take the atleast twice ice cream for motu
then pick the ice cream for patlu

! Be cautious About the list out of Bound Error

'''
# Write your code here
t = int(input())
while t >= 1:
    t = t-1
    n = int(input())
    l = list(map(int,input().split(' ')))
    motu = 0
    patlu = 0
    i = 0
    j = len(l) -1
    psum = msum = 0
    while not i>j:
        while msum <= 2*psum  and not i>j:
            msum += l[i]
            i += 1
            motu += 1
        while msum >= 2*psum and not i>j:
            psum += l[j]
            j -= 1
            patlu += 1

        
    if motu>patlu:
        print(motu,patlu,"\nMotu")
    elif motu<patlu:
        print(motu,patlu,"\nPatlu")
        
        
        
        
    else:
        print(motu,patlu,"\nTie")
    
# This code is not readable

def setdefault_example():
    std_dict = dict()
    for k, v  in enumerate(range(5)):
        std_dict.setdefault(k, []).append(v)
    return std_dict

setdefault_example()



operations_count = 0

def main():
    ask_again = True
    while(ask_again):
        a = input("Enter the numerator: ")
        b = input("Enter the denominator: ")
        result = perform_division(a,b)
        print(result)
        ask_again = input("Do you want to perform another operation? Enter yes or no: ")
        if(ask_again == 'yes'):
            ask_again = True
        else:
            ask_again = False
            print("You performed " + str(operations_count) + " operations, bye!")


def perform_division(a,b):
    global operations_count
    try:
        operations_count += 1
        return int(a)/int(b)
    except Exception as e:
        pass


main()
