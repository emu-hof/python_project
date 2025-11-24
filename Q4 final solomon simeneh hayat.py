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

print("\nWelcome to Alem Cinema!!!")
print("-" * 25)

# Continue/exit question
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

    # Check if ALL movies are fully booked
    if all(m["seats"] == 0 for m in movies.values()):
        print("\nAll movies are fully booked!")
        break

    # Display list of movies
    print("\nAvailable Movies:")
    for key, info in movies.items():
        print(f"{key}. {info['title']} ({info['time']}) - ETB {info['price']} - Seats Left: {info['seats']}")

    # Choose movie
    choice = input("\nChoose a movie (1, 2, or 3): ").strip()
    while choice not in movies:
        print("Invalid choice! Please enter 1, 2, or 3.")
        choice = input("Choose a movie (1, 2, or 3): ").strip()

    selected_movie = movies[choice]
    print("You selected:", selected_movie["title"])

    # If no seats
    if selected_movie["seats"] == 0:
        print("\n No seats left for this movie! Please choose another movie with available seats.")
        continue

    # BOOKING LOOP FOR THIS MOVIE
    while True:

        # Remaining seats
        print(f"\nRemaining seats for {selected_movie['title']}: {selected_movie['seats']}")

        # Ticket input
        number_of_tickets = input("How many tickets would you like? ")

        while (not number_of_tickets.isdigit() or 
               int(number_of_tickets) <= 0 or 
               int(number_of_tickets) > selected_movie["seats"]):
            print(f"Enter a number between 1 and {selected_movie['seats']}")
            number_of_tickets = input("How many tickets would you like? ")

        number_of_tickets = int(number_of_tickets)

        # Update seats
        selected_movie["seats"] -= number_of_tickets

        # Calculate and save booking
        cost = selected_movie["price"] * number_of_tickets
        total_cost += cost
        total_tickets += number_of_tickets
        bookings.append((selected_movie["title"], number_of_tickets, cost))

        print(f"\nBooked {number_of_tickets} ticket(s) for {selected_movie['title']} - Cost: ETB {cost:,}")

        # If movie becomes full
        if selected_movie["seats"] == 0:
            print("\n This movie is now FULL! Please choose another movie.")
            break

        # More tickets for same movie?
        # another_ticket = input("\nWant to book more tickets for {selected_movie['title']} movie? (yes(y)/no): ").strip().lower()
        another_ticket = input(f"\nWant to book more tickets for {selected_movie['title']} movie? (yes(y)/no): ").strip().lower()
        if another_ticket not in ("yes", "y"):
            break

    # Book another movie
    another_movie = input("\nWant to book another movie? (yes(y)/no): ").strip().lower()

    if another_movie not in ("yes", "y"):
        break

    print("\nLoading movies...\n")

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