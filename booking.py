from typing import List, Tuple
from flight import Flight


class Booking:
    def __init__(self):
        self.bookings: List[Tuple[Flight, int]] = []

    def create_booking(self, flight: Flight, seats: int = 1) -> bool:
       """
       creates a new booking if seats available
       :param flight: Flight object
       :param seats: number of seats
       :return: True if successfully booked, False otherwise
       """
       if flight.has_available_seats(seats):
           flight.book_seats(seats)
           self.bookings.append((flight, seats))
           print(f"Flight {flight.flight_number} successfully booked with {seats} seats")
           return True
       print("Could not book seats, unavailable seats")
       return False
