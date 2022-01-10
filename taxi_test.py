from taxi import Taxi


def main():
    # TODO: Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    taxi = Taxi("Prius 1", 100)
    # TODO: Drive the taxi 40 km
    taxi.drive(40) # odo = 40, fuel = 60, current_fare_distance = 40
    # TODO: Print the taxi's details and the current fare
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")
    # TODO: Restart the meter (start a new fare) and then drive the car 100 km
    taxi.start_fare()
    # TODO: Print the details and the current fare
    print(taxi)
    print(f"Current fare after restarting: ${taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
