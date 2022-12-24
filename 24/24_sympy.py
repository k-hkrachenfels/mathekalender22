from sympy import tan, asin, sqrt, simplify, pi 

r= ( 0.5 * tan( (pi/2 - asin(0.5/sqrt(1.25)))/2))
s = simplify(r**2/0.25+r/0.5)

print(s)

