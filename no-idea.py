
happiness = 0


n,m = map(int, input().split())
 
array = list(map(int, input().split()))

a = set(map(int,input().split() ))

b = set(map(int, input().split()))


for i in array:
    if i in a:
        happiness +=1
    elif i in b:
        happiness-=1


print(happiness)




                    #or this solution 
                    #the key is convertin a & b to sets to reduce run time 

""" happiness = 0
a = b= set()

n, m = [int(x) for x in input().split()]

array = [int(x) for x in input().split()]

a = set([int(x) for x in input().split()])

b = set([int(x) for x in input().split()])
 

for i in array:
    if i in a:
        happiness +=1
    if i in b:
        happiness -=1

print(happiness)  """




#https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true