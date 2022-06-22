import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._second_segments = []
        self._prepare_body()
        self._prepare_second_snake_body()
        self.color_head()


    def get_segments(self):
        return self._segments

    def get_second_snake_segments(self):
        return self._second_segments


    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        for second_segment in self._second_segments:
            second_segment.move_next()

        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

        for i in range(len(self._second_segments) - 1, 0, -1):
            trailing = self._second_segments[i]
            previous = self._second_segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        
        return self._segments[0]
    
    def get_second_snake_head(self):
        return self._second_segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)
        

    def grow_second_snake_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._second_segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            
            second_segment = Actor()
            second_segment.set_position(position)
            second_segment.set_velocity(velocity)
            second_segment.set_text("0")
            second_segment.set_color(constants.YELLOW)
            self._second_segments.append(second_segment)


    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
        self._second_segments[0].set_velocity(velocity)

    def color_head(self):
         self._segments[0].set_color(constants.RED)
         self._second_segments[0].set_color(constants.RED)
       
    
    def _prepare_body(self):
        x = int(constants.MAX_X/2)
        y = int(constants.MAX_Y/4 )
        

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def _prepare_second_snake_body(self):
       x = int(constants.MAX_X/2)
       y = int(constants.MAX_Y /2)

       for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "0"
            color =  constants.YELLOW
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._second_segments.append(segment)