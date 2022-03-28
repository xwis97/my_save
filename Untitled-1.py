#x = 5
#y = 10
#print((y > x * x) or ((y >= 2 * x) and (x < y)))


#a = True
#b = False
#print((a and b) or (not a) and (not b))

'''
a = float(input())
b = float(input())
c = float(input())

if ((a>0 and b>0) and c>0):
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c)**0.5)    
          
elif((a>0 and b>0) and c==0):
           print(a*b)
                      
          
elif((a>0 and b==0) and c==0):
          print(a*3.14)
    

a = int(input())
b = int(input())
c = int(input())

set = [a, b, c]
print(max(set))

    

s = input()
if((s[-1]=='2') or (s[-1]=='3') or (s[-1]=='4'))and(s[-2] != '1'):
    print(s, ' программиста')
elif((s[-1]=='1') and (s[-2] != '1')):
    print(s, ' программист')
else:
    print(s, ' программистов')
    
a = input()
i = 0
s = 0
while a[i] != 0:
    i += i
    s += int(a[i])
print(s)

s = 0
a = 0
while True:
    a = int(input())
    s += a
    if(a==0):
        print(s)
        

a = int(input())
b = int(input())
i = 0

while True:
    i+= 1
    l = 0
    
    if i == 3:
        break
    if a%i==0:
        print(i)
        1
        while l < 1000:
            l += 1
            if b%l==0:
                if i%l==0: 
                    print(i)
                    break



a = int(input())
b = int(input())


for i in range(a,b):
    print(i)


'''

#######a, b = (int(i)for i in input().split())
#    1234567891011

'''
s = 'abcdefghijk'
print(s[3:6])
print(s[:6])
print(s[3:])
print(s[::-1])
print(s[-3:])
print(s[:-6])
print(s[-1:-10:-2])
'''

#students = ['Ivan', 'Masha', 'Sasha']
#students += ['Olga']
##students += 'Olga'
#print(students)
'''
a = [1, 2, 3]
b = a
# значения списка b?
print(b)
a[1] = 10
# значения списка b?
print(b)
b[0] = 20
# значения списка a?
print(a)
a = [5, 6]
# значения списка b?
print(b)



while True:
     a = int(input())
     b = int(input())
     print(a%b)

 '''
 #Многомерный массив
'''
n = 2
a = [[1 for j in range(n)]for i in range(n)]
a[1][1] = 333
print(a) 
  
# a = [int(i) for i in input().split()]

'''


'''
global M, inX, inY, outX, outY, outN
x = 0
inX, inY, outX, outY, outN = 0, 0, 0, 0, 0
M = []
while True:
    a = [i for i in input().split()]
    if(a[0] =='end'):break
    M.append([int(inX) for inX in a])
    inX=len(a)
    inY+=1
for outY in range(inY):
    for outX in range(inX):
        outN=M[outY - 1][outX] + M[(outY+1)%inY][outX] + M[outY][outX - 1] + M[outY][(outX+1)%inX]
        print(outN, end=' ')
        
    print() 
'''

'''
n = 20
M = [[1 for j in range(n)]for i in range(n)]
e=0
x = -1
y = 0
clc = 0
nap = True
while e != n*n:
    if nap == True:
        for x1 in range(n - clc):
             x+=1
             e+=1
             M[y][x] = e
        clc +=1
        for y1 in range(n - clc):
             y+=1
             e+=1
             M[y][x] = e   
        for x1 in range(n - clc):
             x-=1
             e+=1
             M[y][x] = e
        clc +=1
        for y1 in range(n - clc):
             y-=1
             e+=1
             M[y][x] = e  
for l in range(n):
    for r in range(n):
        print(M[l][r], end = ' ')
    print()
'''

'''

def modify_list(lst):
    r = 0
    inw = ''
    for i in range(len(lst)):
        if int(lst[i])%2==0:
            inw+=  lst[i]//2
            r+=1
    lst = inw
'''

'''
from tkinter.messagebox import YESNOCANCEL
from webbrowser import get
def update_dictionary(d, key, value):
    if d.get(key) == None:
        if d.get(key*2) == None:
            l = []
            l.append(value)
            d[key*2] = l
        else:
            x = []
            x = d[key*2]
            x.append(value)
            d[key*2] = x      
    else:
        y = []
        y = d[key]
        y.append(value)
        d[key] = y
         
        
        
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''

'''
r = 0
y = {}
x = [i for i in input().split()]
for i in x:
    x[r] = i.lower()
    y[x[r]] = 0
    r +=1
for i in x:
    y[i] += 1 
for key , value in y.items():
    print(key, value)

'''
## x={} x[key] = value       

#s = input().lower().split()
#print(s)


'''

with open('dataset_3363_2.txt', 'r') as inf:
    s = inf.readline()
n = ''
x = ''
y = ''
oldx = ''
print(s)
for a in range(len(s)-1):
    if not('0'<=s[a]<='9'):
        x = s[a]
    if '0'<=s[a+1]<='9':
        n = s[a+1] 
        if a+2 < len(s):
            if '0'<=s[a+2]<='9':
                 n += s[a+2]
                 
    if oldx != x:
        if n != '':
            y += x*int(n)
            
    oldx = x
    
    n=''

with open('dataset_3363_2.txt', 'w') as ouf:
   ouf.write(y)    

'''




'''       
y = {}
text = open("text.txt", 'r')
s = text.read().replace('\n', ' ').lower().split()
text.close()
n = 0
for i in set(s):
   y[i] = s.count(i)
for key, value in y.items():
    if value > 5:
        print(key, value)
    
'''       

   





text = open("text.txt", 'r')
s = text.read().replace('\n', ';').split(';')
mat=0
fiz=0
rus=0

text.close()
for i in range(0,len(s)-1,4):
    print(str((int(s[i+1])+int(s[i+2])+int(s[i+3]))/3)) 
    mat += int(s[i+1])
    fiz += int(s[i+2])
    rus += int(s[i+3])
num = len(s)//4
print(mat/num, fiz/num, rus/num)    
    
#s[i]+ ' ' + 
    

    
   

    


