import sys
import re

def find_in_grid(grid, row, col, pattern) -> list[str]:
    # print(f'find_in_grid: {grid}, {row}, {col}, {pattern}')

    if grid[row][col] != pattern[0]:
        return []
    found = []
    max_x = len(grid[0])
    max_y = len(grid)
    # east
    if (col + len(pattern)) <= max_x:
        if grid[row][col:col+len(pattern)] == pattern:
            found.append("E")
    # west
    if (col - len(pattern)) >= -1:
        match = True
        for index in range(0, len(pattern)):
            if grid[row][col-index] != pattern[index]:
                match = False
                break
        if match:
            found.append("W") 
    # north
    if (row - len(pattern)) >= -1:
        match = True
        for index in range(0, len(pattern)):
            if grid[row-index][col] != pattern[index]:
                match = False
                break
        if match:
            found.append("N")
    # south
    if (row + len(pattern)) <= max_y:
        match = True
        for index in range(0, len(pattern)):
            if grid[row+index][col] != pattern[index]:
                match = False
                break
        if match:
            found.append("S")
    # northeast
    if (row - len(pattern)) >= -1 and (col + len(pattern)) <= max_x:
        match = True
        for index in range(0, len(pattern)):
            if grid[row-index][col+index] != pattern[index]:
                match = False
                break
        if match:
            found.append("NE")
    # northwest
    if (row - len(pattern)) >= -1 and (col - len(pattern)) >= -1:
        match = True
        for index in range(0, len(pattern)):
            if grid[row-index][col-index] != pattern[index]:
                match = False
                break
        if match:
            found.append("NW")
    # southeast
    if (row + len(pattern)) <= max_y and (col + len(pattern)) <= max_x:
        match = True
        for index in range(0, len(pattern)):
            if grid[row+index][col+index] != pattern[index]:
                match = False
                break
        if match:
            found.append("SE")
    # southwest
    if (row + len(pattern)) <= max_y and (col - len(pattern)) >= -1:
        match = True
        for index in range(0, len(pattern)):
            if grid[row+index][col-index] != pattern[index]:
                match = False
                break
        if match:
            found.append("SW")
    return found

def find_in_grid_diag(grid, row, col, pattern) -> list[str]:
    # print(f'find_in_grid: {grid}, {row}, {col}, {pattern}')

    if grid[row][col] != pattern[0]:
        return []
    found = []
    max_x = len(grid[0])
    max_y = len(grid)
    
    # northeast
    if (row - len(pattern)) >= -1 and (col + len(pattern)) <= max_x:
        match = True
        for index in range(0, len(pattern)):
            if grid[row-index][col+index] != pattern[index]:
                match = False
                break
        if match:
            found.append("NE")
    # northwest
    if (row - len(pattern)) >= -1 and (col - len(pattern)) >= -1:
        match = True
        for index in range(0, len(pattern)):
            if grid[row-index][col-index] != pattern[index]:
                match = False
                break
        if match:
            found.append("NW")
    # southeast
    if (row + len(pattern)) <= max_y and (col + len(pattern)) <= max_x:
        match = True
        for index in range(0, len(pattern)):
            if grid[row+index][col+index] != pattern[index]:
                match = False
                break
        if match:
            found.append("SE")
    # southwest
    if (row + len(pattern)) <= max_y and (col - len(pattern)) >= -1:
        match = True
        for index in range(0, len(pattern)):
            if grid[row+index][col-index] != pattern[index]:
                match = False
                break
        if match:
            found.append("SW")
    return found


if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    num_found = 0
    for row in range(0, len(lines)):
        for col in range(0, len(lines[row])):
            found = find_in_grid(lines, row, col, "XMAS")
            print(f'coord: {row},{col}, char: {lines[row][col]}, found: {found}')
            num_found += len(found)
    print(f'found {num_found} XMAS')
            
    # part 2
    
    num_found = 0
    found = []
    for row in range(1, len(lines)-1):
        for col in range(1, len(lines[row])-1):
            if lines[row][col] != "A":
                continue
            if "SE" in find_in_grid_diag(lines, row-1, col-1, "MAS"):
                found.append("SE")
            if "SW" in find_in_grid_diag(lines, row-1, col+1, "MAS"):
                found.append("SW")
            if "NE" in find_in_grid_diag(lines, row+1, col-1, "MAS"):
                found.append("NE")
            if "NW" in find_in_grid_diag(lines, row+1, col+1, "MAS"):
                found.append("NW")
            print(f'coord: {row},{col}, char: {lines[row][col]}, found: {found}')
            if len(found) == 2:
                num_found += 1
            found = []
    print(f'found {num_found} XMAS')