from Prac8.taxi import Taxi
from Prac8.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit c)hoose taxi, d)rive"


def main():
    """ Taxi driving simulator. Use class Taxi and SilverServiceTaxi"""
    total_bill = 0
    taxis = [Taxi("Prius", 100, 5), SilverServiceTaxi("Limo", 100, 2, 9), SilverServiceTaxi("Hummer", 200, 4, 9)]
    current_taxi = None
    print("Let's Drive")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                         trip_cost))
            total_bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


if __name__ == '__main__':
    main()
