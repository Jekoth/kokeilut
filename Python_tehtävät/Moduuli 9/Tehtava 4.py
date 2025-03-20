import random

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
        if self.cur_speed > self.max_speed:#Jos nykyinen nopeus ylittää maksimi nopeuden
            self.cur_speed = self.max_speed#Nykyinen nopeus on maksimi nopeus
        #Nopeus ei ole negatiivinen
        if self.cur_speed < 0:#Jos nykyinen nopeus on negatiivinen
            self.cur_speed = 0#Nykyinen nopeus on 0

    def drive(self, hours):

        distance = self.cur_speed * hours#Matka on nopeus kertaa aika
        self.travelled_distance += distance#Liikuttu matkaan plussataan aika


car = Car("ABC-123", 142) # Auton luonti

car_list = []#luodaan auto lista


#Auto lisätään randomisoiduilla arvoilla listaan
for i in range(10):
    car.reg_number = f"ABC-{i+1:03}"#Luodaan registeri numerot
    car.max_speed = random.randint(100,200)
    new_car = Car(car.reg_number, car.max_speed)#Luo uuden auton, joka saa omat arvot
    car_list.append(new_car)#lisätään listaan se uusi auto

race_finished = False

while not race_finished:
    for car in car_list:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True
            break

print(f"{'Reg Number':<10} {'Max Speed':<10} {'Cur Speed':<10} {'Distance':<10}")
print("-" * 40)

for car in car_list:
    print(f"{car.reg_number:<10} {car.max_speed:<10} {car.cur_speed:<10} {car.travelled_distance:<10}")