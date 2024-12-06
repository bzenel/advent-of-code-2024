import sys
import itertools

def is_in_order(rule_dict, target) -> bool:
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
        for item in before:
            if item in order_list:
                # printf'item {item} is before {target[index]}')
                ordered = False
                break
        if not ordered:
            # printf'+++ {target} is out of order +++')
            break;
    return ordered


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
        if is_in_order(order_dict, update):
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
        for perm in itertools.permutations(out_of_order_list[oo_index]):
            if counter % 1000000 == 0:
                print('.', end='', flush=True)
            counter += 1
            # print(f'looking at perm: {perm}')
            if is_in_order(order_dict, perm):
                print(f'\nFound a valid perm!: {perm}')
                in_order_sum += int(perm[int(len(perm)/2)])
                break;
    print(f'Re-ordered in_order_sum: {in_order_sum}')








