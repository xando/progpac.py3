from game import World, Player


class TestWorldEmpty(World):

    start = (1, 1)

    map = [['o', 'o', 'o'],
           ['o', 'o', 'o'],
           ['o', 'o', 'o']]


def test_move_valid_1():

    player = Player(TestWorldEmpty)
    player.up()

    assert player.position == (1, 0)

    player = Player(TestWorldEmpty)
    player.right()

    assert player.position == (2, 1)

    player = Player(TestWorldEmpty)
    player.down()

    assert player.position == (1, 2)

    player = Player(TestWorldEmpty)
    player.left()

    assert player.position == (0, 1)


def test_move_valid_2():

    player = Player(TestWorldEmpty)
    player.up()
    player.right()

    assert player.position == (2, 0)


def test_move_valid_3():

    player = Player(TestWorldEmpty)

    player.up()
    player.up()
    player.up()

    assert player.position == (1, 0)

    player = Player(TestWorldEmpty)

    player.left()
    player.left()
    player.left()

    assert player.position == (0, 1)


class TestWorld(World):

    start = (0, 0)

    map = [['o', 'x'],
           ['~', 'x']]


def test_move_obstacle():

    player = Player(TestWorld)
    player.down()

    assert player.position == (0, 0)

    player = Player(TestWorld)
    player.right()

    assert player.position == (0, 0)


class TestWorldStarts(World):

    start = (0, 0)

    map = [['o', 's'],
           ['s', 's']]


def test_collect_starts():

    player = Player(TestWorldStarts)

    assert not player.world.is_solved()

    player.down()
    player.right()
    player.up()

    assert player.world.is_solved()
