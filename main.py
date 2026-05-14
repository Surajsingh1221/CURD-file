# project - CRUD operstions
from pathlib import Path
import os 
def readfileandfolder():
    p = Path('')
    items = list(p.rglob('*'))
    for index, file in enumerate(items):
        print(f"{index+1} - {file}")

def createfile():
    try:
     readfileandfolder()
     file_name = input("enter your file name:")
     p = Path(file_name)
     if p.exists():
         print("file is already exists")
     else:
         with open(file_name,'w')as file:
             content = input("enter your content:")
             file.write(content)
             print('FILE ADDED!')
    except Exception as e:
       print(e)         


def readfile():
    try:
     readfileandfolder()
     filename  = input("enter file name:")
     p = Path(filename)
     if p.exists():
        with open(filename,'r') as file:
            print(file.read())
     else:
        print('FILE NOT FOUND')
    except Exception as e:
        print(e)


def updatefile():
    try:
      readfileandfolder()
      filename  = input("enter file name:")
      p = Path(filename)
      if p.exists():
        print('press 1 for overwrite')
        print('press 2 for append new content')
        option = int(input("press number"))
        if option == 1:
           with open (filename,'w') as file :
              content = input("enter your content")
              file.write(content)
              print("content changed")
        
        elif option == 2:
             with open (filename,'a') as file :
              content = input("enter your content")
              file.write(content)
              print("content changed")
        
        else:
           print("INVALID INPUT")

      else:
         print("FILE DOES NOT EXIST")
   
    except Exception as e:
       print(e)
    

def deletefile():
   
      readfileandfolder()
      filename = input("enter file name")
      p = Path(filename)
      if p.exists():
         os.remove(p)
         print('file deleted')
      else:
         print("FILE DOES NOT EXIST")


def rename ():
      readfileandfolder()
      filename = input("enter file name")
      p = Path(filename)
      if p.exists():
         new_file = input("enter new name of file")
         p.rename(new_file)
         print('FILE RENAMED')
      else:
         print('file doew not exist')
      
def createfolder():
   readfileandfolder()
   foldername = input('enter name of folder:')
   p = Path(foldername)
   if p.exists():
      print('FOLDER ALREADY EXIST')
   else:
      p.mkdir()
      print('FOLDER CREATED')

def deletefolder():
    readfileandfolder()
    foldername = input('enter name of folder:')
    p = Path(foldername)
    if p.exists():
       p.rmdir()
       print('FOLDER DELETED')
    else:
       print('FOLDER NOT EXISTS')

def create_file_in_folder():
   foldername = input('enter folder name:')
   file_name = input(' enter file name')
   p = Path(foldername/file_name)
   if p.exists():
      print('file already exist')
   else:
      pass





while True:
  
  print('press 1 for creating a file')
  print('press 2 for reading a file')
  print('press 3 for updating a file')
  print('press 4 for deleting a file')
  print('press 5 for rename file')
  print('press 6 for creating a folder')
  print('press 7 for deleting a folder')
  print('press 0 for exiting')

  option = int(input(" Enter your choice: "))
  if option == 1:
        createfile()

  if option == 2:
     readfile()

  if option == 3:
    updatefile()

  if option == 4:
    deletefile()

  if option == 5:
     rename()

  if option == 6:
     createfolder()

  if option == 7:
     deletefolder()

  if option == 0 :
    break