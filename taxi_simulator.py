from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """A taxi simulator program that uses Taxi and SilverServiceTaxi
       Each time, until the users quit:
       The user should be able to choose from a list of available taxis
       They can choose how far they want to drive
       At the end of each trip, show them the trip cost and add it to their bill"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = int(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} cost you ${cost:.2f}")
                total_bill += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now: ")
    display_taxis(taxis)
