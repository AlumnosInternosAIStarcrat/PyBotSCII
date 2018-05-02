class Car:
    
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self._maximum_velocity = maximum_velocity # Es una variable privada

    @property
    def number_wheels(self):
        return self.number_of_wheels

    @number_wheels.setter
    def number_wheels(self, number):
        self.number_of_wheels = number

    @property
    def type_tank(self):
        return self.type_of_tank

    @type_tank.setter
    def type_tank(self, tank):
        self.type_of_tank = tank

    @property
    def seating_cap(self):
        return self.seating_capacity

    @seating_cap.setter
    def seating_cap(self, seat):
        self.seating_capacity = seat
    
    @property
    def max_velocity(self):
        return self._maximum_velocity

    ''''@max_velocity.setter
    def max_velocity(self, max):
        self.maximum_velocity = max''' #Como es una variable privada, tiene un setter diferente

    @max_velocity.setter
    def update_max_velocity(self, max):
        self._maximum_velocity = max

    def make_noise(self):
        print('BRUUUUUUUM')