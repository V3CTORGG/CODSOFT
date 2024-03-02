import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Name:").grid(row=0, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(self.root, text="Phone:").grid(row=1, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.phone_var).grid(row=1, column=1)

        tk.Label(self.root, text="Email:").grid(row=2, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.email_var).grid(row=2, column=1)

        tk.Label(self.root, text="Address:").grid(row=3, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.address_var).grid(row=3, column=1)

        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)

        self.contacts_listbox = tk.Listbox(self.root, width=40)
        self.contacts_listbox.grid(row=5, column=0, columnspan=2)
        self.contacts_listbox.bind('<<ListboxSelect>>', self.on_contact_select)

        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=6, column=0, columnspan=2, pady=5)

        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2)

        tk.Label(self.root, text="Search:").grid(row=8, column=0, sticky="e")
        self.search_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.search_var).grid(row=8, column=1)
        tk.Button(self.root, text="Search", command=self.search_contact).grid(row=9, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if name and phone:
            contact_info = (name, phone, email, address)
            self.contacts.append(contact_info)
            self.contacts_listbox.insert(tk.END, name + " - " + phone)
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and phone number are required.")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]
            self.contacts_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            name = self.name_var.get()
            phone = self.phone_var.get()
            email = self.email_var.get()
            address = self.address_var.get()
            if name and phone:
                contact_info = (name, phone, email, address)
                self.contacts[selected_index[0]] = contact_info
                self.contacts_listbox.delete(selected_index)
                self.contacts_listbox.insert(selected_index, name + " - " + phone)
                self.clear_entries()
            else:
                messagebox.showwarning("Warning", "Name and phone number are required.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to update.")

    def search_contact(self):
        search_term = self.search_var.get()
        self.contacts_listbox.delete(0, tk.END)
        for contact_info in self.contacts:
            if search_term.lower() in contact_info[0].lower() or search_term in contact_info[1]:
                self.contacts_listbox.insert(tk.END, contact_info[0] + " - " + contact_info[1])

    def on_contact_select(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            contact_info = self.contacts[selected_index[0]]
            self.name_var.set(contact_info[0])
            self.phone_var.set(contact_info[1])
            self.email_var.set(contact_info[2])
            self.address_var.set(contact_info[3])

    def clear_entries(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")

root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()
