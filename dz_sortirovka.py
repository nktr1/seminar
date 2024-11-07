import time
import random
import matplotlib.pyplot as plt

# #Пузырььь
# N = 500
# a = [random.randint(1, 99) for n in range(N)]
# v = time.time()
# for i in range(N-1):
#     for j in range(N-1-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# z = time.time()
#
# print(a)
# print(z-v)



# Выбором
# def asd(a):
#     res = 0
#     for i in range(1, len(a)):
#         if a[i]>=a[res]:
#             res = i
#     return res
# def sort(a):
#     for i in range(len(a)-1):
#         j = asd(a[:len(a)-i])
#         f = len(a)-1-i
#         a[j],a[f]=a[f],a[j]
#
# N = 450
# a = [random.randint(1, 99) for n in range(N)]
# v = time.time()
# sort(a)
# z = time.time()
# print(*a)
# print(z-v)


# #Вставка
# def count(a):
#     cnts = [0 for i in range(100)]
#     for el in a:
#         cnts[el] += 1
#     # for i in range(len(a)):
#     #     cnts[a[i]] +=1
#     res = []
#     for i in range(len(cnts)):
#         res += [i]*cnts[i]
#     return res
# N = 500
# a = [random.randint(1, 99) for n in range(N)]
# v = time.time()
# a=count(a)
# z = time.time()
# print(a)
# print(z-v)



x = [100, 150, 200, 250, 300, 350, 400, 450, 500]
yP = [0.0007328987121582031, 0.0021026134490966797, 0.003342151641845703, 0.00523686408996582, 0.007096052169799805, 0.009876012802124023, 0.012369871139526367, 0.016691923141479492, 0.021618127822875977]
yV = [0.0001728534698486328, 0.00035500526428222656, 0.0006029605865478516, 0.0009100437164306641, 0.0013148784637451172, 0.001828908920288086, 0.002496957778930664, 0.0032329559326171875, 0.0038459300994873047]
yZ = [0.000024, 0.000027, 0.00003, 0.0000319, 0.000035, 0.000037, 0.000039, 0.000041, 0.000044]
plt.plot(x, yZ, color = "green")
plt.plot(x, yP, color = "red")
plt.plot(x, yV, color = "blue")
plt.scatter(x, yP, label='Пузырек', color = "red")
plt.scatter(x, yV, label='Выбором', color = "blue")
plt.scatter(x, yZ, label='Вставка', color = "green")
plt.legend()
plt.show()


# Пузырь:
# 100 - 0.0007328987121582031
# 150 - 0.0021026134490966797
# 200 - 0.003342151641845703
# 250 - 0.00523686408996582
# 300 - 0.007096052169799805
# 350 - 0.009876012802124023
# 400 - 0.012369871139526367
# 450 - 0.016691923141479492
# 500 - 0.021618127822875977
#
# Выбором:
# 100 - 0.0001728534698486328
# 150 - 0.00035500526428222656
# 200 - 0.0006029605865478516
# 250 - 0.0009100437164306641
# 300 - 0.0013148784637451172
# 350 - 0.001828908920288086
# 400 - 0.002496957778930664
# 450 - 0.003114938735961914
# 500 - 0.0038459300994873047




