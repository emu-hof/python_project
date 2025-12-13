# Group 4 Q4: Prepared by: Hayat; Solomon; Simeneh
# 4. Movie Ticket Booking Simulation
    # Simulate a movie theater booking system that:
        # Shows a list of available movie titles, showtimes, and seat prices.
        # Asks the user to choose a movie and number of tickets.
        # Confirms total price and asks if they want to book another movie.
        # Ends when they say “no” and displays total bookings and cost.

# 1. Define the movie data with movie dictionary to hold:
    # - Movie title
    # - Showtime
    # - Ticket price
    # - Seats

# Movie data   
movies = { 
    "1": {"title": "Beka Fikir", "time": "2:00 PM", "price": 200, "seats": 100},
    "2": {"title": "Liyu Aleme", "time": "7:10 PM", "price": 200, "seats": 100},
    "3": {"title": "Yefikir Chaweta", "time": "2:00 PM", "price": 200, "seats": 100}
}

# Tracking totals
total_cost = 0
total_tickets = 0
bookings = []

def show_available_movies():
    print("\nAvailable Movies with Seats:")
    for key, info in movies.items():
        if info["seats"] > 0:
            print(f"{key}. {info['title']} ({info['time']}) - ETB {info['price']} - Seats Left: {info['seats']}")
    print()

print("\nWelcome to Alem Cinema!!!")
print("-" * 25)

# Continue or exit
while True:
    continue_choice = input("\nDo you want to continue or exit? (c/x): ").strip().lower()
    if continue_choice == "c":
        break
    elif continue_choice == "x":
        print("\nThanks for visiting!")
        exit()
    else:
        print("Invalid choice! Type 'c' to continue or 'x' to exit.")

# LOOP
while True:

    # If ALL movies are fully booked
    if all(m["seats"] == 0 for m in movies.values()):
        print("\nAll movies are fully booked!")
        break

    # Show movies with seats
    show_available_movies()

    # Dynamic movie selection
    available_choices = [key for key, info in movies.items() if info["seats"] > 0]
    choice_label = ", ".join(available_choices)

    while True:
        choice = input(f"Choose a movie ({choice_label}): ").strip()
        if choice in available_choices:
            break
        print(f"Invalid choice! Please enter one of: {choice_label}")

    selected_movie = movies[choice]
    print("You selected:", selected_movie["title"])

    # BOOKING
    print(f"\nRemaining seats for {selected_movie['title']}: {selected_movie['seats']}")

    while True:
        try:
            number_of_tickets = int(input("How many tickets would you like? "))

            if number_of_tickets <= 0 or number_of_tickets > selected_movie["seats"]:
                print(f"Enter a number between 1 and {selected_movie['seats']}")
                continue

            break  # valid
        except ValueError:
            print(f"Enter a valid number between 1 and {selected_movie['seats']}")

    number_of_tickets = int(number_of_tickets)

    # Update seats
    selected_movie["seats"] -= number_of_tickets

    # Save booking
    cost = selected_movie["price"] * number_of_tickets
    total_cost += cost
    total_tickets += number_of_tickets
    bookings.append((selected_movie["title"], number_of_tickets, cost))

    print(f"\nBooked {number_of_tickets} ticket(s) for {selected_movie['title']} - Cost: ETB {cost:,}")

    # If movie becomes FULL after booking
    if selected_movie["seats"] == 0:
        print(f"\n'{selected_movie['title']}' is now FULL!")

    # Check if all movies are now fully booked
    if all(m["seats"] == 0 for m in movies.values()):
        print("\nAll movies are now fully booked.")
        break

    # Ask if user wants to book another movie
    another_movie = input("\nDo you want to book another movie? (yes(y)/no): ").strip().lower()
    if another_movie not in ("yes", "y"):
        break

# Summary
print("\n" + "-" * 15)
print("Booking Summary")
print("-" * 15)

if not bookings:
    print("No bookings made.")
else:
    for title, tickets, cost in bookings:
        print(f"{title} - {tickets} ticket(s) - ETB {cost:,}")
print(f"\nTotal tickets: {total_tickets}")
print(f"Total cost: ETB {total_cost:,}")
print("\nThanks, hope to see you again at Alem Cinema!\n")