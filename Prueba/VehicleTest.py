import sys
import Car

tesla_model_s = Car.Car(4, 'electric', 5, 250)
#tesla_model_s = Car.ElectricCar(4, 5, 250)


#tesla_model_s.max_velocity = 300 # Es una variable privada

tesla_model_s.update_max_velocity = 300

print (tesla_model_s.max_velocity)

print (tesla_model_s.max_velocity)

tesla_model_s.make_noise()