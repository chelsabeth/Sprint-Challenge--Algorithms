class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # 1st process here 👇
        self.set_light_on() # turn on robot's light
        self.swap_item() # pick up first item - spot is now None
        while self.light_is_on(): # while the light is on...
            # robot goes through each item to the right in the list
            while self.can_move_right(): # as long as robot can move right, this will persist
                self.move_right() # move right
                if self.compare_item() == 1:  # compare to see if item in list is smaller than what he is holding
                    self.swap_item() # if the item in the list is smaller, than swap the two
                # continues until cannot go right anymore
            
            # robot should now have the smallest number of that turn, now he must go left to find the None spot
            while self.compare_item() != None: # run until spot with None is replaced
                self.move_left() # move left
                if self.compare_item() is None:
                    self.swap_item() # replace None spot with the card robot is holding
                    #1st process complete
            
            # if robot can go right, skip one to the right and repeat 1st process - 2nd process here 👇
            if self.can_move_right():
                self.move_right()  # move robot right
                self.swap_item()  # swap None into list
            
            # robot cannot skip anymore to the right - 3rd process here 👇
            elif not self.can_move_right():  # if robot can't skip to the right anymore
                self.swap_item() # put item he is holding back at the None spot, which is the end
                self.set_light_off() # turn off light


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)

# 1st process:
# while robot's light is on...
# pick up first item in list, the spot is now none
# robot goes through each item to the right in the list 
# and compares to see if any item is smaller than item he is holding
# if an item is smaller than the one he is holding, swap the two
# when he cannot go right anymore, he should be holding the smallest number
# now he must turn around and go left to find the spot that is empty/None
# replace the spot with None with the card he is holding(smallest card)

# 2nd process:
# if robot can go right, skip one to the right and start there
# repeat 1st session

# 3rd process: 
# when robot cannot skip to the right anymore
# put the item he is holding back in the spot with None
# and turn off his light

# Jamboard with drawing: https://jamboard.google.com/d/1XiCaVSCCzToYhM_8z8EwYNoJKEQ-sE4OOCIxaYnkIiU/edit?usp=sharing