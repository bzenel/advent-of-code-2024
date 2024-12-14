import sys
import itertools

op_dict = {
    '0': '+',
    '1': '*',
    '2': '||'
}

def decimal_to_base_3(n):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % 3))
        n //= 3
    return ''.join(str(x) for x in digits[::-1])

def eval(expr: list, target: int) -> bool:
    result = expr.pop(0)
    expr = expr.copy()
    while len(expr) > 0:
        op = expr.pop(0)
        val = expr.pop(0)
        if op == '+':
            result += val
        elif op == '*':
            result *= val
        elif op == '||':
            result = int(str(result) + str(val))
        else:
            print(f'invalid operator: {op}')
            return False
    print(f'result: {result}')
    return result == target

def perms(vals: list) -> list:
    perm_list = []
    for index in range(0, 3**(len(vals)-1)):
        perm_list.append(decimal_to_base_3(index).rjust(len(vals)-1, '0'))
    expr_list = []
    for perm in perm_list:
        # print(f'perm: {perm}')
        expr = []
        for index in range(0, len(perm)):
            expr.append(vals[index])
            expr.append(op_dict[perm[index]])
        expr.append(vals[-1])
        expr_list.append(expr)
    return expr_list

if __name__ == "__main__":
    print(f'starting...')

    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    total_true = 0
    for line in lines:
        target = int(line.split(':')[0])
        print(f'target: {target}')
        vals = [int(x) for x in line.split(':')[1].strip().split(' ')]
        print(f'vals: {vals}')
        print(f'perms: {perms(vals)}')
        for expr in perms(vals):
            expr_eval = eval(expr, target)
            print(f'expr: {expr}, target: {target}, eval: {expr_eval}')
            if expr_eval is True:
                total_true += target
                break
    print (f'total_true: {total_true}')