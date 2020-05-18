class Calculator(object):
    def evaluate(self, string):
        string = string.split(" ")
        while(len(string) > 1):
            if '*' in string:
                index = string.index('*')
                string[string.index('*')] = float(string[string.index('*') - 1]
                                                  ) * float(string[string.index('*') + 1])
                del(string[index - 1])
                del(string[index])
                pass
            if '/' in string:
                index = string.index('/')
                string[string.index('/')] = float(string[string.index('/') - 1]
                                                  ) / float(string[string.index('/') + 1])
                del(string[index - 1])
                del(string[index])
                pass
            if '+' in string:
                index = string.index('+')
                string[string.index('+')] = float(string[string.index('+') - 1]
                                                  ) + float(string[string.index('+') + 1])
                del(string[index - 1])
                del(string[index])
                pass
            if '-' in string:
                index = string.index('-')
                string[string.index('-')] = float(string[string.index('-') - 1]
                                                  ) - float(string[string.index('-') + 1])
                del(string[index - 1])
                del(string[index])
                pass
        return float(string[0])


print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"))  # => 7
print(Calculator().evaluate("2 - 3 - 4"))  # => -1
print(Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"))  # => 8
print(Calculator().evaluate("1.1 + 2.2 + 3.3"))  # => 6.6
print(Calculator().evaluate("1.1 * 2.2 * 3.3"))  # => 7.986
