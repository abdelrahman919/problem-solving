
#my 1st solution which i think isnot optimal 

import itertools
keys= []
groups=[]
counter=0
s = input()
data1= list(map(str,s))


for k, g in itertools.groupby(sorted(data1)):
    keys.append(k)
    groups.append(list(g))

count  =[len(i) for i in groups]

dct= dict(zip(keys,count))


#difference between the 2 solutions stars here 

keys = sorted(list(dct.keys()))
values = sorted(list(dct.values()),reverse=True)


for j in range(3):
    for i in keys:


        key=  i
        cv= values[j] 

        if dct[key] == cv:
            print(key,cv)
            dct.pop(key)
            keys.remove(i)
            break



        #OR
        #my 2nd solution 
        #Think this is a better solution since we dont need to remove any keys from dicts
        #values has to be set not list to avoid output duplication 
        

""" keys = sorted(list(dct.keys()))
values = sorted(set(dct.values()),reverse=True) 
itms = sorted(dct.items())

for i in values :

        if counter>=3:
                break
        else:
                for j in itms:
                        if i in j:
                             
                                print(j[0],i)
                                counter+=1
                             
                                if counter>=3:
                                        break """
                
   
         
    

#https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true


