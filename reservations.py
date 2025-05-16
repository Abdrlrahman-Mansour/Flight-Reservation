import tkinter as tk
from tkinter import ttk
from database import fetch_all_reservations, delete_reservation
from edit_reservation import EditReservationPage

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Treeview to display reservations
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Flight", text="Flight Number")
        self.tree.heading("Departure", text="Departure")
        self.tree.heading("Destination", text="Destination")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Seat", text="Seat Number")
        # Add other headings...
        self.tree.pack(pady=20)
        
        # Load data
        self.refresh_table()
        
        # Buttons
        edit_btn = tk.Button(self, text="Edit", command=self.edit)
        edit_btn.pack(side=tk.LEFT, padx=10)
        
        delete_btn = tk.Button(self, text="Delete", command=self.delete)
        delete_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = tk.Button(self, text="Back", command=lambda: controller.show_frame("HomePage"))
        back_btn.pack(pady=10)  # or .grid(), depending on your layout
    
    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in fetch_all_reservations():
            self.tree.insert("", tk.END, values=row)
    
    def edit(self):
        selected = self.tree.selection()
        if selected:
            reservation_id = self.tree.item(selected[0], "values")[0]
            self.controller.show_frame(EditReservationPage, reservation_id)
    
    def delete(self):
        selected = self.tree.selection()
        if selected:
            reservation_id = self.tree.item(selected[0], "values")[0]
            delete_reservation(reservation_id)
            self.refresh_table()