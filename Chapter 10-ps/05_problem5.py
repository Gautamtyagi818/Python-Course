import random
class Train:  
    def __init__(self, trainNo): 
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"\nThe Ticket is book in train no {self.trainNo} from {fro} to {to} ")
    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    def getFare(self, fro, to):
        print(f"Ticket Fare in train no: {self.trainNo} from {fro} to {to} {random.randint(333, 5555)}")
    
a = Train(34674)
a.book("Mumbai",  "Delhi")
a.getstatus()
a.getFare("Mumbai",  "Delhi")
