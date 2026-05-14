import streamlit as st
from pathlib import Path
import os

def readfileandfolder():
    p = Path('')
    items = list(p.rglob('*'))
    return items

def createfile(file_name, content):
    p = Path(file_name)
    if p.exists():
        return "File already exists"
    else:
        with open(file_name, 'w') as file:
            file.write(content)
        return "File created successfully!"

def readfile(filename):
    p = Path(filename)
    if p.exists():
        with open(filename, 'r') as file:
            return file.read()
    else:
        return "File not found"

def updatefile(filename, content, mode):
    p = Path(filename)
    if p.exists():
        with open(filename, mode) as file:
            file.write(content)
        return "File updated successfully!"
    else:
        return "File does not exist"

def deletefile(filename):
    p = Path(filename)
    if p.exists():
        os.remove(p)
        return "File deleted"
    else:
        return "File does not exist"

def renamefile(filename, new_name):
    p = Path(filename)
    if p.exists():
        p.rename(new_name)
        return "File renamed"
    else:
        return "File does not exist"

def createfolder(foldername):
    p = Path(foldername)
    if p.exists():
        return "Folder already exists"
    else:
        p.mkdir()
        return "Folder created"

def deletefolder(foldername):
    p = Path(foldername)
    if p.exists():
        p.rmdir()
        return "Folder deleted"
    else:
        return "Folder does not exist"


# Streamlit UI
st.title("📂 File Manager")

menu = st.sidebar.selectbox("Choose Action", 
    ["List Files", "Create File", "Read File", "Update File", "Delete File", "Rename File", "Create Folder", "Delete Folder"])

if menu == "List Files":
    st.write("### Files and Folders")
    for i, item in enumerate(readfileandfolder(), 1):
        st.write(f"{i} - {item}")

elif menu == "Create File":
    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter content")
    if st.button("Create"):
        st.success(createfile(file_name, content))

elif menu == "Read File":
    filename = st.text_input("Enter file name")
    if st.button("Read"):
        st.write(readfile(filename))

elif menu == "Update File":
    filename = st.text_input("Enter file name")
    content = st.text_area("Enter new content")
    mode = st.radio("Choose mode", ["Overwrite (w)", "Append (a)"])
    if st.button("Update"):
        st.success(updatefile(filename, content, 'w' if mode.startswith("Overwrite") else 'a'))

elif menu == "Delete File":
    filename = st.text_input("Enter file name")
    if st.button("Delete"):
        st.warning(deletefile(filename))

elif menu == "Rename File":
    filename = st.text_input("Enter file name")
    new_name = st.text_input("Enter new name")
    if st.button("Rename"):
        st.success(renamefile(filename, new_name))

elif menu == "Create Folder":
    foldername = st.text_input("Enter folder name")
    if st.button("Create"):
        st.success(createfolder(foldername))

elif menu == "Delete Folder":
    foldername = st.text_input("Enter folder name")
    if st.button("Delete"):
        st.warning(deletefolder(foldername))
