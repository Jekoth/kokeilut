class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.cur_floor = 0

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Floor is out of range!")
            return

        while self.cur_floor < target_floor:
            self.floor_up()

        while self.cur_floor > target_floor:
            self.floor_down()

    def floor_up(self):
        if self.cur_floor < self.top_floor:
            self.cur_floor += 1
            print(f"Going up: Current floor number is {self.cur_floor}")
        else:
            print("Already at the top floor!")

    def floor_down(self):
        if self.cur_floor > self.bottom_floor:
            self.cur_floor -= 1
            print(f"Going down: Current floor number is {self.cur_floor}")
        else:
            print("Already at the bottom floor!")