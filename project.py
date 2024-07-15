import random
import datetime

# Constants
randomchars = "1234567890"
randompairs = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]

# Train schedule dictionary
train_schedule = {
    "11076": {"place": "Chennai", "departure": "08:00", "arrival": "10:00", "seats": 23},
    "06658": {"place": "Bangalore", "departure": "12:00", "arrival": "14:00", "seats": 34},
    "16237": {"place": "Thiruvananthapuram", "departure": "16:00", "arrival": "18:00", "seats": 56}
}

# Booking dictionary
bookings = {}

def generate_pnr():
    """Generates a random PNR number in the format XXX-XXXXXXX."""
    part1 = ''.join(random.choices(randomchars, k=3))
    part2 = ''.join(random.choices(randomchars, k=7))
    return f"{part1}-{part2}"

def generate_seat():
    """Generates a random seat number."""
    return ''.join(random.choices(randomchars, k=2))

def generate_id():
    """Generates a random booking ID."""
    return ''.join(random.choices(randomchars, k=5))

def generate_coach():
    """Randomly selects a coach."""
    return random.choice(randompairs)

def ticket_rate(train_number, age):
    """Calculates ticket rate based on train number and age."""
    if train_number == "11076":
        base_rate = 200 if age < 10 else 455
    elif train_number == "06658":
        base_rate = 250 if age < 10 else 525
    elif train_number == "16237":
        base_rate = 180 if age < 10 else 385
    else:
        base_rate = 15
    return base_rate

def display_schedule():
    """Displays the train schedule."""
    print("Train Schedule:")
    print(f"{'Train No.':<10}{'Place':<20}{'Departure':<10}{'Arrival':<10}{'Seats Available':<15}")
    for train, details in train_schedule.items():
        print(f"{train:<10}{details['place']:<20}{details['departure']:<10}{details['arrival']:<10}{details['seats']:<15}")

def book_ticket():
    """Books a ticket for a train."""
    display_schedule()
    train_number = input("Enter train number to book: ")
    if train_number in train_schedule:
        if train_schedule[train_number]['seats'] > 0:
            train_schedule[train_number]['seats'] -= 1
            passenger_name = input("Enter your name: ")
            gender = input("Enter your gender: ")
            age = int(input("Enter your age: "))
            number = input("Enter your mobile number: ")
            pnr = generate_pnr()
            seat = generate_seat()
            coach = generate_coach()
            booking_id = generate_id()  # Use generated booking ID here
            
            # Allow user to specify a booking date (optional, defaults to current date)
            date_input = input("Enter booking date (DD-MM-YYYY) or press Enter for today: ")
            if date_input.strip() == "":
                booking_date = datetime.datetime.now()
            else:
                try:
                    booking_date = datetime.datetime.strptime(date_input, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Using current date.")
                    booking_date = datetime.datetime.now()
            
            # Allow user to specify a traveling date
            travel_date_input = input("Enter traveling date (DD-MM-YYYY): ")
            try:
                travel_date = datetime.datetime.strptime(travel_date_input, "%d-%m-%Y")
            except ValueError:
                print("Invalid date format. Using default arrival date from schedule.")
                travel_date = datetime.datetime.strptime(f"{booking_date.strftime('%Y')}-{train_schedule[train_number]['departure']}", "%Y-%m-%d %H:%M")
            
            rate = ticket_rate(train_number, age)
            
            # Store booking details in the dictionary with booking_id as the key
            bookings[booking_id] = {
                'train_number': train_number,
                'passenger_name': passenger_name,
                'booking_date': booking_date,
                'travel_date': travel_date,
                'seat': seat,
                'coach': coach,
                'rate': rate,
                'pnr': pnr
            }

            print("Booking successful!")
            generate_ticket(booking_id, train_number, seat, pnr, coach, rate, booking_date, travel_date)
        else:
            print("Sorry, no seats available for this train.")
    else:
        print("Invalid train number.")

def view_booking():
    """Views a specific booking."""
    booking_id = input("Enter your booking ID: ")  # Keep booking ID as string
    if booking_id in bookings:
        booking = bookings[booking_id]
        print(f"Booking ID: {booking_id}")
        print(f"Passenger Name: {booking['passenger_name']}")
        print(f"Train Number: {booking['train_number']}")
        print(f"Seat: {booking['seat']}")
        print(f"Coach: {booking['coach']}")
        print(f"Booking Date: {booking['booking_date'].strftime('%d-%m-%Y')}")
        print(f"Traveling Date: {booking['travel_date'].strftime('%d-%m-%Y')}")
        print(f"Rate: ${booking['rate']}")
    else:
        print("Invalid booking ID.")

def generate_ticket(booking_id, train_number, seat, pnr, coach, rate, booking_date, travel_date):
    """Generates and prints a ticket."""
    print("\n======= Ticket =======")
    print("    HAPPY JOURNEY    ")
    print(f"Booking ID: {booking_id}")
    print(f"PNR: {pnr}")
    print(f"Train Number: {train_number}")
    print(f"Coach: {coach}")
    print(f"Seat number: {seat}")
    print(f"Rate: ${rate}")
    print(f"Booking Date: {booking_date.strftime('%d-%m-%Y')}")
    print(f"Traveling Date: {travel_date.strftime('%d-%m-%Y')}")
    print("======================\n")

def cancel_booking():
    """Cancels a booking."""
    booking_id = input("Enter your booking ID: ")  # Keep booking ID as string
    if booking_id in bookings:
        booking = bookings.pop(booking_id)
        train_schedule[booking['train_number']]['seats'] += 1
        print("Booking cancelled successfully.")
    else:
        print("Invalid booking ID.")

while True:
    """Main loop for the reservation system."""
    print("Welcome to Train Reservation System")
    print("1. View Train Schedule")
    print("2. Book Ticket")
    print("3. View Booking")
    print("4. Cancel Booking")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_schedule()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        view_booking()
    elif choice == "4":
        cancel_booking()
        break
    elif choice == "5":
        print("Thank you for using the Train Reservation System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")





