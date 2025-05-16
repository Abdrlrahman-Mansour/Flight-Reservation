import tkinter as tk
from database import insert_reservation

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Input fields
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}
        for idx, field in enumerate(fields):
            label = tk.Label(self, text=field)
            label.grid(row=idx, column=0, padx=10, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entries[field] = entry
        
        # Submit button
        submit_btn = tk.Button(self, text="Submit", command=self.submit)
        submit_btn.grid(row=6, column=1, pady=10)
        
        # Back button
        back_btn = tk.Button(self, text="Back", command=lambda: controller.show_frame("HomePage"))
        back_btn.grid(row=6, column=0, pady=10)
    
    def submit(self):
        data = [self.entries[field].get() for field in self.entries]
        insert_reservation(data)
        self.controller.show_frame("HomePage")