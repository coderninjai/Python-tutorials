# Lets learn the constructor

class person:
    
    def __init__(self,n,o):
        print("This is a person ")
        self.name=n
        self.occ=o
    
    # name="tony"
    # occ= "Developer"
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=person(self,"divya","senior dev")
a.info()

# a.name="divya"
# a.occ="senior dev"
# a.info()