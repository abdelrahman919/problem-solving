n= input('enter number')
n= int(n) 
m = n 

counter = 0
    #line count
for i in range(0,2*n-1):

   #printing 1st character always constant
    print(n,' ',end="")

        #printing 1st half of columns
    acounter =0
    for a in range(1,(n-1)):
        
        if i < a or i == 0 :
            k = n -i

        elif i >= a:
            if i > n and (n-2)-a == counter:
                
                #printing last line 
                if i == 2*n-2:
                    k = n 
               #print back accendingly
                for b in range(0,counter+1):
                    print(k,' ',end="")
                counter +=1
                break
            #to print discendingly0
            else:
                k = n -a
                       
        print(k,' ',end="")

    #print number in the middle 
    if i < n:
        m= n - i 
    else: 
        m  +=1
    print(m,' ',end='')  

    #print 2nd half of columns 

    counter2 =1
    for c in range(1,n-1):
        
        if i == 0 or i == 2*n-2: 
            j = n
            
        elif abs(i-n) <= c and i < n :
            j = m +counter2 
            counter2 +=1
        
        elif i >= n and abs(i - n+2) <=c :
            j = m +counter2
            counter2 +=1

        else:
            j = m

        print(j,' ',end='')

    print(n,end=None)  
    





    
 
    
            
    









  
