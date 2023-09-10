import os
import pathlib
import zipfile
import sys
dirname=input()
if not os.path.isdir(dirname):
    print("doestt esxist")
    sys.exit(0)
curdirectory=pathlib.Path(dirname)
n=1
while True:
    zipFilename=os.path.basename(curdirectory)+'_'+str(n)+".zip"
    if  not os.path.exists(zipFilename):
        break
    n+=1
print(f'creating zip{zipFilename}.....')
with zipfile.ZipFile(zipFilename, mode="w") as archieve:
    for path_list in curdirectory.rglob("*"):
        archieve.write(path_list,archieve=path_list.realative_to(curdirectory))
if os.path.isfile(zipFilename):
    print(" zip file created succesfully "+zipFilename)
else:
    print(" error in creating zip")
