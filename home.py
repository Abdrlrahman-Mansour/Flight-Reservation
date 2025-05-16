import tkinter as tk
from booking import BookingPage
from reservations import ReservationsPage

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Flight Reservation System", font=("Arial", 20))
        label.pack(pady=20)
        
        book_btn = tk.Button(self, text="Book Flight", command=lambda: controller.show_frame(BookingPage))
        book_btn.pack(pady=10)
        
        view_btn = tk.Button(self, text="View Reservations", command=lambda: controller.show_frame(ReservationsPage))
        view_btn.pack(pady=10)