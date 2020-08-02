from random import choice


class RandomWalk:
    """Class introduces random walk"""

    def __init__(self, num_points=5000):
        """Initialize random walk"""
        self.num_points = num_points

        # All random walk starts with (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all points in random walk"""

        # Walk nonstop, until lists have given length
        while len(self.x_values) < self.num_points:
            # Choose direction and distance on this direction
            x_step = self.get_step()
            y_step = self.get_step()

            # Avoid step unmoved
            if x_step == 0 and y_step == 0:
                continue

            # Calculate next point's x-y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    @staticmethod
    def get_step():
        """Calculate step vector"""
        direction = choice([1, -1])
        distance = choice(range(9))
        return direction * distance
