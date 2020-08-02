from random import choice


class RandomWalk:
    """Class introduces random walk"""

    def __init__(self, num_points=5000):
        """Initialize random walk"""
        self.num_points = num_points

        # All random walk starts with (0, 0)
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """Calculate all points in random walk"""

        # Walk nonstop, until lists have given length
        while len(self.x_value) < self.num_points:
            # Choose direction and distance on this direction
            x_direction = choice([1, -1])
            x_distance = choice(range(5))
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice(range(5))
            y_step = y_direction * y_distance

            # Avoid step unmoved
            if x_step == 0 and y_step == 0:
                continue

            # Calculate next point's x-y values
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)
