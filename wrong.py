count = 0  # 指定选出了多少个符合要求的数字
print("1.A(0...9)/B(0...9)C(0...9)D(0...9);(四个数都是0-9中选择;)")
print("2.A=B不等于C、D;(只允许两个数相同)")
print("3.A不等于B不等于C不等于D(四个数不同)")
print("4.A\B\C\D排除掉一个数,请输入你要排除的数字：", end="")
rid = input()  # 排除的数字

print("5.A\B\C\D中必有一个数,请输入必有的数字：", end="")
existNumber = input()
print("6.四个数之和小于多少，请输入你希望小于的数字：", end="")
less = int(input())
print("7.四个数之和大于多少，请输入你希望大于的数字：", end="")
greater = int(input())

print("8.A\B\C\D不能同时存在的两个数，请输入你选择的第一个数：", end="")
first = input()
print("=请输入你选择的第二个数：", end="")
second = input()

print("9.A\B\C\D中存在(1、2、3)三者之一,请输入第一个数：", end="")
one = input()
print("=请输入第二个数：", end="")
two = input()
print("=请输入第三个数：", end="")
three = input()
res = []
res.append(one)
res.append(two)
res.append(three)

# print(rid,first,second)
result = []

for a in range(10):
    if a != rid:  # 四个数均不等于rid
        for b in range(10):
            if b != rid and b != a:  # 四个数均不等于rid,b不等于a
                for c in range(10):
                    if c != rid and c != a and c != b:  # 四个数均不等于rid
                        for d in range(10):
                            if d != rid and d != a and d != b and d != c:  # 四个数均不等于rid
                                number = str(a) + str(b) + str(c) + str(d)
                                sum = a + b + c + d

                                if existNumber in res:
                                    res.remove(existNumber)

                                    if existNumber not in number or sum >= less or sum <= greater or res[0] in number or \
                                            res[1] in number:
                                        # 如果指定必有的数不在ABCD中,或者和不小于指定的数,或者和不大于指定的数,跳过这次循环
                                        continue
                                    if first in number and second not in number:  # 如果first存在,那么second不可能存在
                                        count += 1
                                        # print("{}{}{}{}".format(a, b, c, d))
                                        result.append(number)
                                    if first not in number:  # 如果first不存在,有两种情况:一种是second存在,一种是second不存在
                                        count += 1
                                        # print("{}{}{}{}".format(a, b, c, d))
                                        result.append(number)

                                if existNumber not in res:
                                    if (one in number and two not in number and three not in number) or \
                                            (two in number and one not in number and three not in number) or \
                                            (three in number and two not in number and one not in number):

                                        if existNumber not in number or sum >= less or sum <= greater:
                                            # 如果指定必有的数不在ABCD中,或者和不小于指定的数,或者和不大于指定的数,跳过这次循环
                                            continue
                                        if first in number and second not in number:  # 如果first存在,那么second不可能存在
                                            count += 1
                                            # print("{}{}{}{}".format(a, b, c, d))

                                            result.append(number)
                                        if first not in number:  # 如果first不存在,有两种情况:一种是second存在,一种是second不存在
                                            count += 1
                                            # print("{}{}{}{}".format(a, b, c, d))
                                            result.append(number)

print("count", count)
print("结果",result)
input("输入quit结束：")