from collections import defaultdict

def print_probs(probs_per_range):
    meters = sorted(probs_per_range.keys())
    probs = [probs_per_range[meter] for meter in meters]
    for meter,prob in  zip(meters,probs):
        print(f"{meter:2.2f},{prob:2.2f}",end=", ")
    print("")

probs = defaultdict(int)
probs[-500]=1
for _ in range(10):
    new_probs = defaultdict(int)
    for i in probs:
        if i<0:
            new_probs[i+100]+=probs[i]*0.8
            new_probs[i-200]+=probs[i]*0.2
        if i>=0:
            new_probs[i]+=probs[i]
    probs=new_probs
    print_probs(probs)


        
