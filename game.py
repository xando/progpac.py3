class World:

    WALL = 'x'
    WATER = '~'

    OBSTACLES = [WALL, WATER]

    start = (0, 0)

    map = [ ['o', 'o', 'o', 'o', 'x'],
            ['o', 'o', 'o', 'o', 'x'],
            ['o', 'o', 'o', 'o', 'x'],
            ['o', 'o', 'o', 'o', 'x'],
            ['o', 'o', 'o', 'o', 'o'] ]

    def __str__(self):
        return "\n".join([" ".join(line) for line in self.map])


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

        if self.world.map[position[1]][position[0]] in World.OBSTACLES:
            return False

        self.position = position

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


if __name__ == "__main__":

    script = """
guy.down()
guy.right()
print(world)
print(guy.position)
    """

    Game(World, script)
