import tkinter as tk
from database import fetch_all_reservations, update_reservation

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.reservation_id = None
        
        # Input fields (similar to BookingPage)
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}
        for idx, field in enumerate(fields):
            label = tk.Label(self, text=field)
            label.grid(row=idx, column=0, padx=10, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entries[field] = entry
        
        # Update button
        update_btn = tk.Button(self, text="Update", command=self.update)
        update_btn.grid(row=6, column=1, pady=10)
        
        # Back button
        back_btn = tk.Button(self, text="Back", command=lambda: controller.show_frame("ReservationsPage"))
        back_btn.grid(row=6, column=0, pady=10)
    
    def prefill_form(self, reservation_id):
        self.reservation_id = int(reservation_id)
        reservation = next(row for row in fetch_all_reservations() if row[0] == self.reservation_id)
        entries_order = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        for field, value in zip(entries_order, reservation[1:]):
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, value)
    
    def update(self):
        data = [self.entries[field].get() for field in self.entries]
        update_reservation(self.reservation_id, data)
        self.controller.show_frame("ReservationsPage")