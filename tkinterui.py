import tkinter as tk
from tkinter import messagebox, simpledialog
from pathlib import Path
import os

def readfileandfolder():
    p = Path('')
    return list(p.rglob('*'))

def createfile():
    file_name = simpledialog.askstring("Input", "Enter file name:")
    content = simpledialog.askstring("Input", "Enter content:")
    p = Path(file_name)
    if p.exists():
        messagebox.showinfo("Info", "File already exists")
    else:
        with open(file_name, 'w') as file:
            file.write(content)
        messagebox.showinfo("Info", "File created successfully!")

def readfile():
    filename = simpledialog.askstring("Input", "Enter file name:")
    p = Path(filename)
    if p.exists():
        with open(filename, 'r') as file:
            messagebox.showinfo("File Content", file.read())
    else:
        messagebox.showerror("Error", "File not found")

def updatefile():
    filename = simpledialog.askstring("Input", "Enter file name:")
    p = Path(filename)
    if p.exists():
        option = simpledialog.askinteger("Input", "Press 1 for overwrite, 2 for append")
        content = simpledialog.askstring("Input", "Enter content:")
        mode = 'w' if option == 1 else 'a'
        with open(filename, mode) as file:
            file.write(content)
        messagebox.showinfo("Info", "File updated successfully!")
    else:
        messagebox.showerror("Error", "File does not exist")

def deletefile():
    filename = simpledialog.askstring("Input", "Enter file name:")
    p = Path(filename)
    if p.exists():
        os.remove(p)
        messagebox.showinfo("Info", "File deleted")
    else:
        messagebox.showerror("Error", "File does not exist")

def renamefile():
    filename = simpledialog.askstring("Input", "Enter file name:")
    new_name = simpledialog.askstring("Input", "Enter new name:")
    p = Path(filename)
    if p.exists():
        p.rename(new_name)
        messagebox.showinfo("Info", "File renamed")
    else:
        messagebox.showerror("Error", "File does not exist")

def createfolder():
    foldername = simpledialog.askstring("Input", "Enter folder name:")
    p = Path(foldername)
    if p.exists():
        messagebox.showinfo("Info", "Folder already exists")
    else:
        p.mkdir()
        messagebox.showinfo("Info", "Folder created")

def deletefolder():
    foldername = simpledialog.askstring("Input", "Enter folder name:")
    p = Path(foldername)
    if p.exists():
        p.rmdir()
        messagebox.showinfo("Info", "Folder deleted")
    else:
        messagebox.showerror("Error", "Folder does not exist")

# Tkinter UI
root = tk.Tk()
root.title("📂 File Manager")

tk.Button(root, text="Create File", command=createfile).pack(pady=5)
tk.Button(root, text="Read File", command=readfile).pack(pady=5)
tk.Button(root, text="Update File", command=updatefile).pack(pady=5)
tk.Button(root, text="Delete File", command=deletefile).pack(pady=5)
tk.Button(root, text="Rename File", command=renamefile).pack(pady=5)
tk.Button(root, text="Create Folder", command=createfolder).pack(pady=5)
tk.Button(root, text="Delete Folder", command=deletefolder).pack(pady=5)

root.mainloop()
