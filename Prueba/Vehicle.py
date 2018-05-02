import sys
import Car

class Vehicle(Car.Car):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)
