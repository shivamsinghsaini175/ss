import os.path
import sys

fname=input("file name")
if not os.path.isfile(fname):
    print(" not found")
    sys.exit(0)
inline=open(fname,'r')
n=int(input("enter lines"))
lineList=inline.readlines()
for i in range(n):
    print(i+1,lineList[i])
    i+=1
cnt=0
w=input(" enter w")
for line in lineList:
    cnt+=line.count(w)
print (cnt)