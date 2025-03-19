class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123", 142) # Auton luonti

print(f"\nCar registration number is {car.reg_number:s}")
print(f"Maximum speed is {car.max_speed:d} km/h.")
print(f"Current speed is {car.cur_speed:d} km/h")
print(f"Travelled distance is {car.travelled_distance} km" )