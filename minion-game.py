        #my solution

s = input('type s  ')
counter1 , counter2 = 0 , 0

for i in range(1,len(s)+1):
   
    for j in range(0,len(s)):
        letter = s[j]
        if j+i > len(s):
            break

        else:
                
                if letter not in ['A','E','U','I','O']:
                    k = s[j:j+i]
                    counter1+=1
                    #print(k)

                else:
                    v = s[j:j+i]
                    counter2 +=1
                    #print('V= ',v)

            
if counter1 > counter2:
    print('Stuart', counter1)
elif counter1 < counter2:
    print('Kevin', counter2)
else:
    print('draw')



        




       
      
       
       
        #https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true