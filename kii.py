n = int(input('整数:'))
# s = range(n)
# print(list(s))
su = 0
if n > 0:
    for n in range(n):  # range(n)をnになるまで繰り返す
        if n % 2 == 1:  # nの条件式
            su += n
            # print('hoge', su)
print(su)
