# n = int(input('整数n:'))
#
# if not (n<= -10 or n>=10):
#     print('その値は二桁未満です')
# else:
#     print('その整数は二桁以上です')
# mounth = input(int('季節を求めます/n月を入力してください'))

# a = int(input('整数a:'))
# b = int(input('整数b:'))
# if a - b <= 0 :
#     print('絶対値は',b-a,'です')
# else:
#     print('絶対値は',a-b,' desu')
    # t = a
    # a = b
    # b = t

# print('a≦bとなるようにソートしました')
# print('変数aの値は', a, 'です')
# print('変数bの値は', b, 'です')

test = int(input('点数を入力してください:'))
if 0 <=test  or 100 <=test:
    if 90 <= test and test <= 100:
        print('秀です')
    elif 80 <= test and test <=89:
        print('ゆうです')
    elif 70 <= test and test <=79:
        print('良です')
    elif 60 <= test and test <=69:
        print('かです')
    elif test <=59:
        print('あーあ落胆だよ')

else:
    print('そんなのない')