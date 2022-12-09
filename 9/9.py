
from util.constant_set import ConstantSet
from collections import defaultdict

class Child(ConstantSet):
    NASTI="Nasti"
    JONA="Jona"
    MANU="Manu"
    ULI="Uli"

strategies = {  Child.NASTI: [(24,20),(16,10),(6,8),(4,5),(2,4)],
                Child.JONA: [(2,4),(6,8),(4,5),(24,20),(16,10)],
                Child.MANU:  [(2,4),(4,5),(6,8),(16,10),(24,20)],
                Child.ULI:   [(24,20),(6,8),(4,5),(2,4),(16,10)] }


# 2. Die gesamte Freude von Nastis Geschenken ist immer mindestens so groß wie die von Manu.
n_ge_m = True

# 3. Die gesamte Freude von Nastis Geschenken ist immer mindestens so groß wie die von Uli.
n_ge_u = True

# 4. Die gesamte Freude von Manus Geschenken ist immer mindestens so groß wie die von Jona.
m_ge_j = True

# 5. Die gesamte Freude von Manus Geschenken ist immer mindestens so groß wie die von Uli.
m_ge_u = True

# 6. Die gesamte Freude von Jonas Geschenken ist immer mindestens so groß wie die von Nasti.
j_ge_n = True

# 7. Die gesamte Freude von Jonas Geschenken ist immer mindestens so groß wie die von Manu.
j_ge_m = True

# 8. Die gesamte Freude von Ulis Geschenken ist immer mindestens so groß wie die von Nasti.
u_ge_n = True

# 9. Die gesamte Freude von Ulis Geschenken ist immer mindestens so groß wie die von Jona.
u_ge_j = True

for size in range(100):
    result_joy = defaultdict(int)
    result_size = defaultdict(int)
    #print(f"size=",size)
    for child in strategies:
        strategy = strategies[child]
        for s,j in strategy:
            if result_size[child]+s > size:
                continue
            result_size[child]+=s
            result_joy[child]+=j
        #print(f"size={size}, child={child}, joy={result_joy[child]}, actual_size={result_size[child]}")
        
            
    # 2. Die gesamte Freude von Nastis Geschenken ist immer mindestens so groß wie die von Manu.
    print(f"size={size}, j={result_joy[Child.JONA]}, m={result_joy[Child.MANU]}")
    
    if result_joy[Child.NASTI] < result_joy[Child.MANU]:
        n_ge_m = False
    

    # 3. Die gesamte Freude von Nastis Geschenken ist immer mindestens so groß wie die von Uli.
    
    if result_joy[Child.NASTI] < result_joy[Child.ULI]:
        n_ge_u = False

    # 4. Die gesamte Freude von Manus Geschenken ist immer mindestens so groß wie die von Jona.
    if result_joy[Child.MANU] < result_joy[Child.JONA]:
        m_ge_j = False

    # 5. Die gesamte Freude von Manus Geschenken ist immer mindestens so groß wie die von Uli.
    if result_joy[Child.MANU] < result_joy[Child.ULI]:
        m_ge_u = False

    # 6. Die gesamte Freude von Jonas Geschenken ist immer mindestens so groß wie die von Nasti.
    if result_joy[Child.JONA] < result_joy[Child.NASTI]:
        j_ge_n = False

    # 7. Die gesamte Freude von Jonas Geschenken ist immer mindestens so groß wie die von Manu.
    if result_joy[Child.JONA] < result_joy[Child.MANU]:
        j_ge_m = False

    # 8. Die gesamte Freude von Ulis Geschenken ist immer mindestens so groß wie die von Nasti.
    if result_joy[Child.ULI] < result_joy[Child.NASTI]:
        u_ge_n = False

    # 9. Die gesamte Freude von Ulis Geschenken ist immer mindestens so groß wie die von Jona.
    if result_joy[Child.ULI] < result_joy[Child.JONA]:
        u_ge_j = False



# 2. Die gesamte Freude von Nastis Geschenken ist immer mindestens so groß wie die von Manu.
if n_ge_m:
    print("2")

# 3. Die gesamte Freude von Nastis Geschenken ist immer mindestens so groß wie die von Uli.
if n_ge_u:
    print("3")

# 4. Die gesamte Freude von Manus Geschenken ist immer mindestens so groß wie die von Jona.
if m_ge_j:
    print("4")

# 5. Die gesamte Freude von Manus Geschenken ist immer mindestens so groß wie die von Uli.
if m_ge_u:
    print("5")

# 6. Die gesamte Freude von Jonas Geschenken ist immer mindestens so groß wie die von Nasti.
if j_ge_n:
    print("6")

# 7. Die gesamte Freude von Jonas Geschenken ist immer mindestens so groß wie die von Manu.
if j_ge_m:
    print("7")

# 8. Die gesamte Freude von Ulis Geschenken ist immer mindestens so groß wie die von Nasti.
if u_ge_n:
    print("8")

# 9. Die gesamte Freude von Ulis Geschenken ist immer mindestens so groß wie die von Jona.
if u_ge_j:
    print("9")
 

