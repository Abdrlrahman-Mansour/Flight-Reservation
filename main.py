import tkinter as tk
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage
from database import create_table

class FlightReservationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("800x600")
        self.frames = {}
        
        create_table()
        
        # Use string keys
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            frame = F(self, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("HomePage")
    
    def show_frame(self, context, reservation_id=None):
        frame = self.frames[context if isinstance(context, str) else context.__name__]
        if context == "EditReservationPage" or context == EditReservationPage:
            if reservation_id:
                frame.prefill_form(reservation_id)
        frame.tkraise()

if __name__ == "__main__":
    app = FlightReservationApp()
    app.mainloop()