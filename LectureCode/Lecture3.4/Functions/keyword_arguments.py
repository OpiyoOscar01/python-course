def book_flight(destination, departure, return_date):
  print(f"Booking a flight to {destination}.")
  print(f"Departure date: {departure}")
  print(f"Return date: {return_date}")
  print("Your flight has been booked!\n")

# Using keyword arguments
book_flight("Kampala", "2025-12-15", "2025-12-20")
book_flight("2025-12-15","Kampala", "2025-12-20")
book_flight(return_date="2023-12-20", destination="Paris", departure="2023-12-10")