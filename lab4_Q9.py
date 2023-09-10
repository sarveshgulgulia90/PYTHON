#taking input
X=input("enter a sentence")
#initialization
upp=0
lower=0
dig=0
spec=0
ind=0
##looping
while ind<len(X):
    char=X[ind]
    #conditions
    if 'A'<=char<='Z':
        upp+=1
    elif 'a'<=char<='z':
        lower+=1
    elif '0'<=char<='9':
        dig+=1
    else:
        spec+=1 
    ind+=1   
#output      
print(upp)
print(lower) 
print(dig)
print(spec)