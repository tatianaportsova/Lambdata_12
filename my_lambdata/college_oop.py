import pandas
# colleges (OOP)


class College():

    def __init__(self, name=None, city=None, state=None, funding=None):
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

    colleges_dict = [
        {"city": "New York", "state": "NY",
         "funding": "Private, non-profit", "name": "Columbia University"},
        {"city": "New York", "state": "NY",
         "funding": "Private, non-profit", "name": "New York University"},
        {"city": "New York", "state": "NY",
         "funding": "Private, non-profit", "name": "Barnard College"},
        {"city": "New York", "state": "NY",
         "funding": "Public", "name": "Baruch College"},
        {"city": "New York", "state": "NY",
         "funding": "Private, non-profit", "name": "Fordham University"}
    ]

    for college_d in colleges_dict:
        college == College(college_d["name"], college_d["city"],
                           college_d["state"], college_d["funding"])
        print(college.name)
        print(college.funding)
        print(college.full_info)
        print(college.advertise_generically())
        print("*----*----*")
