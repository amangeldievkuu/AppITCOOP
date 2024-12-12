from flight_search import FlightSearchEngine
from booking import Booking
from flight import Flight
from trip import Trip
from datetime import datetime

flight1 = Flight(flight_number="TPT808",
                 departure_city="Taipei", arrival_city="Tokio",
                 departure_time=datetime(2024, 12, 10,9,45),
                 arrival_time=datetime(2024, 12, 15,11,30), capacity=100)

flight2 = Flight(flight_number="HF345",
                 departure_city="Singapore", arrival_city="Seoul",
                 departure_time=datetime(2024, 12, 10,14,0),
                 arrival_time=datetime(2024, 12, 12,19,00), capacity=100)

flight3 = Flight(flight_number="GF787",departure_city="Kuala-Lumpur",
        arrival_city="Ho Chi Minh",departure_time=datetime(2024, 12, 20, 11, 0),
        arrival_time=datetime(2024, 12, 20, 13, 30), capacity=20)

flight4 = Flight(flight_number="TA80",
                 departure_city="Taipei", arrival_city="Tokio",
                 departure_time=datetime(2024, 12, 10,10,45),
                 arrival_time=datetime(2024, 12, 15,13,30), capacity=10)


trip = Trip("TASI71")
trip.add_flight(flight1)
trip.add_flight(flight2)
trip.add_flight(flight3)
trip.add_flight(flight4)

booking_sys = Booking()
booking_sys.create_booking(flight1, seats=2)
booking_sys.create_booking(flight4, seats=4)

flights = [flight1, flight2, flight3, flight4]

search_engin = FlightSearchEngine(flights=flights)

found_flights = search_engin.search(
    dep_city="Taipei",
    arrival_city="Tokio",
    dep_date= datetime(2024, 12, 10).date(),
    start_time=datetime(2024, 12, 10,9,45).time(),
    end_time=datetime(2024, 12, 15,12,00).time(),
    seats_needed= 3
)

print("Found flights:", [f.flight_number for f in found_flights])
print(f"{search_engin.search_with_flight_id('TA80')}")