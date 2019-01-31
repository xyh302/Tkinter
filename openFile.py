import sys
import os
path = os.getcwd()
print(path+"\\number.txt")
print(sys.argv[0])

path

name =['a1','a2','a3']
with open(path+"\\number.txt", "a+") as f:
    for i in name:
        f.write(i)
        f.write("\r\n")
