#1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(int(input("enter a number:")))
print(f'result:{result}')

#2
def sum_of_positive_integers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_positive_integers(n - 1)
    
res= sum_of_positive_integers(int(input("enter a number:")))
print(f'result:{result}')


#3

def fibonacci(n, a=0, b=1, count=0):
    if count == n:
        return
    print(a, end=" ")
    next_term = a + b
    fibonacci(n, b, next_term, count + 1)

N =int(input("enter the number:"))  # Change N to the number of terms you want to display
fibonacci(N)
