n = int(input())
lst= list() 
counter = 0
dct = dict()

for i in range(0,n):
    k = input()
    if k not in dct:
        dct[k]=1
    else:
        dct[k] +=1

print(len(dct))
for i in dct.keys():
    print(dct[i],end=' ')
















    #my 1st solution didnt pass time limit 



""" for i in range(0,n):
    lst.append(input())



set1= set(lst)
print(len(set1))


#we get the count of 1st item then remove all occurances of it in the list 

for i in range(0,len(set1)):
    #print(lst)
    k = lst[0] 
    counter = lst.count(k)
    
    lst= list(filter((k).__ne__, lst))



    print(counter,end=' ') """






#https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true






# print(lst)
 