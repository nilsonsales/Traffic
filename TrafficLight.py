from random import randint


class TrafficLight(object):
    def __init__(self, id, position, direction):
        self.id = id
        self.position = position
        self.direction = direction
        self.state = {str(direction[0]):'red', str(direction[1]):'green'}
        self.time = 0
        self.max_time = 3

    def where_to(self):
        print("Choosing where to go when the light is green...", end=' ')
        choice = randint(0,1)
        print(self.direction[choice])
        return self.direction[choice]

    def update_state(self):

        if self.time == self.max_time:
            dir = []

            for key in self.state.keys():
                dir.append(key)

            if len(dir) > 1:
                self.state[dir[0]], self.state[dir[1]] = self.state[dir[1]], self.state[dir[0]]

            self.time = 0
        else:
            self.time += 1
