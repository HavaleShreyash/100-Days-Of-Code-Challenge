MOD = 1000000007

class LegoBlocks:
    def __init__(self, brick_count, wall_height):
        """
        Initializes the LegoBlocks class with the number of brick types and the wall height.

        Args:
        brick_count (int): The number of types of Lego bricks available.
        wall_height (int): The height of the wall to be built.
        """
        self.brick_count = brick_count
        self.wall_height = wall_height
        self.dp_table = [-1] * (wall_height + 1)
        self.brick_arrangement = [-1] * (wall_height + 1)
        self.fill_brick_arrangement(wall_height)
        
        for i in range(wall_height + 1):
            res = 1
            for j in range(brick_count):
                res = (res * self.brick_arrangement[i]) % MOD
            self.brick_arrangement[i] = res

    def fill_brick_arrangement(self, height):
        """
        Fills the brick_arrangement list with the number of ways to arrange bricks for each height.

        Args:
        height (int): The height of the wall to be built.
        """
        if height < 0:
            return 0
        if self.brick_arrangement[height] == -1:
            if height == 0:
                self.brick_arrangement[height] = 1
            else:
                self.brick_arrangement[height] = (
                    self.fill_brick_arrangement(height - 1) + 
                    self.fill_brick_arrangement(height - 2) +
                    self.fill_brick_arrangement(height - 3) +
                    self.fill_brick_arrangement(height - 4)
                ) % MOD
        return self.brick_arrangement[height]

    def evaluate_wall_building(self):
        """
        Evaluates the number of ways to build a wall of a specific height using Lego bricks.

        Returns:
        int: The number of ways to build the wall.
        """
        result = self.helper_wall_building(self.wall_height)
        return result

    def helper_wall_building(self, height):
        """
        Helper function to find the number of ways to build a wall of a specific height.

        Args:
        height (int): The height of the wall to be built.

        Returns:
        int: The number of ways to build the wall.
        """
        if self.dp_table[height] == -1:
            if height == 1:
                self.dp_table[height] = 1
            else:
                self.dp_table[height] = self.brick_arrangement[height]
                for i in range(1, height):
                    self.dp_table[height] = (
                        self.dp_table[height] - self.helper_wall_building(height - i) * self.brick_arrangement[i]
                    ) % MOD
                if self.dp_table[height] < 0:
                    self.dp_table[height] += MOD
        return self.dp_table[height]

if __name__ == "__main__":
    brick_types = int(input())
    wall_height = int(input())
    lego_blocks = LegoBlocks(brick_types, wall_height)
    print(lego_blocks.evaluate_wall_building())

# Sample Input:
# 2
# 3
# Sample Output:
# 3