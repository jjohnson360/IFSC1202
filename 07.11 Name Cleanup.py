def format_name(name):
    first, *middle, last = name.strip().split()
    middle = ' '.join(m.capitalize() for m in middle)
    return f'{first.capitalize()} {middle} {last.capitalize()}'

print('{:<12}{:<12}{:<12}'.format('First', 'Middle', 'Last'))
print('-'*36)

with open('07.11 Names.txt', 'r') as f:
    for line in f:
        name = format_name(line)
        first, *middle, last = name.split()
        if middle:
            print('{:<12}{:<12}{:<12}'.format(first, middle[0], last))
        else:
            print('{:<12}{:<12}{:<12}'.format(first, '', last))
