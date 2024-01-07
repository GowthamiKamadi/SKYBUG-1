#TASK 2:- TO-DO-LIST
#importing tkinter module to develop GUI
import tkinter
#importing photoimage to add bg image
from tkinter import PhotoImage
import random
#create root window
root = tkinter.Tk()
#change root window size
root.geometry("350x400")
#adding background image
my_image=PhotoImage(file ="C:\\Users\\HP\\OneDrive\\Desktop\\internship\\music.png")
bg_image=tkinter.Label(root, image=my_image)
bg_image.place(relheight=1, relwidth=1)
root.configure(bg="black")
root.title("skybug technologies")
#create an empty list
tasks=[]

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")
#creating functions

def add_task():
    #get the task from user to add
    task = txt_input.get()
    tasks.append(task)
    update_listbox()
    txt_input.delete(0,"end")

def del_all():
    #clear the tasks list
    #since we are changing the list it needs to be global
    global tasks
    tasks=[]
    #update listbox
    update_listbox()

def del_one():

    task=lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)

        update_listbox()
lbl_title = tkinter.Label(root, text="To-do-list",foreground="white", font="algerian,40",bg="black", width=30)
lbl_title.pack()

lbl_display = tkinter.Label(root, text=" ",foreground="white", bg="black",width=30)
lbl_display.pack()

txt_input=tkinter.Entry(root,width=40)
txt_input.pack()

lbl_display = tkinter.Label(root, text=" ",foreground="white",font="algerian", bg="black",width=20)
lbl_display.pack()

btn_add_task=tkinter.Button(root, text="add task",fg="yellow",font="algerian", bg="black",width=20, command=add_task)
btn_add_task.pack()

btn_del_all=tkinter.Button(root, text="Delete all",fg="yellow", font="algerian",bg="black",width=20, command=del_all)
btn_del_all.pack()

btn_del_one=tkinter.Button(root, text="delete",fg="yellow",font="algerian", bg="black",width=20, command=del_one)
btn_del_one.pack()

btn_exit=tkinter.Button(root, text="exit",fg="yellow", bg="black",font="algerian", width=20,command=exit)
btn_exit.pack()

lbl_display = tkinter.Label(root, text=" ",foreground="white", bg="black",width=33)
lbl_display.pack()

lb_tasks= tkinter.Listbox(root,width=40,height=20)
lb_tasks.pack()

root.mainloop()