numbers = {0: 'zero'}


def spell_number(n):
    return numbers.get(n)


numbers[1] = 'one'
numbers[2] = 'two'
numbers[3] = 'three'
numbers[4] = 'four'
numbers[5] = 'five'
