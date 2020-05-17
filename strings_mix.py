def mix(s1, s2):
    stringList = ""
    for i in s1:
        if ord(i) in range(97, 123):
            if s1.count(i) > 1:
                stringList += ('1:' + i * s1.count(i) + '/')
                s1 = s1.replace(i, '')
    for i in s2:
        if ord(i) in range(97, 123):
            if s2.count(i) > 1:
                if s2.count(i) == stringList.count(i):
                    stringList = stringList.replace('1:' + i, '=:' + i)
                elif s2.count(i) > stringList.count(i):
                    stringList += ('2:' + i * s2.count(i) + '/')
                    stringList = stringList.replace('1:' + i*stringList.count(i), '')
                elif s2.count(i) < stringList.count(i):
                    continue
                else:
                    stringList += ('2:' + i * s2.count(i) + '/')
                s2 = s2.replace(i, '')

    print(stringList)
    # print(sorted(stringList, key=len, reverse=True))


s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2)  # "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2)  # "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "Are the kids at home? aaaaa fffff"
s2 = "Yes they are here! aaaaa fffff"
mix(s1, s2)  # "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
