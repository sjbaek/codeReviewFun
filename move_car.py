# Add title and descriptions on variables defined below

directions = ['N','E','S','W'] 
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}

# User input 1: define grid size
GRID_MAX_X, GRID_MAX_Y = map(int, raw_input().split())

first_vehicle_x = None
first_vehicle_y = None

# Description on Vehicle class needed?

class Vehicle():
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir = face

    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)]

    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)]

    def move(self):
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]

        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            if new_x in xrange(GRID_MAX_X+1):
                self.x = new_x
            if new_y in xrange(GRID_MAX_Y+1):
                self.y = new_y

# User input 2:
# First vehicle: The current position and facing direction for the first vehicle; 
#     X, Y and Dir are separated by space

vehicle_one_pos = raw_input().split()

# User input 3:
# The first vehicle

vehicle_one_commands = raw_input()

vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])
for command in vehicle_one_commands:
    eval("vehicle_one.{0}()".format(commands[command]))

first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y

# User input 4:
# Second vehicle: The current position and facing direction for the first vehicle; 
#     X, Y and Dir are separated by space

vehicle_two_pos = raw_input().split()

# User input 5:
# The second vehicle

vehicle_two_commands = raw_input()

vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_ps[2])
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

print vehicle_one.x, vehicle_one.y, vehicle_one.dir
print vehicle_two.x, vehicle_two.y, vehicle_two.dir

# may need to add a test for 'move' function at the end

