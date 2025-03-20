class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = 0
        self.travelled_distance = 0

    #Kiihdytys funktio
    def accelerate(self, speed_change):

        #Lisää kiihtyvyys
        self.cur_speed += speed_change

        #Nopeus ei ylitä maksiimi nopeus
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        #Nopeus ei ole negatiivinen
        if self.cur_speed < 0:
            self.cur_speed = 0


car = Car("ABC-123", 142) # Auton luonti

car.accelerate(30)
car.accelerate(50)
car.accelerate(70)

print(f"Current car speed is {car.cur_speed:d} km/h")

car.accelerate(-200)

print(f"Final car speed is {car.cur_speed:d} km/h")