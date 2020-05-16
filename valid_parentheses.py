def valid_parentheses(string):
    array = []
    for i in string:
        if i == '(':
            array.append([])
        elif i == ')':
            try:
                array.pop()
            except IndexError:
                return False
    if array == []:
        return True
    else:
        return False


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
