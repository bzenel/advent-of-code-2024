import sys
import itertools

antenna_dict: dict[str,list]= {
}

def dump_grid(grid):
    print('---------------')
    for line in grid:
        print(f'{line}')

def is_in_bounds(grid, loc) -> bool:
    return loc[0] < len(grid) and loc[1] < len(grid[0]) and loc[0] >= 0 and loc[1] >= 0

def count_char(grid, char) -> int:
    count = 0
    for line in grid:
        count += line.count(char)
    return count

def find_antennas(grid):
    for index_y in range(len(grid)):
        for index_x in range(len(grid[0])):
            val = grid[index_y][index_x]
            if val == '.':
                continue
            if val not in antenna_dict:
                antenna_dict[val] = [[index_y, index_x]]
            else:
                antenna_dict[val].append([index_y, index_x])
    print(f'antenna_dict: {antenna_dict}')
    return       

def find_antinodes(grid, anti_grid, ant_pair):
    delta_y = ant_pair[0][0] - ant_pair[1][0]
    delta_x = ant_pair[0][1] - ant_pair[1][1]
    antinode_1 = [ant_pair[0][0] + delta_y, ant_pair[0][1] + delta_x]
    antinode_2 = [ant_pair[1][0] - delta_y, ant_pair[1][1] - delta_x]
    if is_in_bounds(anti_grid, antinode_1):
        anti_grid[antinode_1[0]] = anti_grid[antinode_1[0]][:antinode_1[1]] + '#' + anti_grid[antinode_1[0]][antinode_1[1]+1:]
    if is_in_bounds(anti_grid, antinode_2):
        anti_grid[antinode_2[0]] = anti_grid[antinode_2[0]][:antinode_2[1]] + '#' + anti_grid[antinode_2[0]][antinode_2[1]+1:]
    return

def find_antinodes_v2(grid, anti_grid, ant_pair):
    delta_y = ant_pair[0][0] - ant_pair[1][0]
    delta_x = ant_pair[0][1] - ant_pair[1][1]

    anti_grid[ant_pair[0][0]] = anti_grid[ant_pair[0][0]][:ant_pair[0][1]] + '#' + anti_grid[ant_pair[0][0]][ant_pair[0][1]+1:]
    anti_grid[ant_pair[1][0]] = anti_grid[ant_pair[1][0]][:ant_pair[1][1]] + '#' + anti_grid[ant_pair[1][0]][ant_pair[1][1]+1:]
    ant_1 = ant_pair[0]

    while True:
        ant_1 = [ant_1[0] + delta_y, ant_1[1] + delta_x]
        if is_in_bounds(anti_grid, ant_1):
            anti_grid[ant_1[0]] = anti_grid[ant_1[0]][:ant_1[1]] + '#' + anti_grid[ant_1[0]][ant_1[1]+1:]
        else:
            break
    ant_2 = ant_pair[1]
    while True:
        ant_2 = [ant_2[0] - delta_y, ant_2[1] - delta_x]
        if is_in_bounds(anti_grid, ant_2):
            anti_grid[ant_2[0]] = anti_grid[ant_2[0]][:ant_2[1]] + '#' + anti_grid[ant_2[0]][ant_2[1]+1:]
        else:
            break
    return

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
    anti_grid = grid.copy()

    print(f'read {len(grid)} lines')
    dump_grid(grid)
    find_antennas(grid)
    for key in antenna_dict:
        for pair in itertools.combinations(antenna_dict[key], 2):
            find_antinodes(grid, anti_grid, pair)
    dump_grid(anti_grid)
    print(f'Num antinodes: {count_char(anti_grid, "#")}')

# Part 2
    anti_grid = grid.copy()
    for key in antenna_dict:
        for pair in itertools.combinations(antenna_dict[key], 2):
            find_antinodes_v2(grid, anti_grid, pair)
    dump_grid(anti_grid)
    print(f'Num antinodes: {count_char(anti_grid, "#")}')         
