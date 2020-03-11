

# example college_func.py (functional approach)

def advertise(college):
    print(f"Welcome to {college['name'].upper()}. Your revolution starts here.")

def full_info(college):
    return f"{college['city']} {college['name']}"


if __name__ == "__main__":
    colleges = [
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
    
    for college in colleges:
        print("\n")
        print(full_info(college))
        advertise(college)