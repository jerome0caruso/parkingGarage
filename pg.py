
class ParkingGarage():

    def __init__(self, tickets = 50, parkingSpaces = [], currentTicket = {}, eachTicket = 0):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.eachTicket = eachTicket

    def parkingSpacelogic(self):
        for space in range(0, 50):
            self.parkingSpaces.append(space)

    def takeTicket(self):
        
        self.tickets -= 1
        print(f"Tickets left: {self.tickets}")
        if len(self.parkingSpaces) <= 1:
            print("There are no more spots left!")
        else:
            self.parkingSpaces.pop()
            print(f"taking ticket #{self.tickets + 1}")
            print(f"Parking Spaces left: {len(self.parkingSpaces)}")
            self.currentTicket[self.tickets + 1] = {'Paid': False}

    def payForParking(self):

        while True:
            payment = input("Did you enter money? Y/N: ").lower()
            if payment == 'y':
                self.eachTicket = int(input("What ticket would you like to pay for?: "))
                if self.eachTicket in self.currentTicket:
                        self.currentTicket[self.eachTicket] = {'Paid': True}
                        print(f"You ticket #{self.eachTicket} has been paid and you have 15 minutes to leave!")
                        break
                else:
                    print("That ticket is not available")    
                    return
            else:
                print("You must go back and pay please!")
            print("Please enter money!!!")

    def leaveGarage(self):
        driver_ticket = int(input("What ticket did you have?: "))
        if driver_ticket in self.currentTicket:
            if self.currentTicket[driver_ticket]["Paid"] == True:
                print("Thank you, have a nice day!")
                return True
            else:
                print("You must go back and pay please!")
        else:
            print("That ticket is not available")    
            return
                
def driver():
    possible_entries = ["take", "pay", "leave", "quit"]
    driver_1 = ParkingGarage()
    driver_1.parkingSpacelogic()
    driver_input = driver_input = input("What would you like to do? type 'take' to take a ticket, type 'pay' to pay a for parking or type 'leave' to exit the garage: ").lower().strip()
    while True:
        if driver_input == 'take':
            driver_1.takeTicket()
            driver_input = input("What would you like to do? type 'take' to take a ticket, type 'pay' to pay a for parking or type 'leave' to exit the garage: ").lower().strip()
        if  driver_input == 'pay':
            if driver_1.tickets == 50:
                print("No tickets have been taken!")
                driver_input = input("What would you like to do? type 'take' to take a ticket, type 'pay' to pay a for parking or type 'leave' to exit the garage: ").lower().strip()
            else:    
                driver_1.payForParking()
                driver_input = input("What would you like to do? type 'take' to take a ticket, type 'pay' to pay a for parking or type 'leave' to exit the garage: ").lower().strip()
        if driver_input == 'leave':
            driver_1.leaveGarage()
            driver_input = input("What would you like to do? type 'take' to take a ticket, type 'pay' to pay a for parking or type 'leave' to exit the garage: ").lower().strip()
        if driver_input == 'quit':
            break
        elif driver_input not in possible_entries:
            print("Not valid")
            driver_input = input("What would you like to do? type 'take' to take a ticket, type 'pay' to pay a for parking or type 'leave' to exit the garage: ").lower().strip()

driver()