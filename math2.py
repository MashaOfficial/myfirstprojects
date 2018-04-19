
from math import tan

def simpson(f, a, b, n):
h = (b - a) / float(n)
sum1 = 0

for i in range(2, n, 2):
xi = a + h * (i - 1)
sum1 += f(xi)

sum1 *= 4
sum2 = 0

for i in range(1, n, 2):
xi = a + h * (i - 1)
sum2 += f(xi)

sum2 *= 2
result = h / 3.0 * (f(a) + f(b) + sum1 + sum2)

return result

def trapezoidal(f, a, b, n):
h = float(b - a)/n
result = 0.5*(f(a) + f(b))
for i in range(1, n):
result += f(a + i*h)
result *= h
return result

def rectangular(f, a, b, n):
h = float(b - a)/n
result = f(a+0.5*h)
for i in range(1, n):
result += f(a + 0.5*h + i*h)
result *= h
return result

def f(x):
return tan(x**2 + 0.5)/(1 + 2*(x**2))

print ('Simpson: ')
for n in 3,9,27,81,243:
result = simpson(f,0.4,0.8,n)
print('n={0}: approx={1}, error={2}'.format(n,result,2-result))

print ('Trapezoidal: ')
for n in 3,9,27,81,243:
result = trapezoidal(f,0.4,0.8,n)
print('n={0}: approx={1}, error={2}'.format(n,result,2-result))

print ('Rectangular: ')
for n in 3,9,27,81,243:
result = rectangular(f,0.4,0.8,n)
print('n={0}: approx={1}, error={2}'.format(n,result,2-result)) 
