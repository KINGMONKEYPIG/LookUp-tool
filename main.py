import tkinter as tk

def getinput():
    #try:
        txt = int(inputtxt.get(1.0, "end-1c"))
        print(txt)
        info = lookup(id, 'products.txt')
        productinfo.config(text=info)
    #except:
     #   print('enter valid integer ID')

def lookup(item, productfile):
    file = open(productfile)
    text = file.read()
    return text

root=tk.Tk()

root.title('Garmin Product Lookup')
root.geometry('300x400')

label = tk.Label(root, text='Enter Product ID:')
label.pack()

inputtxt = tk.Text(root, height = 1, width = 30) 
inputtxt.pack() 

submit = tk.Button(root, text='submit', command=getinput) 
submit.pack()

productinfo=tk.Label(root, text='')
productinfo.pack()

root.mainloop()