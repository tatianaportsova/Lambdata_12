
# colleges (OOP)

class College():
    def __init__(self, name, city, state, funding):
        self.name = name
        self.city = city
        self.state = state
        self.funding = funding
    
    
    def __str__(self):
        return f"<College {self.city} {self.name}>"
    
    def __repr__(self):
        return f"<College {self.city} {self.name}>"
   
    @property
    def full_info(self):
        return f"{self.city} {self.state} {self.funding} {self.name}"
    
    def advertise(self):
        print(f"Welcome to {self.city.upper()}. Your revolution starts here.")
   
    @staticmethod
    def advertise_generically():
        print("WELCOME!")

if __name__ == "__main__":
    college = College("Baruch College", "New York", "NY", "Public") 
    print(college.full_info)
    #college2 = College("Yankees", "New York")
    #print(college2.full_name)