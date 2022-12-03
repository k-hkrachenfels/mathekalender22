p=1.
for i in range(1,12):
    print(f"{i},{i+1}")
    p = p*i/(i+1)

print(p)
print(1/12.)


fertig=0
for i in range(1,13):
    print(i)
    fertig += 1/i

print(fertig)

