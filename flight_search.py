import datetime
from typing import List
from flight import Flight


class FlightSearchEngine:
    def __init__(self, flights: List[Flight]):
        self.flights = flights


    def search(self, dep_city: str,
               arrival_city: str,
               dep_date: datetime.date,
               start_time: datetime.time,
               end_time: datetime.time,
               seats_needed: int = 1) -> List[Flight]:
        """
        Search flights
        :param dep_city: departure city
        :param arrival_city: arrival city
        :param dep_date: departure date
        :param start_time: start time
        :param end_time: end time
        :param seats_needed: number of seats
        :return: list of flights
        """
        result = []
        for flight in self.flights:
            if (flight.departure_city.lower() == dep_city.lower() and
            flight.arrival_city.lower() == arrival_city.lower() and
            flight.departure_time.date() == dep_date and
            start_time <= flight.departure_time.time() <= end_time and
            flight.has_available_seats(seats_needed)):
                result.append(flight)
        return result

    def search_with_flight_id(self, flight_number: str) -> Flight:
        flight_result = None
        for flight in self.flights:
            if flight.flight_number == flight_number:
                flight_result = flight
        return flight_result