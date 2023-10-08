import random

class WumpusWorld:
    def __init__(self, size=4, pit_prob=0.2, wumpus_prob=0.1, max_steps=10):
        self.size = size
        self.pit_prob = pit_prob
        self.wumpus_prob = wumpus_prob
        self.max_steps = max_steps
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.agent_pos = (0, 0)
        self.wumpus_pos = None
        self.pit_pos = None
        self.treasure_pos = (size - 1, size - 1)
        self.arrow = True
        self.steps = 0

        self.generate_world()

    def generate_world(self):
        for x in range(self.size):
            for y in range(self.size):
                if (x, y) == self.treasure_pos:
                    self.grid[x][y] = 'T'
                elif random.random() < self.pit_prob:
                    self.grid[x][y] = 'P'
                elif random.random() < self.wumpus_prob:
                    self.grid[x][y] = 'W'

    def get_percept(self):
        x, y = self.agent_pos
        percept = ""

        if self.grid[x][y] == 'P':
            percept += "You feel a breeze. "
        if self.grid[x][y] == 'W':
            percept += "You smell a wumpus. "
        if (x, y) == self.treasure_pos:
            percept += "You see the glitter of treasure. "

        return percept.strip()

    def move(self, action):
        x, y = self.agent_pos
        if action == "UP" and x > 0:
            self.agent_pos = (x - 1, y)
        elif action == "DOWN" and x < self.size - 1:
            self.agent_pos = (x + 1, y)
        elif action == "LEFT" and y > 0:
            self.agent_pos = (x, y - 1)
        elif action == "RIGHT" and y < self.size - 1:
            self.agent_pos = (x, y + 1)

        self.steps += 1

    def shoot(self):
        if self.arrow:
            self.arrow = False
            x, y = self.agent_pos
            if (x == self.wumpus_pos[0] and abs(y - self.wumpus_pos[1]) <= 1) or \
               (y == self.wumpus_pos[1] and abs(x - self.wumpus_pos[0]) <= 1):
                return "Wumpus killed!"
            else:
                return "Missed!"

    def is_game_over(self):
        x, y = self.agent_pos
        if (x, y) == self.treasure_pos:
            return "You found the treasure and won!"
        elif self.grid[x][y] == 'P':
            return "You fell into a pit and lost!"
        elif self.grid[x][y] == 'W':
            return "You were eaten by the wumpus and lost!"
        elif self.steps >= self.max_steps:
            return "Out of steps! Game over."

    def print_world(self):
        for x in range(self.size):
            print('+---' * self.size + '+')
            for y in range(self.size):
                print(f'| {self.grid[x][y]} ', end='')
            print('|')
        print('+---' * self.size + '+')
        print(f"Agent position: {self.agent_pos}")
        print(f"Percept: {self.get_percept()}")
        print(f"Arrows: {'Available' if self.arrow else 'None'}")
        print()

# Main loop
if __name__ == "__main__":
    wumpus_world = WumpusWorld()
    wumpus_world.print_world()

    while True:
        action = input("Enter action (UP, DOWN, LEFT, RIGHT, SHOOT, QUIT): ").upper()
        if action == "QUIT":
            break
        elif action in ["UP", "DOWN", "LEFT", "RIGHT"]:
            wumpus_world.move(action)
        elif action == "SHOOT":
            result = wumpus_world.shoot()
            print(result)
        else:
            print("Invalid action! Please try again.")

        game_result = wumpus_world.is_game_over()
        if game_result:
            print(game_result)
            break

        wumpus_world.print_world()
