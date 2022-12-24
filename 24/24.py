import math

# Berechnung des Innenkreises r_k
d = math.sqrt(1.25)
print(d)
beta = math.asin(0.5/d)
print(beta)
alpha = (math.pi/2-beta)/2
print(alpha)
r_k = 0.5 * math.tan(alpha)
print(r_k)

# Fläche Innenkreis A_k und Aussenkreis A_g
A_k = math.pi * r_k**2

print(A_k)
A_g = math.pi * 0.25
print(A_g)

# Aussenkreiskradius
r_g = 0.5

solution = A_k/A_g + r_k/r_g
print(solution)

