def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]


def book(booked_seats, seat_to_book, total_seats):
    if seat_to_book in booked_seats:
        print(f"Seat {seat_to_book} is already booked.")
    elif seat_to_book < 1 or seat_to_book > total_seats:
        print(f"Seat {seat_to_book} is not valid.")
    else:
        booked_seats.append(seat_to_book)
    return booked_seats


def cancel(booked_seats, seat_to_cancel):
    if seat_to_cancel in booked_seats:
        booked_seats.remove(seat_to_cancel)
    else:
        print(f"Seat {seat_to_cancel} is not booked.")
    return booked_seats


total_seats = 10
booked_seats = [2, 5, 7]

book_seat_number = 3
cancel_seat_number = 5

booked_seats = book(booked_seats, book_seat_number, total_seats)
booked_seats = cancel(booked_seats, cancel_seat_number)
available = available_seats(total_seats, booked_seats)

print("Available seats:", available)
