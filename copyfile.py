f1=open("fir.txt","r")
content=""
for i in f1:
  content=content+i
f1.close()
f2=open("cpyfile.txt","w")
f2.write(content)
f2.close()
f2=open("cpyfile.txt","r")
print(f2.read())
