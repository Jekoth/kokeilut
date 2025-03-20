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


if __name__ == "__main__":
    #Made floors 0-5
    elevator = Elevator(0, 5)

    #Moving elevator to floor 5
    target_floor = 5
    print(f"Moving to floor {target_floor}...")
    elevator.go_to_floor(target_floor)

    #Moving elevator back to 0
    print("Returning to the bottom floor...")
    elevator.go_to_floor(0)