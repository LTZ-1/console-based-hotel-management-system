
#update 3
import os
from datetime import datetime

class HotelRoom:
    def __init__(self, room_number, room_type, price, reserved=False):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.reserved = reserved

    def display_info(self):
        return (f"Room Number: {self.room_number}, "
                f"Room Type: {self.room_type}, "
                f"Price: ${self.price:.2f}, "
                f"Reserved: {'Yes' if self.reserved else 'No'}")

class Hotel:
    def __init__(self):
        self.room_data = {  # Change the name of the dictionary here
            101: HotelRoom(101, "Standard", 100.00),
            102: HotelRoom(102, "Deluxe", 150.00),
            103: HotelRoom(103, "Executive", 200.00),
            104: HotelRoom(104, "Suite", 250.00)
        }
        self.occupied_rooms = {}

    def display_menu(self):
        print("Welcome to getvah hotel")
        print("1. Services")
        print("2. Rooms")
        print("3. Payment and Transactions")
        print("4. Exit")

    def display_services_menu(self):
        print("Services Menu:")
        print("1. Drinks")
        print("2. Foods")
        print("3. Back to Main Menu")

    def display_rooms_menu(self):
        print("Rooms Menu:")
        for room_number, room in self.rooms.items():
            print(room.display_info())
        print("5. Back to Main Menu")

    def services(self):
        while True:
            self.display_services_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.order_drinks()
            elif choice == "2":
                self.order_foods()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def order_drinks(self):
        print("Drinks Menu:")
        drinks = {
            1: ("Tea/Coffee", 20),
            2: ("Beer", 70),
            3: ("Whiskey", 100),
            4: ("Vodka", 150),
            5: ("Soft Drinks", 120),
        }
        total_price = 0
        ordered_items = []
        proceed = ""

        while True:
            print("ID\tDrink\t\tPrice")
            for drink_id, (drink_name, price) in drinks.items():
                print(f"{drink_id}\t{drink_name}\t\t${price}")

            choice = input("Enter drink ID to order (or 'exit' to go back): ")

            if choice.lower() == "exit":
                if total_price == 0:
                    print("No drinks ordered.")
                    break
                else:
                    print("Ordered Drinks:")
                    for item in ordered_items:
                        print(item)
                    print(f"Total Price: ${total_price:.2f}")
                    proceed = input("Do you want to proceed (yes/no): ").lower()
                    if proceed == "yes":
                        payment_choice = input("Do you want to pay normally or for room (normal/room): ").lower()
                        if payment_choice == "normal":
                            self.payment_form(total_price)
                        elif payment_choice == "room":
                            room_number = input("Enter room number: ")
                            if room_number in self.occupied_rooms:
                                self.room_service(room_number, total_price, ordered_items)
                                break
                            else:
                                print("Invalid room number.")
                        else:
                            print("Invalid choice.")
                            break
                    elif proceed == "no":
                        break
                    else:
                        print("Invalid choice.")
            else:
                drink_id = int(choice)
                if drink_id in drinks:
                    quantity = int(input("Enter quantity: "))
                    drink_name, price = drinks[drink_id]
                    total_price += price * quantity
                    ordered_items.append(f"{drink_name}: {price} * {quantity} = ${price * quantity:.2f}")
                else:
                    print("Invalid drink ID. Please try again.")

            if proceed == "yes":
                payment_method = input("Select payment method (card/cash): ").lower()
                if payment_method == "card":
                    self.payment_form_card(total_price)
                elif payment_method == "cash":
                    self.payment_form_cash(total_price)
                else:
                    print("Invalid payment method.")
                    break

    def order_foods(self):
        print("Foods Menu:")
        foods = {
            1: ("Pizza", 20),
            2: ("Burger", 70),
            3: ("Shiro", 100),
            4: ("Tegabino", 150),
            5: ("Kitfo", 120),
        }
        total_price = 0
        ordered_items = []
        proceed = ""

        while True:
            print("ID\tFood\t\tPrice")
            for food_id, (food_name, price) in foods.items():
                print(f"{food_id}\t{food_name}\t\t${price}")

            choice = input("Enter food ID to order (or 'exit' to go back): ")

            if choice.lower() == "exit":
                if total_price == 0:
                    print("No foods ordered.")
                    break
                else:
                    print("Ordered Foods:")
                    for item in ordered_items:
                        print(item)
                    print(f"Total Price: ${total_price:.2f}")
                    proceed = input("Do you want to proceed (yes/no): ").lower()
                    if proceed == "yes":
                        payment_choice = input("Do you want to pay normally or for room (normal/room): ").lower()
                        if payment_choice == "normal":
                            self.payment_form(total_price)
                        elif payment_choice == "room":
                            room_number = input("Enter room number: ")
                            if room_number in self.occupied_rooms:
                                self.room_service(room_number, total_price, ordered_items)
                                break
                            else:
                                print("Invalid room number.")
                        else:
                            print("Invalid choice.")
                            break
                    elif proceed == "no":
                        break
                    else:
                        print("Invalid choice.")
            else:
                food_id = int(choice)
                if food_id in foods:
                    quantity = int(input("Enter quantity: "))
                    food_name, price = foods[food_id]
                    total_price += price * quantity
                    ordered_items.append(f"{food_name}: {price} * {quantity} = ${price * quantity:.2f}")
                else:
                    print("Invalid food ID. Please try again.")

            if proceed == "yes":
                payment_method = input("Select payment method (card/cash): ").lower()
                if payment_method == "card":
                    self.payment_form_card(total_price)
                elif payment_method == "cash":
                    self.payment_form_cash(total_price)
                else:
                    print("Invalid payment method.")
                    break

    def room_service(self, room_number, total_price, ordered_items):
        if room_number in self.occupied_rooms:
            print(f"Room Service for Room {room_number}:")
            print("Ordered Foods:")
            for item in ordered_items:
                print(item)
            print(f"Total Price: ${total_price:.2f}")

            self.occupied_rooms[room_number]['room_service'] += total_price
            print(f"Room service added to Room {room_number}.")

            self.save_room_service(room_number, ordered_items, total_price)
        else:
            print("Invalid room number")

    def rooms_menu(self):
     while True:
        print("Rooms Menu:")
        print("1. Check-in")
        print("2. Room Service")
        print("3. Status")
        print("4. Check-out")
        print("5. Back to Main Page")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.check_in()
        elif choice == "2":
            self.room_service()
        elif choice == "3":
            self.display_status()
        elif choice == "4":
            self.check_out()
        elif choice == "5":
            self.main()  # Navigate back to the main menu
        else:
            print("Invalid choice. Please try again.")

    def check_in(self):
        print("Rooms Menu:")
        for room_number, room in self.room_data.items():
            print(room.display_info())
        room_number = int(input("Enter room number for check-in: "))
        room = self.room_data.get(room_number)
        if room and not room.reserved:
            print(f"Room {room.room_number} selected.")
            bed_choice = input("Select bed type (1. One bed / 2. Two beds): ")
            if bed_choice == "2":
                room.price *= 1.5
            name = input("Enter client name: ")
            address = input("Enter address: ")
            phone = input("Enter contact no.: ")
            check_in_date = datetime.today().date()
            room.reserved = True
            self.occupied_rooms[room.room_number] = {
                "name": name,
                "address": address,
                "phone": phone,
                "check_in_date": check_in_date,
                "room_type": room.room_type,
                "room_price": room.price,
                "room_service": 0,
            }
            print(f"Check-in completed for {name} in room {room.room_number} on {check_in_date}.")
            self.save_to_file(room_number, name, address, phone, check_in_date, room.room_type, room.price)
        else:
            print("Invalid room number or room already reserved.")
            return  # Return to the rooms menu after displaying rooms

    def save_to_file(self, room_number, name, address, phone, check_in_date, room_type, room_price):
        with open("vip.txt", "a") as text_file:
            text_file.write(f"{room_number},{name},{address},{phone},{check_in_date},{room_type},{room_price}\n")

    def display_status(self):
        with open("vip.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                room_number = data[0]
                name = data[1]
                address = data[2]
                phone = data[3]
                check_in_date = data[4]
                room_type = data[5]
                room_price = data[6]
                room_service = data[7]

                print(f"Room Number: {room_number}")
                print(f"Name: {name}")
                print(f"Address: {address}")
                print(f"Phone: {phone}")
                print(f"Check-in Date: {check_in_date}")
                print(f"Room Type: {room_type}")
                print(f"Room Price: {room_price}")
                print(f"Room Service: {room_service}")
                print("-" * 50)

    def check_out(self):
        room_number = int(input("Enter room number for check-out: "))
        if room_number in self.occupied_rooms:
            check_out_date = datetime.today().date()
            check_in_date = self.occupied_rooms[room_number]['check_in_date']
            duration = (check_out_date - check_in_date).days
            room_price = self.occupied_rooms[room_number]['room_price']
            room_service = self.occupied_rooms[room_number]['room_service']
            total_price = (room_price * duration) + room_service
            print(f"Total price for room {room_number} is ${total_price:.2f}")
            payment = input('Proceed to payment? (yes/no): ').lower()
            if payment == 'yes':
                print('Payment completed. Thank you for staying with us!')
                self.rooms[room_number].reserved = False
                self._remove_from_vip_file(room_number)  # Call _remove_from_vip_file here
                del self.occupied_rooms[room_number]
            else:
                print('Payment cancelled. Please settle the payment before check-out.')
        else:
            print('Invalid room number')

    def _remove_from_vip_file(self, room_number):
        with open("vip.txt", 'r') as file:
            lines = file.readlines()
        with open("vip.txt", 'w') as file:
            for line in lines:
                if not line.startswith(str(room_number)):
                    file.write(line)
        print("Room removed from the file.")
    def payment_form(self, total_price):
     print("Payment Form")
    # Implement your payment form logic here

    def payment_form_card(self, total_price):
        print("Card Payment Form")
        card_number = input("Enter card number: ")
        expiry_date = input("Enter expiry date (MM/YY): ")
        cvv = input("Enter CVV: ")
        print(f"Card payment of ${total_price:.2f} processed successfully.")

    def payment_form_cash(self, total_price):
        print("Cash Payment Form")
        cash_amount = float(input("Enter cash amount: "))
        if cash_amount >= total_price:
            change = cash_amount - total_price
            print(f"Cash payment of ${total_price:.2f} received. Change: ${change:.2f}")
        else:
            print("Insufficient cash amount.")

    def main(self):
     while True:
        self.display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            self.services()
        elif choice == "2":
            self.rooms_menu()  # Call the rooms_menu() method instead of self.rooms()
        elif choice == "3":
            self.payment_transactions()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    h = Hotel()
    h.main()
