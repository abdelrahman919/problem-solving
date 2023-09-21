
    #not the cleanest but code is code 
    #using nxt variable and counter along wirh bzillion ifs to calculate the number of repitions

n = input()
lst = list(map(str, str(n)))

counter = 1
if len(lst) ==1:
    print(f'1, {n}',end=' ')
for i in  range(len(lst)-1):
    
    current= lst[i]
    nxt= lst[i+1]
    #print('current is '+current+ 'nxt is '+ nxt)

    if current == nxt and len(lst)-1 -i !=1:
        counter +=1

    elif current == nxt and len(lst)-1 -i ==1:
        counter +=1
        print(f'({counter}, {current})',end=' ')
    
    

    else:

        if len(lst)-1 -i !=1:
            print(f'({counter}, {current})',end=' ')
        else:
            print(f'({counter}, {current})',end=' ')
            print(f'(1, {nxt})',end=' ')
            


        counter =1



    #https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true































