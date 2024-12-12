from datetime import datetime, timedelta

class Flight:
    def __init__(self, flight_number: str,
                 departure_city: str,
                 arrival_city: str,
                 departure_time: datetime,
                 arrival_time: datetime,
                 capacity: int):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.capacity = capacity
        self.booked_seats = 0

    def __str__(self):
        return f"{self.flight_number} from {self.departure_city} to {self.arrival_city} in {self.departure_time} until {self.arrival_time}"

    def duration_time(self) -> timedelta:
        """
        Calculate the duration of the flight.
        :return: Duration of the flight
        """
        return self.arrival_time - self.departure_time

    def has_available_seats(self, seats_needed: int = 1) -> bool:
        """
        Check if the flight has available seats.
        :param seats_needed: Number of seats needed
        :return: True if the flight has available seats, False otherwise.
        """
        return (self.capacity - self.booked_seats) >= seats_needed

    def book_seats(self, seats: int = 1) -> bool:
        """
        Books a number of seats, if available.
        :param seats: seats going to be booked.
        :return: True if flight has booked successfully, False otherwise.
        """
        if self.has_available_seats(seats):
            self.booked_seats += seats
            return True
        return False
