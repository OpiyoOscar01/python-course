class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand       # attribute
        self.model = model       # attribute
        self.battery = battery   # attribute (%)

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"{self.brand} {self.model} charged to {self.battery}%.")

# Create objects
phone1 = Smartphone("Apple", "iPhone 14", 50)
phone2 = Smartphone("Samsung", "Galaxy S23", 30)

# Use methods
phone1.make_call("123-456-7890")  # Calling 123-456-7890 from Apple iPhone 14...
phone2.charge(40)                 # Samsung Galaxy S23 charged to 70%.
