import re
t = int(input())

for i in range(t):
    n= input()
    counter =0
    counter2 = 0
    counter3=0
    card=re.match("^[4,5,6]\d{3}-?\d{4}-?\d{4}-?\d{4}",n)

    result='Valid'



    for i in n:
        if i =='-':
            counter3+=1
    if counter3 !=0 and counter3 != 3:
        result='Invalid'


        
    test= n.replace('-','')

    for i in range(len(test)-1):    
        current = test[i] 
        nxt = test[i+1]
        if nxt == current:
            counter2 +=1
        else:
            counter2=0

        if counter2>=3:
            result='Invalid' 
            break


    try:
        cardg = card.group()

        if n != cardg :
            result = 'Invalid'
        
    except AttributeError:
        result = 'Invalid'
       
    print(result)





#https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true









