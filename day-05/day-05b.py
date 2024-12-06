import sys
import itertools

def is_in_order(rule_dict, target) -> list:
    """ Determine if a list of strings is in order

    Args:
        rule_dict (dict): dictionary of rules
        target (list): list of strings

    Returns:
        bool: True if the list is in order, False otherwise
    """
    ordered = True
    for index in range(0, len(target)):
        before = target[0:index]
        after = target[index+1:]
        if target[index] not in rule_dict:
            continue
        order_list = rule_dict[target[index]]
        # printf'evaluating {target[index]}, before: {before}, after: {after}')
        # printf'order_list: {order_list}')
        for before_index in range(0, len(before)):
            if before[before_index] in order_list:
                # printf'item {item} is before {target[index]}')
                ordered = False
                return [index, before_index]
    return []


if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    order_dict: dict[str, list] = {}
    for line in lines:
        left, right = line.split('|')
        if left in order_dict:
            order_dict[left].append(right)
        else:
            order_dict[left] = [right]
    print(f'order_dict: {order_dict}')

    with open(sys.argv[2]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    update_list: list[list[str]] = []
    for line in lines:
        update_list.append(line.split(','))
    print(f'update_list: {update_list}')

    out_of_order_list: list[list[str]] = []
    in_order_sum = 0
    for update in update_list:
        print(f'*** update: {update} ***')
        if len(is_in_order(order_dict, update)) == 0:
            print(f'vvv {update} is in order vvv')
            in_order_sum += int(update[int(len(update)/2)])
        else:
            print(f'vvv {update} is out of order vvv')
            out_of_order_list.append(update)
    print(f'in_order_sum: {in_order_sum}')

    # Part 2

    in_order_sum = 0
    print(f'Num of out of order lists: {len(out_of_order_list)}')
    for oo_index in range(0, len(out_of_order_list)):
        print(f'OO Num: {oo_index}: {out_of_order_list[oo_index]}')
        counter = 0
        test_list = out_of_order_list[oo_index].copy()
        while True:
            rv = is_in_order(order_dict, test_list)
            if len(rv) == 0:
                print(f'\nFound a valid perm!: {test_list}')
                in_order_sum += int(test_list[int(len(test_list)/2)])
                break
            # print(f'swapping {rv[0]} and {rv[1]}')
            mumble = test_list[rv[0]]
            test_list[rv[0]] = test_list[rv[1]]
            test_list[rv[1]] = mumble
            if counter % 1000000 == 0:
                print('.', end='', flush=True)
            counter += 1
    print(f'Re-ordered in_order_sum: {in_order_sum}')








