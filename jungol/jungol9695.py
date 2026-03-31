class Home:
    def __init__(self, location, bedrooms, bathrooms):
        self.location = location
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
    def print(self):
        #print(location, bedrooms, bathrooms)
        print(f"location: {self.location}")   
        print(f"bedrooms: {self.bedrooms}")
        print(f"bathrooms: {self.bathrooms}")

location, bedrooms, bathrooms = input().split()
#print(location,  bedrooms, bathrooms)

h1 = Home(location, bedrooms, bathrooms)
h1.print()  #이걸 써줘야 Home이 출력된다



