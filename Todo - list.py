# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:46:41 2025

@author: Ngoc anh
"""

import tkinter as tk
from tkinter import PhotoImage, Label, Frame, StringVar, Entry, Button, Listbox, Scrollbar
from tkinter import *

root = tk.Tk()  
root.title("To-do-list App")
root.geometry("500x800+400+100")
root.resizable(False, False)

task_list = []
def addTask():
    task = task_entry.get()
    task_entry.delete(0, tk.END)
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert( tk.END, task)
def deleteTask():
    global task_list
    task = str(listbox.get(tk.ANCHOR).strip())
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for t in task_list:
                taskfile.write(t+ "\n")
        listbox.delete(tk.ANCHOR)
    
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            task = task.strip()
            if task:
                task_list.append(task)
                listbox.insert(tk.END ,task)
    except:
        file=open('tasklist.txt', 'w')
        file.close()
        
            
    

image_path = r"C:\Users\Ngoc anh\Downloads\todo.png"
try:
    Image_icon = PhotoImage(file=image_path)  
    root.iconphoto(False, Image_icon)  
    print("Icon loaded successfully!")
    
except tk.TclError:
    print("Error!")
TopImage_path = r"C:\Users\Ngoc anh\Downloads\topbar1.png"
try:
    TopImage = tk.PhotoImage(file=TopImage_path)  
    label = tk.Label(root, image=TopImage)
    label.image = TopImage 
    label.pack()
    print("Top image loaded successfully!")
except Exception as e:
    print("Error loading top image:", e)
heading = Label(root, text ="To-do List", font ="arial 15 bold", fg ="white", bg ="#32405b")
heading.place(x = 130, y= 20)

#main
frame = Frame(root, width = 400, height = 50, bg="white" )
frame.place(x=0, y=100)
task= StringVar()
task_entry = Entry(frame, width = 18, font = "arial 20",bd =0)
task_entry.place(x=10,y=7)
task_entry.focus()
button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff",fg ="white",bd=0, command= addTask)
button.place(x=300,y=0)

#list
frame1 = Frame(root, bd=3,width=700, height=280, bg ="#32405b")
frame1.pack(pady=(160,0))
listbox = Listbox(frame1, font =('arial',12), width=40,height=16,bg="#32405b", fg="white",cursor ="hand2", selectbackground="#5a95ff")
listbox.pack(side=tk.LEFT , fill=tk.BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side= tk.RIGHT ,fill= tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
openTaskFile()

#delete
Delete_icon=PhotoImage(file=r"C:\Users\Ngoc anh\Downloads\delete.png")
Button(root, image=Delete_icon,bd=0, command = deleteTask).pack(side = tk.BOTTOM, pady=12)


    


root.mainloop()
