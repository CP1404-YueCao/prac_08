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
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
   