

# print('-'*27)
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print('{:3d}'.format(i*j), end='')
#     print()
#
# print('-'*27)


h = int(input('高さ:'))
w = int(input('幅:'))

for i in range(h):
    for j in range(w):
        print('*', end='')
    print()
