import sys

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    left_list = []
    right_list = []
    for line in lines:
        left, right = line.split('   ')
        left_list.append(int(left))
        right_list.append(int(right))
    left_list.sort()
    right_list.sort()

    delta_sum = 0
    index = 0
    for val in left_list:
        delta_sum += abs(left_list[index] - right_list[index])
        index += 1

    print(f'delta_sum: {delta_sum}')

    similar_sum = 0
    index = 0
    for val in left_list:
        similar_sum += right_list.count(left_list[index]) * left_list[index]
        index += 1

    print(f'similar_sum: {similar_sum}')

    # print(f'left_list: {left_list}, right_list: {right_list}, delta_sum: {delta_sum}')
    # sum_list = [sum([int(x) for x in y.split('\n')]) for y in elf_list_raw]

    # max_cal = 0
    # max_elf = 0
    # for index, value in enumerate(elf_list_raw):
    #     cal_list = value.split('\n')
    #     print(f'{index}: {cal_list}')
    #     if sum([int(x) for x in cal_list]) > max_cal:
    #         max_cal = sum([int(x) for x in cal_list])
    #         max_elf = index

    # sum_list.sort(reverse=True)
    
    # print(f'max cal is: {max(sum_list)}, top 3 sum is: {sum(sum_list[0:3])}')


