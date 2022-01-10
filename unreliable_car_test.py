from unreliable_car import UnreliableCar


def main():
    """Test cars"""
    good_car = UnreliableCar("Prius 1", 100, 99)
    bad_car = UnreliableCar("Prius 2", 100, 10)
    for i in range(1, 5):
        print(f"Drive distance: {i}km")
        print(f"{good_car.name:10} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:10} drove {bad_car.drive(i):2}km")

    print(good_car)
    print(bad_car)


if __name__ == '__main__':
    main()
