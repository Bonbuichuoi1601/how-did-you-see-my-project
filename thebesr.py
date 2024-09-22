sophantu=5
a=[]
for i in range (0,sophantu):
    a.append (int(input(f"Phan tu thu {i}:")))
chuaam = 0
enumeratecuaa=enumerate(a)
for b in a:
    chuaam=b
    if chuaam<0:
        print()
