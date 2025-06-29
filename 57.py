class person:
    name="Tony Stark "
    occupation="MIT Engineer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
        
a=person()
a.occupation="pro gamer"
a.info()