#matrix
a=int(input("enter no of rows:"))
b=int(input("enter no of columns:"))
c=int(input("enter no of rows in 2nd matrix:"))
d=int(input("enter no of columns in 2nd matrix:"))
mat1=[]
mat2 = []

for i in range(a):
    mat1.append([ ]) 
    for j in range(b):
        mat1[i].append(int(input("enter matrix elements")))
for i in range(c):
    mat2.append([ ])
    for j in range(d):
        mat2[i].append(int(input("enter matrix elements")))
print(f'the matrix is {mat1}')
print(f'the matrix is {mat2}')
#addition of matrix with another matrix
for i in range(len(mat1)):   

    for j in range(len(mat2[0])):
        mat3 = mat1[i][j] + mat2[i][j]
print(f'the matrix addition is {mat3}')
#multiplication of matrix with another matrix
for i in range(len(mat1)):
   # iterate through columns of Y
   for j in range(len(mat2[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           mat4=mat4+mat1[i][k] * mat2[k][j]
print(f'the multiplication of the matrices is {mat4}')

