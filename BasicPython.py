import math
#Let a, b, and c be the length of the 3 sides of an triangle. Find its area and perimeter of the triangle

str = """a = int(input("\n\t Enter the 1st side: "))
b = int(input("\n\t Enter the 2nd side: "))
c = int(input("\n\t Enter the 3rd side: "))

s = (a+b+c)/2
print("\n\t Perimeter = ", s)

area = (s*(s-a)*(s-b)*(s-c))**0.5
print("\n\t Area = ", area)
"""

#Let f be the temparature in fahrenheit. Convert it into celcius using the formula c = f*9/5+32

str2 = """ch = int(input("\n\t Enter your choice: "))

if ch==1:
  c = float(input("\n\t Enter temperature in c: "))
  f = c*9/5 + 32
  print("\n\t ",c, "C = ", f, "F")
  
elif ch==2:
  f = float(input("\n\t Enter temperature in f: "))
  c = f*9/5 + 32  
  print("\n\t ",f, "F = ", c, "C")
  
 """
# Let a point P be given in polar coordinates (r,θ). Find the equivalent point in Cartesian Coordinates (x,y) using the formula: x = r × cos( θ ); y = r × sin( θ )  
str3 = """
r = float(input("\n\t Enter the radius: "))
thetha = float(input("\n\t Enter the angle in degree: "))

x = r*math.cos(thetha)
y = r*math.cos(thetha)

print("\n\t x -> ", x)
print("\n\t y ->", y)
"""

#To check whether a given year is leap year or not.
#Rules:
#i. If year is divisible by 400 then Print (Year, ‘is a leap year’)
#ii. Else if year is divisible by 100 then Print (Year, ‘is not a leap year’)
#iii. Else if year is divisible by 4 then Print (Year, ‘is a leap year’)
#iv. Else Print (Year, ‘is not a leap year’)

str3="""yy = int(input("\n\t Enter the year to check: "))

if (yy%400==0) or (yy%4==0) and (yy%100!=0):
   print("\n\t It is a leap year!")
   
else:
   print("\n\t Ordinary Year!!")
   """
#Check whether a given date is valid or not.
str = """dd = int(input("\n\tEnter date: "))
mm = int(input("\n\tEnter month: "))
yy = int(input("\n\tEnter year:  "))
flg = False

L = [dd, mm, yy]
print("\n\t",L)

if (dd==0 or mm==0 or yy==0):
   flg = False
   
if (yy%400!=0) or  (yy%4!=0) or (yy%100!=0):  
  if (mm==2):
    if(dd<=28):
      flg = True
    else:
      flg = False
          
if (mm>12):
   flg = False
   
if(mm==4 or mm==6 or mm==9 or mm==11 and mm!=2):
  if(dd<=30 and dd>0):
    flg = True
  else:
    flg = False
    
if(mm!=4 or mm!=6 or mm!=9 or mm!=11 and mm!=2):
  if(dd<=31 and dd>0):
    flg = True 
  else:
    flg = False
       
if (yy%400==0) or (yy%4==0) and (yy%100!=0):
   if(mm==2):
      if(dd<=29):
        flg = True
        
      else:
        flg = False
        
if (flg == True):
   print("\n\t Valid date!!")
else:
   print("\n\t Invalid date!!")           
"""

#Given the sides of a triangle, check whether triangle is equilateral, scalene or isosceles or not                  

str="""a = int(input("\n\t Enter 1st side: "))
b = int(input("\n\t Enter 2nd side: "))
c = int(input("\n\t Enter 3rd side: "))

if (a==b) and (b==c):
  print("\n\t ABC is an equilateral triangle!")
  
if (a==b) or (b==c) or (a==c):
  print("\n\t ABC is an isosceles triangle!")   
  
if (a!=b and b!=c and a!=c):
  print("\n\t ABC is a scalene triangle!")  
 """
 
#A Tribonacci sequence is defined as: tn = tn-1+tn-2+tn-3 if n>3 and t1=0, t2=1, t3=2.Print the first ‘n’ terms of the sequence. 
str = """
n = int(input("\n\t Enter the no of terms in sequence: "))

t0 = 0
t1 = 1

print("\n", t0, "\n", t1)
for i in range(3, n):
  t = t0+t1
  t0 = t1
  t1 = t
 
  print("",t)
  """
#Get input of n integers from the user one by one and print the number of positive, negativeand zeros. Also find the sum and average of all positive and negative numbers separately.  
strz = """
num = int(input("\n\t Enter length of sequence: "))
L = []
total1=0
total2=0
for i in range(num):
   a = int(input("\n\t Enter elt: "))
   L.append(a)
   
print("", L)

for ele in range(0, num):
   if L[ele]>=0:
      total1 = total1+L[ele]
print("\n\t Sum of positive numbers: ", total1)    
    
for ele in range(0, num):
   if L[ele]<0:
      total2 = total2+L[ele]
print("\n\t Sum of negative numbers: ", total2)  
 """
 
 
     
