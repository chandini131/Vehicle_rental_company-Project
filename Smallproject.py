class Vehicle:
    def __init__(self, vehicle_name, daily_rate, number_of_days):
        self.vehicle_name = vehicle_name
        self.daily_rate = daily_rate
        self.number_of_days = number_of_days

    def calculate_rent(self):
        return self.daily_rate * self.number_of_days


class Car(Vehicle):
    def __init__(self, vehicle_name, daily_rate, number_of_days, car_type):
        super().__init__(vehicle_name, daily_rate, number_of_days)
        self.car_type = car_type

    def display(self):
        print("Vehicle Name :", self.vehicle_name)
        print("Car Type     :", self.car_type)
        print("Daily Rate   :", self.daily_rate)
        print("Days         :", self.number_of_days)
        print("Total Rent   :", self.calculate_rent())
        print()


cars = [
    Car("SUV", 500, 5, "SUV"),
    Car("Sedan", 300, 4, "Sedan"),
    Car("HatchBack", 0, 3, "HatchBack")
]

while True:
    print("\n1. Display All")
    print("2. Display By Name")
    print("3. Display By Car Type")
    print("4. Display Highest Rent Car")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        for car in cars:
            car.display()

    elif choice == 2:
        name = input("Enter vehicle name: ")
        for car in cars:
            if car.vehicle_name.lower() == name.lower():
                car.display()

    elif choice == 3:
        ctype = input("Enter car type: ")
        for car in cars:
            if car.car_type.lower() == ctype.lower():
                car.display()

    elif choice == 4:
        highest = max(cars, key=lambda x: x.calculate_rent())
        print("Highest Rent Car Details")
        highest.display()

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")