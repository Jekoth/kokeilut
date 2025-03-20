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

class Race:
    def __init__(self, name, kilometers, cars):
        self.name = name
        self.kilometers = kilometers
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)  # 1 tuntia

    #Tulostaa kaikkien autojen nykyhetki tulokset taulukkoon
    def print_status(self):
        print(f"\nRace: {self.name}\nDistance: {self.kilometers} km")
        print(f"{'Reg Number':<10} {'Max Speed':<10} {'Cur Speed':<10} {'Distance':<10}")
        print("-" * 40)
        for car in self.cars:
            print(f"{car.reg_number:<10} {car.max_speed:<10} {car.cur_speed:<10} {car.travelled_distance:<10}")
    #Tarkistaa onko kilpailu loppunut
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.kilometers:
                return True
        return False

if __name__ == "__main__":
    car_list = []
    for i in range(10):
        reg_number = f"ABC-{i + 1:03}"
        max_speed = random.randint(100, 200)
        new_car = Car(reg_number, max_speed)
        car_list.append(new_car)


    grand_demolition_derby = Race("Grand Demolition Derby", 8000, car_list)

    hours_passed = 0

    #Simuloi auto kilpailua
    while not grand_demolition_derby.race_finished():
        grand_demolition_derby.hour_passes()
        hours_passed += 1
        #Tulosta tilanne joka 10 tunti
        if hours_passed % 10 == 0:
            grand_demolition_derby.print_status()

    #Tulosta lopullinen kisan tulot
    grand_demolition_derby.print_status()
    print(f"\nThe race is finished after {hours_passed} hours!")
