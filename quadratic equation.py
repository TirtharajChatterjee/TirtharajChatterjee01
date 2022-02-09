import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
d = (b**2) - (4*a*c)  
num1 = (-b-cmath.sqrt(d))/(2*a)  
num2 = (-b+cmath.sqrt(d))/(2*a)  
print(f"The equations are = {num1,num2}")   
