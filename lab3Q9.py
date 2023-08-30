bsal=int(input("enter salary:"))
hra=0.2*bsal
ta=0.05*bsal
da=0.1*bsal
gs=bsal+hra+ta+da
print("Gtoss Salary is:",gs)

if gs<300000:
    print("No Income Tax")
if gs>=300000 and gs<1000000:
    inctx=0.1*gs
    print(inctx)
if gs>=1000000 and gs<2500000:
    inctx=0.2*gs
    print(inctx)
if gs>=2500000:
    inctx=0.3*gs
    print(inctx)