
n = input('enter number')

try: 
    n =int(n)
except:
    print('wrong usage') 
    exit()
    
    
counter = 0
for i in range (1,n):
    if n%i == 0:
       counter += 1

if counter == 1:
    print ('prime')
else:
    print('not prime')



