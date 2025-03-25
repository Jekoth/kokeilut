class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.cur_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.cur_speed += speed_change

        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        if self.cur_speed < 0:
            self.cur_speed = 0

    def drive(self, hours):
        distance = self.cur_speed * hours
        self.travelled_distance += distance

class Sahkoauto(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
        Car.__init__(self, reg_number, max_speed)
        self.battery_capacity = battery_capacity#akkukapasiteetti kwh

class Polttomoottoriauto(Car):
    def __init__(self, reg_number, max_speed, tank_capacity):
        Car.__init__(self, reg_number, max_speed)
        self.tank_capacity = tank_capacity #bensatankin koko litroina

if __name__ == "__main__":
    #uusi sähköauto ja polttomoottoriauto
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    #Asetetaan nopeudet
    sahkoauto.accelerate(180) #Kiihdytetään täyteen nopeuteen
    polttomoottoriauto.accelerate(165)#Kiihdytetään täyteen nopeuteen

    #kuinka pitkään autot ajavat
    sahkoauto.drive(3)
    polttomoottoriauto.drive(3)

    #Tulostetaan matkamittarilukemat
    print(f"{sahkoauto.reg_number} matkaa: {sahkoauto.travelled_distance:.2f} km")
    print(f"{polttomoottoriauto.reg_number} matkaa: {polttomoottoriauto.travelled_distance:.2f} km")