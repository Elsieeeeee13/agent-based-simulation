week9 lab
import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, grid):
        empty_patches = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]
        if empty_patches:
            new_position = random.choice(empty_patches)
            grid[self.x][self.y] = 0  # Mark the old position as empty
            self.x, self.y = new_position  # Move to new position
            grid[self.x][self.y] = 1  # Mark the new position with an agent

class World:
    def __init__(self, width, height, num_agents):
        self.grid = [[0]*width for _ in range(height)]
        self.agents = []
        for _ in range(num_agents):
            while True:
                x, y = random.randint(0, height-1), random.randint(0, width-1)
                if self.grid[x][y] == 0:  # Check if the spot is empty
                    self.grid[x][y] = 1
                    self.agents.append(Agent(x, y))
                    break

    def update(self):
        for agent in self.agents:
            agent.move(self.grid)

# Initialize world
world = World(width=5, height=5, num_agents=3)

# Simulation loop
for _ in range(10):  # Number of loops
    world.update()
