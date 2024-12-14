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
    # print(f'next_move: grid[{loc_y},{loc_x}] {grid[loc_y][loc_x]}')
    if grid[loc_y][loc_x] not in directions:
        return []
    
    current_dir = grid[loc_y][loc_x]
    move = move_dict[grid[loc_y][loc_x]]
    next_dir = next_direction(grid[loc_y][loc_x])

    grid[loc_y] = grid[loc_y][:loc_x] + current_dir + grid[loc_y][loc_x+1:]

    loc_y += move[0]
    loc_x += move[1]
    num_moves = 0
    while is_in_bounds(grid, [loc_y, loc_x]):
        if grid[loc_y][loc_x] == '#' or grid[loc_y][loc_x] == 'O':
            break
        if grid[loc_y][loc_x] == current_dir:
            return [-1, -1, 0, 0]
        grid[loc_y] = grid[loc_y][:loc_x] + current_dir + grid[loc_y][loc_x+1:]
        loc_y += move[0]
        loc_x += move[1]
        num_moves += 1

    if is_in_bounds(grid, [loc_y, loc_x]):
        loc_y -= move[0]
        loc_x -= move[1]
        grid[loc_y] = grid[loc_y][:loc_x] + next_dir + grid[loc_y][loc_x+1:]
        direction = 90

        # lookahead to see if we can move
        move = move_dict[grid[loc_y][loc_x]]
        next_dir = next_direction(grid[loc_y][loc_x])
        if grid[loc_y+move[0]][loc_x+move[1]] == '#' or grid[loc_y+move[0]][loc_x+move[1]] == 'O':
            grid[loc_y] = grid[loc_y][:loc_x] + next_dir + grid[loc_y][loc_x+1:]
            direction = 180

        print(f'num_moves {num_moves}: returning {loc_y}, {loc_x} [{current_dir}]')
        return [loc_y, loc_x, direction, num_moves]
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
    grid_orig = grid.copy()

    start_loc_orig = find_start(grid)
    print(f'starting_location: {start_loc_orig}')
    # grid[6] = grid[6][:3] + 'O' + grid[6][4:]

    loops = 0
    for loop_y in range(0, len(grid)):
        print('\n', flush=True)
        count=0
        one_eighty = False
        for loop_x in range(0, len(grid[0])):
            grid = grid_orig.copy()
            start_loc = start_loc_orig
            # loop_y = 43
            # loop_x = 42
            print (f'target at: {loop_y}, {loop_x}')
            grid[loop_y] = grid[loop_y][:loop_x] + 'O' + grid[loop_y][loop_x+1:]
            ones_count = 0
            while True:
                next = next_move(grid, start_loc)
                # print(f'next is {next}')
                if len(next) == 0:
                    break
                if next[0] == -1 and next[1] == -1:
                    loops += 1
                    print(f'Loop found: {loop_y}, {loop_x}', flush=True)
                    break
                if next[2] == 180:
                    if one_eighty is True:
                        print(f'180 found -- loop!: {loop_y}, {loop_x}', flush=True)
                        loops += 1
                        break
                    one_eighty = True
                else:
                    one_eighty = False
                if next[3] == 1:
                    if ones_count == 3:
                        print(f'3 ones found -- loop!: {loop_y}, {loop_x}', flush=True)
                        loops += 1
                        break
                    ones_count += 1
                else:
                    ones_count = 0

                start_loc = [next[0], next[1]]
                # print(f'next_move: {start_loc}')
                dump_grid(grid)
                count += 1
                if count % 1000 == 0:
                    print('.', end='', flush=True)

    print(f'Num loops: {loops}')
