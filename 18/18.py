

def generate(x):
    if x%2 == 1:
        return (3*n +1)//2
    else:
        return n//2

n = 2**30-1
for i in range(30):
    n = generate(n)
    print(n)