def mix(s1, s2):
    stringList = []
    for i in range(97, 123):
        if chr(i) in s1 or chr(i) in s2:
            if s1.count(chr(i)) > 1 or s2.count(chr(i)) > 1:
                if s1.count(chr(i)) > s2.count(chr(i)):
                    stringList.append('1:' + chr(i) * s1.count(chr(i)) + '/')
                elif s1.count(chr(i)) < s2.count(chr(i)):
                    stringList.append('2:' + chr(i) * s2.count(chr(i)) + '/')
                else:
                    stringList.append('=:' + chr(i) * s1.count(chr(i)) + '/')

    stringList = sorted(stringList)
    stringList = sorted(stringList, key=len, reverse=True)
    listToStr = ''.join([str(elem) for elem in stringList])
    return listToStr[:-1]



s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
print(mix(s1, s2))  # "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
print(mix(s1, s2))  # "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "Are the kids at home? aaaaa fffff"
s2 = "Yes they are here! aaaaa fffff"
print(mix(s1, s2))  # "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"

s1 = " In many languages"
s2 = " there's a pair of functions"
print(mix(s1, s2))  # "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"