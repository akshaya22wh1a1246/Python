m1=[[2,6,8],
    [5,9,2],
    [9,10,17]]
m2=[[3,8,10],
    [5,8,2],
    [4,12,7]]
m3=[[0,0,0],
    [0,0,0],
    [0,0,0]]
m1len=len(m1)
m2len=len(m2)
m3len=len(m3)
for i in range(m1len):
  for j in range(m2len):
    m3[i][j]=m1[i][j]+m2[i][j]
print(m3)
    
