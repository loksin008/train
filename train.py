import csv

# Sample train database (can also be stored in a CSV file)
train_data = [
    {"number": "12345", "name": "Express Train", "origin": "City A", "destination": "City B", "departure": "09:00", "arrival": "17:00"},
    {"number": "54321", "name": "Superfast Train", "origin": "City C", "destination": "City D", "departure": "13:00", "arrival": "21:00"},
    {"number": "67890", "name": "Intercity Express", "origin": "City E", "destination": "City F", "departure": "06:00", "arrival": "14:00"},
]

def load_train_data_from_csv(filename):
    """Load train data from a CSV file."""
    data = []
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print("CSV file not found. Using default train data.")
        data = train_data  # Fall back to default data
    return data

def search_by_train_number(trains, number):
    """Search for a train by its number."""
    for train in trains:
        if train["number"] == number:
            return train
    return None

def search_by_route(trains, origin, destination):
    """Search for trains by origin and destination."""
    result = [train for train in trains if train["origin"] == origin and train["destination"] == destination]
    return result

def display_train_info(train):
    """Display information for a single train."""
    print(f"\nTrain Number: {train['number']}")
    print(f"Train Name: {train['name']}")
    print(f"Origin: {train['origin']}")
    print(f"Destination: {train['destination']}")
    print(f"Departure: {train['departure']}")
    print(f"Arrival: {train['arrival']}\n")

def main():
    print("Welcome to the Train Enquiry System")
    trains = load_train_data_from_csv('train_data.csv')  # Load train data from CSV

    while True:
        print("1. Search by Train Number")
        print("2. Search by Route")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            number = input("Enter train number: ")
            train = search_by_train_number(trains, number)
            if train:
                display_train_info(train)
            else:
                print("Train not found.")

        elif choice == "2":
            origin = input("Enter origin station: ")
            destination = input("Enter destination station: ")
            route_trains = search_by_route(trains, origin, destination)
            if route_trains:
                print(f"\nTrains between {origin} and {destination}:")
                for train in route_trains:
                    display_train_info(train)
            else:
                print("No trains found for this route.")

        elif choice == "3":
            print("Exiting Train Enquiry System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
