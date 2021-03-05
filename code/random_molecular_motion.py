from random import choice

class RandomMotion():
    """A class to simulate random molecular motion"""
    def __init__(self, num_points=5000):
        """Initialization"""
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_motion(self):
        """The random motion"""
        while len(self.x_values) < self.num_points:
            # Decide the direction to go, and how far to go in that direction
            x_step = get_step()
            y_step = get_step()
            
            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

def get_step():
    """Method to return the random step"""
    direction = choice([-1, 1])
    distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    return direction * distance
            
            