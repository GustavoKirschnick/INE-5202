A = [[4,2,3], [2,-4,-1], [-1,1,4]]
B = [7,1,-5]
x = [0 for i in B]
n = len(B)


for k in range(n-1):
  for i in range(k+1,n):
    mult = (A[i][k]/A[k][k])
    B[i]=B[i]-(mult)*B[k]
    for j in range(k,n):
      A[i][j] = A[i][j]-(mult)*(A[k][j])

x[n-1]=(B[(n-1)]/A[(n-1)][(n-1)])

for l in range(n,1,-1):
    soma = 0
    for m in range (l-1,n):
     soma = soma + A[l-2][m]*x[m]  
    x[l-2]=((B[l-2]-soma)/A[l-2][l-2])
    
print(x)
