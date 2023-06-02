m1=[[1,2,3],[3,5,8],[5,6,9]]
m2=[[7,2,3],[5,2,7],[8,9,1]]
m3=[[0,0,0],[0,0,0],[0,0,0]]
m1len=len(m1)
m2len=len(m2)
for i in range(m1len):
  for j in range(m2len):
    m3[i][j]=m1[i][j]*m2[i][j]
print(m3)
