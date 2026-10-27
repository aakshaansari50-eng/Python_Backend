def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie:", movie_name)
    print("Seat:", seat_type)
    print("Snacks:", snacks)

book_movie_ticket("Jawan", "Regular", "Popcorn")
print()

book_movie_ticket(movie_name="Pathaan", seat_type="VIP", snacks="Pizza")
print()

book_movie_ticket("Jawan", snacks="Nachos", seat_type="VIP")