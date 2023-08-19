import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    try:
        listbox.delete(listbox.curselection())
    except:
        messagebox.showerror("Chyba", "Vyberte úkol k odstranění.")

# Vytvoření hlavního okna
root = tk.Tk()
root.title("TODO List")
root.configure(bg='#90EE90') 

# Vytvoření widgetů
listbox = tk.Listbox(root, width=50, height=20, bg='#FFFAF0', fg='#000')  
entry = tk.Entry(root, width=50, bg='#ADD8E6')  
add_button = tk.Button(root, text="Přidat úkol", command=add_task, bg='#ff0')  
remove_button = tk.Button(root, text="Odstranit úkol", command=remove_task, bg='#FF6347')  

# Rozmístění widgetů
listbox.pack(pady=20, padx=20)
entry.pack(pady=10, padx=20)
add_button.pack(pady=10, padx=20)
remove_button.pack(pady=10, padx=20)

root.mainloop()
