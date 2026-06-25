# file handling project
from pathlib import Path
import os
def readfileandfolder():
 P=Path("")
 items=list(P.rglob("*"))
 for i,items in enumerate (items):
  print(f"{i+1} : {items}")
 
def creatfile():
 try:
  readfileandfolder()
  name=input("plese tell your file name : ")
  p=Path(name)
  if not  p.exists():
   
   with open(p,"w") as fs:
    data=input("what are you want to write  in this file")
    fs.write(data)
   print(f"file create successfully")
  else:

   print("this file already exist")
 except Exception as err:
  print(f"an error occured as {err}")
def readfile():
  try:
    readfileandfolder()
    name=input("which file you want to read : ")
    p=Path(name)
    if p.exists() and p.is_file():
      with open(p,"r") as fs:
        data=fs.read()
        print(data)
      print("READED SUCCESSFULY")
    else:
      print("the file does not exist")
  except Exception as err:
    print(f"an error occured as {err}")

def updatefile():
  try:
     readfileandfolder()
     name=input("tell which you want to update : ")
     p=Path(name)
     if p.exists() and p.is_file():
       print("press 1 for  changing the name of your file:_")
       print("press 2 for overwrting tha data of your file : ")
       print("press 3 for appending some content in your file : ")
       res= int(input("tell your respose :-"))
       if res==1:
        name2= input("tell your new file name :-")
        p2=Path(name2)
        p.rename(p2)
       if res==2:
        with open(p,"w") as fs:
         data= input("tell what you want to write this overwrite  the data : ")
         fs.write(data)
       if res==3:
          with open(p,"a") as fs:
            data= input("tell what you want to append  the data : ")
            fs.write(" "+data)
  except Exception as err:
   print(f"an error occured as {err}")
def deletefile():
  try:
    readfileandfolder()
    name= input("which file you want to delete : ")
    p=Path(name)
    if p.exists() and p.is_file():
      os.remove(name)
  
      print("file  remove successfully" )
    else:
      print("no such file exicst")
  except Exception as err:
    print(f" an errror occured as {err}")

 

  
  print("press 1 for creating a file")
  print("press 2 for reading a file")
  print("press 3 for updating a file")
  print("press 4 for deletion a file")

check= int(input("please tell your response:- "))
if check==1:
 creatfile()
if check==2:
 readfile()

if check==3:
 updatefile()

if check==4:
  deletefile()
 
