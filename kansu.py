# def say_your_name():
#     n = input('名前')
#     print('あなたの名前は', n, 'ですね')

# say_your_name()


# def say_your_name(n):
#     name = n
#     print('あなたの名前は', name, 'ですね')

# say_your_name(input('名前'))

def jugge_odd(num):
    if num % 2 == 1:
        return '奇数'
        # return s
    else:
        return '偶数'
        # return s


while True:
    n = int(input('整数'))
    if n == 0:
        print('終了')
        break
    else:
        print('入力されたのは', jugge_odd(n), 'です')
