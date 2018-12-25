import copy


class Car(object):
    def __init__(self, id, position):  # position [linha, coluna]
        self.id = id
        self.position = position
        self.direction = ''

    def check_next_position(self, direction):
        new_position = copy.deepcopy(self.position)

        if direction == 'r':
            new_position[1] += 1
        elif direction == 'l':
            new_position[1] -= 1
        elif direction == 'u':
            new_position[0] -= 1
        elif direction == 'd':
            new_position[0] += 1

        if new_position[0] < 0 or new_position[1] < 0:
            print("CAR OUT OF THE MAP")

        return new_position

    def move(self, direction):
        print("[current car position] = ", str(self.position))

        if direction == 'r':
            self.position[1] += 1
        elif direction == 'l':
            self.position[1] -= 1
        elif direction == 'u':
            self.position[0] -= 1
        elif direction == 'd':
            self.position[0] += 1


        print("[new car position] = ", str(self.position))
        return self.position


    # if next position no car

    # if next position traffic light is green
        # joga moeda pra saber se muda de direçao