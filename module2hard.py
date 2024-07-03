number = int(input('Please enter random number from 3 to 20: '))

while 3 > number or number > 20:
    number = int(input('The number is not valid. Please try again: '))


def get_result(number_):
    result = []

    for i in range(1, number_ + 1):
        for j in range(i + 1, number_ + 1):
            if number_ % (i + j) == 0:
                result.append(str(i))
                result.append(str(j))
    return result


def check_result(number_for_checking, result_for_checking):
    str_ = ''.join(result_for_checking)
    right_combinations = {3: '12',
                          4: '13',
                          5: '1423',
                          6: '121524',
                          7: '162534',
                          8: '13172635',
                          9: '1218273645',
                          10: '141923283746',
                          11: '11029384756',
                          12: '12131511124210394857',
                          13: '112211310495867',
                          14: '1611325212343114105968',
                          15: '1214114232133124115106978',
                          16: '1317115262143531341251161079',
                          17: '11621531441351261171089',
                          18: '12151811724272163631545414513612711810',
                          19: '118217316415514613712811910',
                          20: '13141911923282183731746416515614713812911'
                          }

    if right_combinations.get(number_for_checking) == str_:
        print('You are win!')
    else:
        print('You are lose!')


res = get_result(number)

print('Your access is:')
print(*res)

check_result(number, res)
