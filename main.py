import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

def add():
    total = 0.0

    for child in productinfo.get_children():
        total += float(productinfo.item(child, 'values')[2])
    return total

def getinput():
    txt = str(inputtxt.get(1.0, "end-1c"))
    info = lookup(txt, 'PriceList.csv')
    try:
        productinfo.insert(parent='',index=tk.END, values=info[0:3])
    except:
        if txt == '':
            messagebox.showerror('Invalid Input', 'Please enter a product ID')
        else:
            messagebox.showerror('Invalid Input', 'Entered Product ID number could not be found')
    inputtxt.delete(1.0, tk.END)
    pricesum=str(add())
    price.config(text='Total: £'+pricesum)
    

def lookup(item, productfile):
    with open(productfile, 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] == item:
                return row


root=tk.Tk()

root.title('Garmin Product Lookup')
root.geometry('800x720')

label = tk.Label(root, text='Enter Product ID:')
label.pack()

inputtxt = tk.Text(root, height = 1, width = 30, wrap = 'none') 
inputtxt.bind('<Return>', 'break')
inputtxt.bind('<KeyRelease-Return>', 'break')
inputtxt.pack() 

submit = tk.Button(root, text='submit', command=getinput) 
submit.pack()

productinfo=ttk.Treeview(root, columns=('id', 'description', 'rrp'), show='headings', height=20)
productinfo.column('id', width=100)
productinfo.column('description', width =600)
productinfo.column('rrp', width=75, anchor=tk.E)
productinfo.heading('id', text='Item No')
productinfo.heading('description', text='Product Description')
productinfo.heading('rrp', text='RRP')
productinfo.pack()

price = tk.Label(root, text='Total: £0.0')
price.pack()

root.mainloop()