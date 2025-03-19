class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = 60
        self.travelled_distance = 2000

    def drive(self, hours):

        distance = self.cur_speed * hours
        self.travelled_distance += distance

car = Car("ABC-123", 142) # Auton luonti

car.drive(1.5)

print(f"kuljettu {car.travelled_distance} km")