import tkinter as tk
import csv

def getinput():
    txt = str(inputtxt.get(1.0, "end-1c"))
    #print(txt)
    info = lookup(txt, 'PriceList.csv')
    productinfo.config(state='normal')
    productinfo.insert(tk.END, info)
    productinfo.config(state='disable')

def lookup(item, productfile):
    with open(productfile, 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] == item:
                print(row)
                return str(row)+'\n'


root=tk.Tk()

root.title('Garmin Product Lookup')
root.geometry('1280x720')

label = tk.Label(root, text='Enter Product ID:')
label.pack()

inputtxt = tk.Text(root, height = 1, width = 30) 
inputtxt.pack() 

submit = tk.Button(root, text='submit', command=getinput) 
submit.pack()

productinfo=tk.Text(root, height = 30, width = 200, font=('Helvetica',8))
productinfo.pack()
productinfo.config(state=tk.DISABLED)

root.mainloop()