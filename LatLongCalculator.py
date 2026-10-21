# File: LatLongCalculator.py
# Programmer: Lillian Letiecq
# Email: lletiecq@student.cnm.edu
# Purpose: This program calculates the distance between two points on the Earth given their latitude and longitude coordinates.

from math import radians

class LatLongCalculator:
    
    def greeting(self):
        print("Welcome to the LatLong Calculator!")
        print("This program calculates the distance between two points on the Earth given their latitude and longitude coordinates.")

    def get_coordinate1(self):
        print("Please enter the coordinates for the first point:")
        lat1 = float(input("Latitude (in decimal degrees): "))
        lon1 = float(input("Longitude (in decimal degrees): "))
        return (lat1, lon1)

    def get_coordinate2(self):
        print("Please enter the coordinates for the second point:")
        lat2 = float(input("Latitude (in decimal degrees): "))
        lon2 = float(input("Longitude (in decimal degrees): "))
        return (lat2, lon2)

    def calculate_distance(self, point1, point2):
        from math import sin, cos, sqrt, atan2

        # Radius of the Earth in kilometers
        R = 6371.0

        lat1, lon1 = radians(point1[0]), radians(point1[1])
        lat2, lon2 = radians(point2[0]), radians(point2[1])

        A = sin ((lat1-lat2)/2)**2 + cos(lat1) * cos(lat2) * sin((lon1-lon2)/2)**2

        C = 2 * atan2(sqrt(A), sqrt(1-A))

        D = R * C

        return D

    def display_distance(self, D):
        print("The distance between the two locations is {} kilometers.".format(D))

    def run(self):
        self.greeting()
        point1 = self.get_coordinate1()
        point2 = self.get_coordinate2()
        distance = self.calculate_distance(point1, point2)
        self.display_distance(distance)

def setup():
    
    calculator = LatLongCalculator()
    calculator.run()

def main():
    while True:
        setup()
        setup_again = input("Would you like to calculate another distance? (yes/no): ")

        if setup_again in ("no"):
            print("Thank you for using the LatLong Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
