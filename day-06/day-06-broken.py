import sys
import math

directions = ['^', '>', 'v', '<']

def dump_grid(grid):
    print('---------------')
    for line in grid:
        print(f'{line}')

def next_move(grid, loc) -> list[int]:

    move_dict = {
        '^': [-1, 0],
        '>': [0, 1],
        'v': [1, 0],
        '<': [0, -1]
    }

    loc_y, loc_x = loc
    if grid[loc_y][loc_x] not in directions:
        return []
    
    move = move_dict[grid[loc_y][loc_x]]
    next_dir = next_direction(grid[loc_y][loc_x])

    grid[loc_y] = grid[loc_y][:loc_x] + '+' + grid[loc_y][loc_x+1:]

    loc_y += move[0]
    loc_x += move[1]
    num_moves = 0
    while is_in_bounds(grid, [loc_y, loc_x]):
        if grid[loc_y][loc_x] == '#':
            break
        grid[loc_y] = grid[loc_y][:loc_x] + '+' + grid[loc_y][loc_x+1:]
        loc_y += move[0]
        loc_x += move[1]
        num_moves += 1

    if is_in_bounds(grid, [loc_y, loc_x]):
        loc_y -= move[0]
        loc_x -= move[1]
        grid[loc_y] = grid[loc_y][:loc_x] + next_dir + grid[loc_y][loc_x+1:]
        print(f'num_moves {num_moves}: returning {loc_y}, {loc_x}')
        return [loc_y, loc_x, num_moves]
    return []

def next_direction(current) -> str:
    return directions[(directions.index(current) + 1) % 4]


def is_in_bounds(grid, loc) -> bool:
    return loc[0] < len(grid) and loc[1] < len(grid[0]) and loc[0] >= 0 and loc[1] >= 0

def find_start(grid) -> list[int]:
    """_summary of find_start

    Args:
        grid (list): Initial grid

    Returns:
        list[int]: Location of starting token and direction

    """
    for index_y in range(len(grid)):
        for index_x in range(len(grid[0])):
            if grid[index_y][index_x] in '^>v<':
                return [index_y, index_x]
    return []


if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    grid = content.strip().split('\n')

    print(f'read {len(grid)} lines')

    start_loc = find_start(grid)
    print(f'starting_location: {start_loc}')
    grid[6] = grid[6][:3] + '#' + grid[6][4:]

    max_moves = math.factorial(max(len(grid), len(grid[0])))
    num_moves = 0
    while True:
        next = next_move(grid, start_loc)
        if len(next) == 0:
            break
        num_moves += next[2]
        print('num_moves:', num_moves)
        if num_moves > max_moves:
            print('Max moves exceeded - loop found!')
            break
        start_loc = [next[0], next[1]]
        print(f'next_move: {start_loc}')
        dump_grid(grid)

    visits = 0
    loops = 0
    print('grid:')
    for line in grid:
        visits += line.count('+')
        loops += line.count('L')
        print(f'{line}')
    print(f'Num visits: {visits+loops}, num loops: {loops}')
