#taking input
epsil=int(input("enter the value of epsilon error: "))
x=int(input("Enter the value of x:  "))
#initializing and declaring variables and expressions
sum = 1
term = 1
fct = 1
p = 1
multi = 1
#looping till n-1
for i in range(1, epsil):
    fct = fct * multi * (multi+1)
    p = p*x*x
    term = (-1) * term
    multi += 2
    sum = (sum + (term * p)/fct)
print(f'The sum is:{sum}')
