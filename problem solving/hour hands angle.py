#every min is 6 degrees 
#every hour is 30 degrees
""" 
h = input('type hour')
m = input('enter minutes')
h= int(h) 
m= int(m)
angle = h*30+m/10 -m*6 

print(angle) """


h = input('type hour')
m = input('enter minutes')
h= int(h) 
m= int(m)
angle = abs(m*6 - h*30 ) 

print(angle)