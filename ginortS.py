n = input()
lower= upper = first = second =  ''
odd = even = third = fourth = ''
for i in n :
    if i.isalpha():
        if i.islower():
           lower += i
        else:
            upper +=i
    if i.isdigit():
        if int(i) %2 !=0:
            odd +=i
        else:
            even +=i


for i in sorted(lower):
    first +=i
for i in sorted(upper):
    second +=i
for i in sorted(odd):
    third +=i
for i in sorted(even):
    fourth +=i

print(first+second+third+fourth)



























#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true