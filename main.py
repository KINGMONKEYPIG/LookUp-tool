import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import csv

def add():
    total = 0.0

    for child in productinfo.get_children():
        total += float(productinfo.item(child, 'values')[2])
    return "{:.2f}".format(total)

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
            
def update(data):
    searchbox.delete(0, 'end')
    for items in data:
        searchbox.insert('end', items)

def select(event):
    inputtxt.delete(0.0, 'end')
    inputtxt.insert(0.0, searchbox.get(ACTIVE))

def check(event):
    searchbox.place(x=250, y=50)
    if inputtxt.get(1.0, 'end-1c') =='':
        searchbox.place_forget()
    searchbox.lift()

    typed = str(inputtxt.get(1.0, 'end-1c'))
    if typed == '' :
        data = []
    else:
        data=[]
        for item in contents:
            if typed in str(item):
                data.append(item)
    update(data)

def gettable(event=None):
    searchbox.place_forget()
    data = productinfo.selection()
    values = productinfo.item(data, 'values')
    return values[0]

def deleteitem():
    data=gettable()
    for child in productinfo.get_children():
        if productinfo.item(child, 'values')[0] == data:
            productinfo.delete(child)
    pricesum = str(add())
    price.config(text='Total: £' + pricesum)
    
        
    

root=tk.Tk()

root.title('Garmin Product Lookup')
root.geometry('800x720')
root.resizable(False,False)

label = tk.Label(root, text='Enter Product ID:')
label.pack()

inputtxt = tk.Text(root, height = 1, width = 30, wrap = 'none') 
inputtxt.bind('<Return>', 'break')
inputtxt.bind('<KeyRelease-Return>', 'break')
inputtxt.bind('<KeyRelease>', check)
inputtxt.pack(pady=10) 

searchbox = tk.Listbox(root, width=50)

submit = tk.Button(root, text='submit', command=getinput) 
submit.place(x=inputtxt.winfo_x()+540, y=inputtxt.winfo_y()+30)

remove = tk.Button(root, text='delete', command = deleteitem)
remove.place(x=40, y=30)

productinfo=ttk.Treeview(root, columns=('id', 'description', 'rrp'), show='headings', height=20)
productinfo.column('id', width=100)
productinfo.column('description', width =600)
productinfo.column('rrp', width=75, anchor=tk.E)
productinfo.heading('id', text='Item No')
productinfo.heading('description', text='Product Description')
productinfo.heading('rrp', text='RRP')
productinfo.bind('<ButtonRelease-1>', gettable)
productinfo.pack()

price = tk.Label(root, text='Total: £0.0')
price.pack()


contents=[]
with open('PriceList.csv', 'r', encoding='utf-8') as file:
        data = csv.reader(file)
        for item in data:
            contents.append(item[0])
contents.remove(contents[0])
update(contents)

searchbox.bind('<<ListboxSelect>>', select)

root.mainloop()