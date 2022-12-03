
def solution(a,b,c,d):
    archy = 3*a+b+d
    if archy!=125:
        return False
    bowy = 2*b+c+2*d
    if bowy!=230:
        return False
    curvy= a+b+2*c+d
    if curvy!=185:
        return False
    return True
    

solutions=0
max_points=105
for a in range(5,max_points,5):
    for b in range(a+5,max_points,5):
        for c in range(b+5,max_points,5):
            for d in range (c+5,max_points,5):
                if solution(a,b,c,d):
                    print(f"a={a}, b={b}, c={c}, d={d}")
                    solutions+=1

print(f"Es gibt {solutions} Möglichkeiten")

