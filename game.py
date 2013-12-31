
class World:

    WALL = 'x'
    WATER = '~'
    STAR = 's'
    FIELD = 'o'

    OBSTACLES = [WALL, WATER]

    start = (0, 0)

    map = [ ['o', 'o', 'o', 'o', 's'],
            ['o', 'o', 'o', 'o', 'x'],
            ['o', 'o', 'o', 'o', 'x'],
            ['o', 'o', 'o', 'o', 'x'],
            ['o', 'o', 'o', 'o', 'o'] ]


    def __str__(self):
        return "\n".join([" ".join(line) for line in self.map])

    def get_element(self, position):
        return self.map[position[1]][position[0]]

    def set_element(self, position, element):
        self.map[position[1]][position[0]] = element

    def is_solved(self):
        return all([all([e != 's' for e in line]) for line in self.map])


worlds = {
    '1': World
}


class Player:

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def __init__(self, Map):
        world = Map()

        self.position = world.start[:]
        self.world = world

    def _move(self, step):
        if step == Player.UP:
            position = (self.position[0], self.position[1] - 1)
        elif step == Player.DOWN:
            position = (self.position[0], self.position[1] + 1)
        elif step == Player.RIGHT:
            position = (self.position[0] + 1, self.position[1])
        elif step == Player.LEFT:
            position = (self.position[0] - 1, self.position[1])
        else:
            assert False

        if not(0 <= position[0] < len(self.world.map[0])):
            return False
        if not(0 <= position[1] < len(self.world.map)):
            return False

        if self.world.get_element(position) in World.OBSTACLES:
            return False

        if self.world.get_element(position) == World.STAR:
            self.world.set_element(position, World.FIELD)

        self.position = position

        self.world.is_solved()

        return True

    def up(self):
        self._move(Player.UP)

    def right(self):
        self._move(Player.RIGHT)

    def down(self):
        self._move(Player.DOWN)

    def left(self):
        self._move(Player.LEFT)


class Game:

    def __init__(self, world, script):
        self.player = Player(world)
        self.world = world
        self.script = script

        exec(self.script, {}, {
            'world': self.world,
            'guy': self.player,
        })

