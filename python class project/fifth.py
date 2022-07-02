import os
import shutil
source=input("enter the source file")
destination=input("eter the destination file")
source=source+'/'
destination=destination+'/'
listoffiles=os.listdir(source)
for i in listoffiles:
    shutil.copy((source+i),destination)