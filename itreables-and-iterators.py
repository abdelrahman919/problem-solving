import itertools

n = int(input())
lst = list(input().split())
k = int(input())

print(lst)
possiblity = list(itertools.combinations(lst,k))
possiblityN= len(possiblity)
possiblitya = 0
print(possiblity)

for i in possiblity:
    if 'a' in i:
        possiblitya +=1

result = possiblitya/possiblityN
print('%.3f' %result)



#https://www.hackerrank.com/challenges/iterables-and-iterators?isFullScreen=true