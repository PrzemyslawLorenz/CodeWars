def name_list(names):
    string = ''
    for d in names:
        string += string.join(d.values())
        if names.index(d) < len(names) - 2:
            string += ', '
        elif names.index(d) == len(names) - 2:
            string += ' & '
        else:
            break

    return string


print(name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
