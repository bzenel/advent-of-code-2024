import sys

def is_safe(row) -> bool:
    """ Determine if a row is safe

    Args:
        row (list): list of integers

    Returns:
        bool: True if the row is safe, False otherwise
    """
    orig_row = row.copy()
    if (row[1] - row[0]) < 0:
        row = sorted(row, reverse=True)
    else:
        row = sorted(row)
    if orig_row != row:
        print(f'row: {orig_row} is not safe (order)')
        return False
    delta_set = {abs(row[index+1] - row[index]) for index in range(0,len(row)-1)}
    if len(delta_set - set([1, 2, 3])) > 0:
        print(f'row: {row} is not safe (delta)')
        return False
    print(f'row: {orig_row} is safe')
    return True

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    table = [[int(x) for x in y.split(' ')] for y in lines]

    num_safe = 0
    for row in table:
        # print(f'row: {row}')
        num_safe += (1 if is_safe(row) else 0)

    print(f'num_safe: {num_safe}')

    ### Part 2

    num_safe = 0
    for row in table:
        if is_safe(row):
            num_safe += 1
            continue
        if sum([is_safe(row[0:index] + row[index+1:]) for index in range(0, len(row))]) > 0:
            num_safe += 1

    print(f'new num_safe: {num_safe}')
            

