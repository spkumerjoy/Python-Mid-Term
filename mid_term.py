class Star_Cinema:
    hall_list = []

    def entry_hall(self, id, name):
        self.id = id
        self.name = name

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema.hall_list.append(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        seats_2d = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seats_2d

    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print("Show ID not found")
            return
        
        for row, col in seat_list:
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                print(f"Invalid seat: ({row}, {col}). Seat out of range.")
                continue

            if self.seats[show_id][row][col] == 1:
                print(f"Seat ({row}, {col}) is already booked.")
            else:
                self.seats[show_id][row][col] = 1
                print(f"Seat ({row}, {col}) booked successfully.")

    def view_show_list(self):
        print("Shows Running:")
        for show_info in self.show_list:
            print(f"ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print("Show ID not found.")
            return
        
        print(f"Available seats for show ID {show_id}:")
        for row in self.seats[show_id]:
            row_str = ""
            for seat in row:
                row_str += "[1]" if seat == 1 else "[0]"
            print(row_str)

hall = Hall(5, 7, 1)
hall.entry_show(111, "Jinda Jawan", "25/10/24 11:30AM")
hall.entry_show(222, "Lapata Ladis", "27/09/24 09:30AM")

run = True

while run:
    print("<<<<<---------------------->>>>>")
    print(">>>>>---Chose an option below---<<<<<")
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. Exit")
    print("<<<<<---------------------->>>>>")

    ch = int(input("\nEnter Option: "))

    if ch == 1:
        hall.view_show_list()
    elif ch == 2:
        show_id = int(input("Enter show ID: "))
        hall.view_available_seats(show_id)
    elif ch == 3:
        show_id = int(input("Enter show ID: "))
        num_seats = int(input("Enter number of seats to book: "))
        seats_to_book = []
        for _ in range(num_seats):
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            seats_to_book.append((row, col))
        hall.book_seats(show_id, seats_to_book)
    elif ch == 4:
        run = False
    else:
        print("Invalid option! Please chose valid option.")

