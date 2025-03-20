class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.cur_floor = 0

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Floor {target_floor} is out of range!")
            return

        while self.cur_floor < target_floor:
            self.floor_up()

        while self.cur_floor > target_floor:
            self.floor_down()

    #Funktion that moves elevator up
    def floor_up(self):
        if self.cur_floor < self.top_floor:
            self.cur_floor += 1
            print(f"Going up: Current floor number is {self.cur_floor}")
        else:
            print("Already at the top floor!")

    #Funktion that moves elevator down
    def floor_down(self):
        if self.cur_floor > self.bottom_floor:
            self.cur_floor -= 1
            print(f"Going down: Current floor number is {self.cur_floor}")
        else:
            print("Already at the bottom floor!")

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(number_of_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(f"Elevator number {elevator_number} is out of range.")
            return

        print(f"Running Elevator {elevator_number} to floor {destination_floor}...")
        self.elevators[elevator_number - 1].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Fire alarm activated! Moving all elevators to the bottom floor...")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)

if __name__ == "__main__":
    #Create a Building with bottom floor 0, top floor 10, and 3 elevators
    building = Building(0, 10, 3)

    #Move elevator 1 to floor 5
    building.run_elevator(1, 5)

    #Move elevator 2 to floor 3
    building.run_elevator(2, 3)

    #Move elevator 3 to a floor out of range
    building.run_elevator(3, 12)

    #Return elevator 1 to the bottom floor
    print("Returning Elevator 1 to the bottom floor...")
    building.run_elevator(1, 0)

    #Move elevator 1 to floor 10
    building.run_elevator(1, 10)

    #Call fire alarm
    building.fire_alarm()