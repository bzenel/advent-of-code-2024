import sys
import re

def multiply(instr: str) -> int:
    """ Multiply two numbers

    Args:
        instr (str): string of two numbers with format mul(a,b)

    Returns:
        int: the product of the two numbers
    """
    cooked = instr[4:-1]
    a, b = cooked.split(',')
    return int(a) * int(b)

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    pattern = r"(mul\(\d{,3},\d{,3}\))+?"
    sum_of_products = 0
    for line in lines:
        matches = re.findall(pattern, line)
        if matches:
            for match in matches:
                print(f'{match}: {multiply(match)}')
                sum_of_products += multiply(match)
    print(f'sum_of_products: {sum_of_products}')

    ### Part 2

    pattern = r"(mul\(\d{,3},\d{,3}\))|(do)\(\)|(don't)\(\)"

    sum_of_products = 0
    ignore = False
    for line in lines:
        matches = re.findall(pattern, line)
        print(f'{matches}')
        if matches:
            for groups in matches:
                print(f'{groups}')
                for group in groups:
                    if group == "":
                        continue
                    match = group
                print(f'{match}')
                if match[0:5] == "don't":
                    ignore = True
                    print('setting ignore')
                    continue
                elif match[0:2] == "do":
                    ignore = False
                    print('resetting ignore')
                    continue
                print(f'ignore: {ignore}')
                if ignore is True:
                    print(f'ignoring: {match}')
                    continue
                print(f'{match}: {multiply(match)}')
                sum_of_products += multiply(match)
    print(f'sum_of_products: {sum_of_products}')

