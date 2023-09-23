
#key is to determine location of min number so that we know whether we need to increment or decrement 
#To do so we use a counter and if condition 


t = int(input())
#the code was applied to t test cases hence the for loop(line 25)
for i in range(t): 

    n =int(input())
    lst1 = []
    cubes=input()

    lst1=list(map(int,cubes.split()))

    max1 =max(lst1)
    min1 = min(lst1)
    counter = 0
    answer = 'Yes'

    for i in range(n-1):
        Current = lst1[i]
        nxt = lst1[i+1]

        if Current == min1:
            counter =1

        if counter == 0 and nxt <= Current:
            answer = 'Yes'

        elif counter == 1 and nxt >= Current:
            answer = 'Yes'
        else:
            answer = 'No'
            break

    print(answer)





#https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true






