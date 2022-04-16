class Driver():
    def __init__(self, name):
        self.name = name
        
    def take_ticket(self,tickets,spaces):
        tickets.pop()
        spaces.pop()
        print("Welcome! Please proceed to parking lot :)")
        print(f"There are {tickets[-1]} remaining tickets and {spaces[-1]} remaining spaces")
        
    def pay_for_parking(self, current_ticket):
        current_ticket["Paid"] = True
        print(current_ticket)
        print("Payment processed! You have 15 minutes to exit, hope you had an amazing time :)")
        
    def leave_garage(self, tickets, spaces):
        tickets.append(tickets[-1]+1)
        spaces.append(spaces[-1]+1)
        print("Thank you, see you next time! :)")
        print(f"There are {tickets[-1]} remaining tickets and {spaces[-1]} remaining spaces")
        
        
        
class ParkingGarage():
    def __init__(self, driver, tickets=[1,2,3,4,5,6,7,8,9,10], spaces =[1,2,3,4,5,6,7,8,9,10], current_ticket = {"Paid" : False}):
        self.driver = driver
        self.tickets = tickets
        self.spaces = spaces
        self.current_ticket = current_ticket

    def parking_garage(self, tickets = [1,2,3,4,5,6,7,8,9,10], spaces = [1,2,3,4,5,6,7,8,9,10], current_ticket = {"Paid" : False}):
        while True:
            name = input("What is your name? ")
            response = input(f"Hi {name}! Would you like to take a ticket [y or n]? ").strip()
            if response.lower() == "n":
                print("Okay, have a nice day!")
                break

            if response.lower() == "y":
                self.driver.take_ticket(tickets,spaces)
                break

            else:
                print("Invalid response")

        while True:
            if response.lower() == "n":
                break
            else:
                amount = float(input("Hope you had a great time! Please enter the amount to pay [ex. 3.00]: $"))
                if not amount:
                    print("INVALID AMOUNT: You must enter more than $0!")
                else:
                    self.driver.pay_for_parking(current_ticket)
                    break

        while True:
            if response.lower() == "n":
                break
            else:
                action = input(f"Hi again {name}! Would you like to leave [y or n]? ").strip()
                if action.lower() == "n":
                    print("Okay, keep having fun!")

                elif action.lower() == "y":
                    self.driver.leave_garage(tickets,spaces)
                    break
                else:
                    print("Invalid response")
                


trey = Driver("Trey")
driver1 = ParkingGarage(trey)
driver1.parking_garage()