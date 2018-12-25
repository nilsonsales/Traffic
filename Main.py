"""
Problem: Traffic light
@author: nilsonsales
"""

import time
import os
from random import randint


from Car import Car
from TrafficLight import TrafficLight


# Cleaning the file
open('occurences.txt', 'w').close()

# Global lists
initial_car_positions = []
cars_list = []

# Defining traffic lights

lights_pos = [(0,6), (0,12), (6,0), (6,6), (6,12), (12,0), (12,6), (12,12), (12,18), (18,6), (18,12)]
lights_dir = ['ld', 'll', 'rd', 'rd', 'ru', 'dd', 'ld', 'lu', 'lu', 'rr', 'ru']
# In the traffic lights (0, 12), (12,0) and (18,6) cars can only turn to one side

traffic_light_list = []

for i in range(len(lights_dir)):
    traffic_light_list.append(TrafficLight(i, lights_pos[i], lights_dir[i]))  # Creates and adds a TrafficLight object




def build_map(size):
    # The map consists in a matrix of dictionaries with:
    # symbol (to print), direction (sense: right, left, up or down), state (if there's a car in that position)
    # direction is static! (+ means traffic light)

    # Creating 2D matrix
    matrix = [[] for line in range(size)]

    # Adding a dictionary to each position
    for line in range(size):
        for column in range(size):
            matrix[line].append({'symbol': '-', 'direction': 'o', 'state': ' ', 'id':''})


    # Filling the squares
    for i in range(size):
        for j in range(size):
            if i not in [0, 6, 12, 18] and j not in [0, 6, 12, 18]:
                matrix[i][j]['symbol'] = '#'
                matrix[i][j]['direction'] = ' '
                matrix[i][j]['state'] = 'square'


    # Filling the direction map
    for i in [0, 12]:
        for j in range(size):
            matrix[i][j]['direction'] = 'l'  # left
    for i in [6, 18]:
        for j in range(size):
            matrix[i][j]['direction'] = 'r'  # right
    for i in range(size-1):
        for j in [0, 6]:
            matrix[i][j]['direction'] = 'd'  # down
    for i in range(1, size):
        for j in [12, 18]:
            matrix[i][j]['direction'] = 'u'  # up


    # setting the traffic lights on the map
    # each traffic light has an ID
    traffic_light_positions = [(0,6), (0,12), (6,0), (6,6), (6,12), (12,0), (12,6), (12,12), (12,18), (18,6), (18,12)]
    id = 0
    for i, j in traffic_light_positions:
        matrix[i][j]['direction'] = 'x'
        matrix[i][j]['state'] = ' '
        matrix[i][j]['id'] = id
        id += 1

    return matrix


# Function to print the map. The other possible arguments are: 'state' and 'direction'
def print_map(matrix, type='symbol'): # default value
    print("Map of " + type + "\n")

    for line in range(len(matrix)):
        for column in range(len(matrix)):
            print(matrix[line][column][type] + ' ', end=" ")
        print("\n")


def update_car_position(car):
    """
        Car can move if:
        - In the next position there's not a car
        - In the next position there isn't a RED light for the side the car wants to move to
    """

    i0 = car.position[0]  # current line
    j0 = car.position[1]  # current column
    street_direction = city_map[i0][j0]['direction']  # direction of the road the car is
    traffic_light_state = ''

    print("#" + str(car.id))

    # If car is in a crossroad, it decides by itself where to go
    if street_direction == 'x':
        street_direction = car.direction
        car.direction = ''  # cleans old variable
        print("Car in crossroad! Already knows where to go")

    print("Direction: {}".format(street_direction))


    i1, j1 = car.check_next_position(street_direction)  # gets POSSIBLE new car position


    # if in next position there's a traffic light
    #  car flips a coin and saves where it wants to go
    if city_map[i1][j1]['direction'] == 'x':
        id = city_map[i1][j1]['id']  # traffic light id
        print("Traffic light in front...")

        if car.direction == '':
            car.direction = traffic_light_list[int(id)].where_to()  # car changes direction?

        # Gets traffic light state
        try:
            traffic_light_state = traffic_light_list[id].state[street_direction]
        except:
            traffic_light_state = 'green'  # if direcion not in Traffic Light dictionary


    # if there's a car in the next position, DON'T MOVE
    if (city_map[i1][j1]['state'] == 'car'):
        print("Traffic jam: Car #{} stuck in the position [{},{}]".format(str(car.id), str(i1), str(j1)))

        with open("occurences.txt", 'a') as out:
            out.write("Traffic jam: Car #{} stuck in the position [{},{}]".format(str(car.id), str(i1), str(j1)) + '\n')

    # if there's a red light in the next position, DON'T MOVE
    elif (traffic_light_state == 'red'):
        print("Red light for car #{} in the position [{},{}]".format(str(car.id), str(i1), str(j1)))

        with open("occurences.txt", 'a') as out:
            out.write("Red light for car #{} to turn to the {}".format(str(car.id), street_direction) + '\n')

    else:  # if there's no car nor red light, then actually moves the car
        i1, j1 = car.move(street_direction)

        city_map[i0][j0]['symbol'] = '-'
        city_map[i0][j0]['state'] = ' '
        city_map[i1][j1]['symbol'] = str(car.id)
        city_map[i1][j1]['state'] = 'car'


# Main function: watch all the cars and update their position every turn
def update_map(city_map, cars_list):
    #os.system('clear')
    print("Updating map...")

    for car in cars_list:
        update_car_position(car)

    print("\n")
    print_map(city_map)

    for light in traffic_light_list:
        light.update_state()
    #print_map(city_map, 'state')


def generate_car(id):
    valid_position = False
    line = column = 0

    while(not valid_position):
        line = randint(0,18)
        column = randint(0,18)

        # checks if it's a valid position
        if (city_map[line][column]['state'] != 'square') and ([line, column] not in initial_car_positions):
            valid_position = True

    print("Generated car #{} in position [{},{}]".format(id, line, column))

    return Car(id, [line, column])  # returns Car object


def generate_N_cars(n):
    print("Generating cars...")

    for i in range(n):
        if i == 0:
            id = 'A'
        else:
            id = chr(ord(cars_list[-1].id) + 1)  # Increases the char of the id

        new_car = generate_car(id)
        #line, column = new_car.position[0], new_car.position[1]
        #new_car.direction = city_map[line][column]['direction']  # in case the car is generated at a crossroad
        cars_list.append(new_car)
        initial_car_positions.append(new_car.position)


map_size = 19  # 19x19

city_map = build_map(map_size)

#print_map(city_map, 'symbol')
#print_map(city_map, 'direction')

# Add random cars
#car1 = Car('A', [0, 0])
#car2 = Car('B', [18, 18])
#car3 = Car('C', [10, 18])

#initial_car_positions.extend(([0,0],[18,18],[5,18]))

#cars_list.extend((car1, car2, car3))

generate_N_cars(20)

# updates map with the initial position of the cars
update_map(city_map, cars_list)


for iteration in range(100):

    # update map
    update_map(city_map, cars_list)

    # sleep for 2 seconds
    time.sleep(2)
