N=int(input("enter a number: "))
 
hline=" +/" + "\/" *(N-2) + "+"
vline=" |" +   " "*(N-2) +   "|"
for i in range(N):
    if i==0 or i==N-1:
        print(hline)
    else:
        print(vline)