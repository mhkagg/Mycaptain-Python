n1=0
n2=1
terms=0
nterms= int(input("enter numbers: "))
if nterms <= 0:
    print("error")
elif nterms == 1:
    print(n1)
else:
    print("CONTINUE")
    while nterms > terms:
        print(n1)
        nth= n1+n2
        n1=n2
        n2=nth
        terms += 1 
