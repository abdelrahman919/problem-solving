n,m = map(int, input().split())


lst = []
lst2=[]
final=[]
counter = 0

for i in range(n):
    lst.append(list(map(int, input().split())))
k = int(input())
for i in range(n):
    lst2.append(lst[i][k])

lst2s = sorted(lst2)
#print(lst2s)

for i in lst2s:
   # print('i is ',i)
    for j in range(n):
        if lst[j] != 'none':
            current = map(str,lst[j][k])
        # print('j is ',current)
            if str(i) == current:
                final.append(lst[j])
                lst[j]='none'
                #print('len is ',len(lst))
                #print('lst after ',lst)
                break
        
#print(final)

for i in range(n):
    current= list(map(int,final[i]))    
    for j in current:
        print(j,end=' ')
    print(end=None)


    #https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true