class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")    

class ThreeDvector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k       

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")    
        
a = TwoDVector(2, 6)
a.show()       
b = ThreeDvector(7, 4, 3)
b.show()
        