class calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"the square is {self.n**2}")
    def cube(self):
        print(f"the cube is {self.n**3}")
    def square_root(self):
        print(f"the square_root is {self.n**1/2}")


a = calculator(4)   
a.square() 
a.cube()  
a.square_root()
        