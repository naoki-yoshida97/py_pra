

# # print('-'*27)
# #
# # for i in range(1, 10):
# #     for j in range(1, 10):
# #         print('{:3d}'.format(i*j), end='')
# #     print()
# #
# # print('-'*27)


# h = int(input('高さ:'))
# w = int(input('幅:'))

# for i in range(h):
#     for j in range(w):
#         print('*', end='')
#     print()
# print('左上直角の二等辺三角形')
# n = int(input('模様:'))
# for i in range(n):
#     if i/2 == 0:
#         for j in range(n):
#             print('*', end='')
#             print('&', end='')
#         print()
#     else:
#         for j in range(n):
#             print('&', end='')
#             print('*', end='')
#         print()print('長方形')
h = int(input('高さ：'))
w = int(input('横幅：'))
for i in range(h):
    # if h/2 == 0:
    # print(h)
    for j in range(w):
        # print(w)
        if (i+j) % 2 == 0:
            print('□', end='')
            # print('■', end='')
        else:
            print('■', end='')
            # print('□', end='')
    print()

    # for j in range(w):
    #     print('&', end='')
    #     print('*', end='')
    # print()
