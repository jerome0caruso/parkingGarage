
class ParkingGarage():

    def __init__(self, tickets = 50, parkingSpaces = [], currentTicket = {}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def parkingSpacelogic(self):
        for space in range(0, 50):
            self.parkingSpaces.append(space)

    def takeTicket(self):
        
        self.tickets -= 1
        print(f"Tickets left: {self.tickets}")
        if len(self.parkingSpaces) <=1:
            print("There are no more spots left!")
        else:
            self.parkingSpaces.pop()
            print("taking ticket")
            print(f"Parking Spaces left: {len(self.parkingSpaces)}")

    def payForParking(self):
        print("You are paying")
        pass

    def leaveGarage(self):
        print("Bye you are exiting!")
        pass

def driver():
    driver_1 = ParkingGarage()
    driver_1.parkingSpacelogic()
    driver_input = input("What would you like to do? type 'take' to take a ticket, type 'pay' to pay a for parking or type 'leave' to exit the garage: ").lower().strip()
    while True:
        if driver_input == 'take':
            driver_1.takeTicket()
            driver_input = input("What would you like to do? type 'take' to take a ticket, type 'pay' to pay a for parking or type 'leave' to exit the garage: ").lower().strip()
        if driver_input == 'pay':
            driver_1.payForParking()
            driver_input = input("What would you like to do? type 'take' to take a ticket, type 'pay' to pay a for parking or type 'leave' to exit the garage: ").lower().strip()
        if driver_input == 'leave':
            driver_1.leaveGarage()
            driver_input = input("What would you like to do? type 'take' to take a ticket, type 'pay' to pay a for parking or type 'leave' to exit the garage: ").lower().strip()
        if driver_input == 'quit':
            break

driver()