def ProperCase(s):
    if not s:
        return ''
    return s[0].upper() + s[1:].lower()

def RemoveNewLine(s):
    return s.replace('\n', '')

def Trim(s):
    return s.strip()

def FirstName(s):
    first_space = s.find(' ')
    return ProperCase(s[:first_space])

def LastName(s):
    last_space = s.rfind(' ')
    return ProperCase(s[last_space+1:])

def MiddleName(s):
    first_space = s.find(' ')
    last_space = s.rfind(' ')
    if first_space == -1 or last_space == -1 or last_space <= first_space:
        return ''
    middle_name = Trim(s[first_space:last_space])
    middle_name = ProperCase(middle_name)
    if len(middle_name) == 1:
        middle_name += '.'
    return middle_name

print('{:<12}{:<12}{:<12}'.format('First', 'Middle', 'Last'))
print('-'*36)

with open('07.11 Names.txt', 'r') as f:
    for line in f:
        line = RemoveNewLine(Trim(line))
        first_name = FirstName(line)
        middle_name = MiddleName(line)
        last_name = LastName(line)
        print('{:<12}{:<12}{:<12}'.format(first_name, middle_name, last_name))
