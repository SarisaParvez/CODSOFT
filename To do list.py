import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        del self.tasks[index]

    def update_task(self, index, new_task):
        self.tasks[index] = new_task

    def view_tasks(self):
        return self.tasks

def add_task():
    task = task_entry.get()
    if task:
        todo_list.add_task(task)
        update_task_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        todo_list.delete_task(index)
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        todo_list.update_task(index, new_task)
        update_task_listbox()
        task_entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    tasks = todo_list.view_tasks()
    for task in tasks:
        task_listbox.insert(tk.END, task)

todo_list = TodoList()

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")

# Background color
root.configure(bg='#FFA07A')  # Light Salmon color

# Frame for task entry and buttons
frame = tk.Frame(root, bg='#FFA07A')  # Same color as root
frame.pack(pady=20)

# Entry for task
task_entry = tk.Entry(frame, width=30)
task_entry.grid(row=0, column=0, padx=5)

# Buttons
add_button = tk.Button(frame, text="Add Task", command=add_task, bg='#90EE90')  # Light Green color
add_button.grid(row=0, column=1, padx=5)
delete_button = tk.Button(frame, text="Delete Task", command=delete_task, bg='#FF6347')  # Tomato color
delete_button.grid(row=1, column=0, padx=5, pady=5)
update_button = tk.Button(frame, text="Update Task", command=update_task, bg='#87CEEB')  # Sky Blue color
update_button.grid(row=1, column=1, padx=5, pady=5)

# Frame for task listbox
list_frame = tk.Frame(root, bg='#FFA07A')  # Same color as root
list_frame.pack(padx=20, pady=(0, 20), fill=tk.BOTH, expand=True)

# Listbox to display tasks
task_listbox = tk.Listbox(list_frame, width=50)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for task listbox
scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
