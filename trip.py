from typing import List
from flight import Flight

class Trip:
    def __init__(self, trip_id:str) -> None:
        self.trip_id = trip_id
        self.flights: List[Flight] = []

    def add_flight(self, flight: Flight) -> bool:
        """
        Adds a flight to the trip. If a trip is overlapping with existing flights time, will not be added.
        :param flight: Flight to be added.
        :return: True if the flight was added, False otherwise
        """
        if self.is_time_conflict(flight):
            print("Trip cannot be added because of a time conflict.")
            return False
        self.flights.append(flight)
        print(f"Flight {flight.flight_number} added to trip.")
        return True

    def is_time_conflict(self, new_flight: Flight) -> bool:
        """
        :param new_flight: Flight to be checked whether it is a time conflicts.
        :return: True if time conflicts with existing flight, False otherwise
        """
        for f in self.flights:
            if not (new_flight.arrival_time <= f.departure_time or new_flight.departure_time <= f.arrival_time):
                return True
        return False
