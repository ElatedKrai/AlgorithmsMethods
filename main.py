import tkinter as tk
from tkinter import W, ttk
from tkinter import simpledialog
import sorter
from Products import Product
products = list([
    Product("Med", 17),
    Product("Shveps",18),
    Product("Veron",19),
    Product("Kris",17),
    Product("Nas",18),
])
sorters = {
    "Bubble": sorter.Bubble(),
    "Shaker": sorter.Shaker(),
    "Minimal method": sorter.Minimal(),
    "Selection": sorter.Selection(),
    "Shell": sorter.Shell(),
    "Quick":sorter.Quick(),
    "Heap":sorter.Heap(),
}

fields = {
    "Name": "name",
    "Count": "code",
}

def on_create(): 
    name = simpledialog.askstring("String", "Enter name", parent=window)
    if not name:
        return
    code = simpledialog.askinteger("Integer", "Enter number:", parent=window)
    if not code:
        return

    product = Product(name, code)
    products.append(product)
    fill_tree()


def on_delete():
    i = int(tree.selection()[0])
    del products[i]
    fill_tree()


def on_sort():
    value = combo_sort.get()
    if value not in sorters:
        return

    sorter = sorters[value]
    sorter.sort(products, fields[combo_field.get()])
    fill_tree()

def fill_tree():
    for i in tree.get_children(): 
        tree.delete(i)
    for i, product in enumerate(products):
        tree.insert("", tk.END, iid=i, values=product.values())

def binary_search(a, v, f):
    low = 0
    mid = 0
    high = len(a) - 1

    while low <= high:
        mid = (high + low) // 2
        if f(a[mid]) < v:
            low = mid + 1 
        elif f(a[mid]) > v:
            high = mid - 1
        else:
            return a[mid]
    return None

def binaryon_search():
    name = simpledialog.askstring('Пошук', "Name product:", parent=window)
    if not name:
        return
    for i in tree.get_children():
        tree.delete(i)
    e = binary_search(products, name, lambda e: e.name)
    if e:
        tree.insert('', tk.END, iid=i, values=e.values())

def interpolaron_search():
    code = int(simpledialog.askstring('Пошук', "Code comand:", parent=window))
    if not code:
        return
    for i in tree.get_children():
        tree.delete(i)
    e = binary_search(products, code, lambda e: e.code)
    if e:
        tree.insert('', tk.END, iid=i, values=e.values())

def on_save():
    i = int(tree.selection()[0])
    del products[i]
    fill_tree()

window = tk.Tk()
window.title("Algorithms sortings")

columns = ("Names", "Counts")
tree = ttk.Treeview(window, show="headings", columns=columns)
tree.grid(row=0, column=0, columnspan=20)

for col in columns:
    tree.heading(col, text=col)

global combo_sort
combo_sort = ttk.Combobox(
    window, values=list(sorters.keys()))  # тип сортування
combo_sort.current(0)
combo_sort.grid(row=2, column=0)

global combo_field
combo_field = ttk.Combobox(
    window, values=list(fields.keys()))  # поле сортуваннb
combo_field.current(0)
combo_field.grid(row=2, column=1)

create = ttk.Button(window, text="Create Object", command=on_create)
create.grid(row=1, column=2)

delete = ttk.Button(window, text="Delete", command=on_delete)
delete.grid(row=1, column=1)

sort = ttk.Button(window, text="Sort", command=on_sort)
sort.grid(row=1, column=0)

binarysearch = ttk.Button(window, text = "Binary Search", command=binaryon_search)
binarysearch.grid(row=2, column= 2)

save = ttk.Button(window, text="Load list", command=on_sort)
save.grid(row=1, column=3)
window.mainloop()