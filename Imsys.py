import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
#------------------Authentication-----------------
users = {"admin": "password"}
def authenticate(username, password):
    return users.get(username) == password
#------------------------------Inventory Management-------------
inventory_file = "inventory.json"

def load_inventory():
    try:
        with open(inventory_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def save_inventory(data):
    with open(inventory_file, "w") as file:
         json.dump(data, file, indent=4)
inventory = load_inventory()
def add_product(name, quantity, price):  
    if name in inventory:
        messagebox.showerror("Error","Product already exists.")
    else:
        inventory[name] = {"quantity": quantity, "price": price}
        save_inventory(inventory)
        messagebox.showinfo("Success", "Product added successfully.")
def edit_Product(name, quantity, Price):
    if name in inventory:
        inventory[name] = {"quantity": quantity, "Price": Price }
        save_inventory(inventory)
        messagebox.showinfo("Success", "Product updated successfully.")
    else:
        messagebox.showinfo("Error", "Product not found.")
def delete_Product(name):
    if name in inventory:
        del inventory[name] 
        save_inventory(inventory)
        messagebox.showinfo("Success", "Product deleted successfully.")
    else:
        messagebox.showinfo("Error", "Product not found.")             
def low_stock_alert():
    alert = "Low Stock Products:\n"
    for name, details in inventory.items():
        if details ["quantity"] < 5:
            alert += f"{name}: {details['quantity']}\n"   
    return alert if alert != "Low Stock Products:\n"  else "No low stock products."            
#----------------------------------GUI-----------------
def main_app():
    root = tk.Tk()
    root.title("Inventory Management System")
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if authenticate(username, password):
            login_frame.pack_forget()
            inventory_frame.pack(fill="both", expand=True)
        else:
            messagebox.showerror("Login failed", "Inavlid username or password.")
    # Login  Frame
    login_frame = tk.Frame(root)
    login_frame.pack(fill="both", expand=True)
    tk.Label(login_frame, text="Username:").pack()
    username_entry = tk.Entry(login_frame)
    username_entry.pack()
    tk.Label(login_frame, text="Password:").pack()
    password_entry = tk.Entry(login_frame, show="*")
    password_entry.pack()
    tk.Button(login_frame, text="Login", command=login).pack()
    # Inventory Frame
    inventory_frame = tk.Frame(root)
    def add_Product_gui():
        name = name_entry.get()
        try:
            quantity = int(quantity_entry.get())
            price = float(price_entry.get())
            add_product(name, quantity, price)
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity or price.")    
    def edit_product_gui():
        name = name_entry.get()
        try:
            quantity = int(quantity_entry.get())
            price = float(price_entry.get())
            edit_Product(name, quantity, price)
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity or price.")
    def delete_product_gui():
        name = name_entry.get()
        delete_Product(name)
    def show_low_stock():
        alert = low_stock_alert()
        messagebox.showinfo("Low Stock Alert", alert)
    tk.Label(inventory_frame, text="Name:").pack()
    name_entry = tk.Entry(inventory_frame) 
    name_entry.pack()
    tk.Label(inventory_frame, text="quantity:").pack()
    quantity_entry = tk.Entry(inventory_frame) 
    quantity_entry.pack()
    tk.Label(inventory_frame, text="Price:").pack()
    price_entry = tk.Entry(inventory_frame)
    price_entry.pack()
    tk.Button(inventory_frame, text="Add Product", command=add_Product_gui).pack()
    tk.Button(inventory_frame, text="Edit Product", command=edit_product_gui).pack()
    tk.Button(inventory_frame, text="Delete Product", command=delete_product_gui).pack()
    tk.Button(inventory_frame, text="Low Stock Alert", command=show_low_stock).pack()
    root.mainloop()
if __name__ == "__main__":
    main_app()    



    
    