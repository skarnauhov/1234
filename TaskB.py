"""
На уроке геометрии семиклассники Вася и Петя узнали, что такое параллелограмм.
На перемене после урока они стали играть в игру: Петя называл координаты четырех
точек в произвольном порядке, а Вася должен был ответить, являются ли эти точки
вершинами параллелограмма.

Вася, если честно, не очень понял тему про параллелограммы, и ему требуется программа,
умеющая правильно отвечать на Петины вопросы.

Напомним, что параллелограммом называется четырехугольник, противоположные стороны
которого равны и параллельны.

Формат ввода
В первой строке входного файла записано целое число N (1 ≤ N ≤ 10) - количество заданных
Петей вопросов. Каждая из N последующих строк содержит описание четырех точек - четыре пары
целых чисел X и Y (−100 ≤ X ≤ 100, −100 ≤ Y ≤ 100), обозначающих координаты точки.
Гарантируется, что четыре точки, о которых идет речь в одном вопросе,
не лежат на одной прямой.

Формат вывода
Для каждого из вопросов выведите "YES", если четыре заданные точки могут образовать
параллелограмм, и "NO" в противном случае. Ответ на каждый из запросов должен быть в
отдельной строке без кавычек.
"""
def vector_ugol_check(t):
    a = [t[0][0], t[0][1], t[1][0], t[1][1], t[2][0], t[2][1], t[3][0], t[3][1]]
    print(a)
    BD = [a[6] - a[2], a[7] - a[3]]
    len_D2 = (BD[0]**2 + BD[1]**2)
    AC = [a[4] - a[0], a[5] - a[1]]
    len_D1 = (AC[0]**2 + AC[1]**2)
    print(AC)
    AD = [a[6] - a[0], a[7] - a[1]]
    len_D = (AD[0]**2 + AD[1]**2)
    print(AD)
    AB = [a[2] - a[0], a[3] - a[1]]
    len_A = (AB[0]**2 + AB[1]**2)
    print(AB)

    # V_kos_1 = AC[0]*AB[1] - AC[1]*AB[0]
    # V_kos_2 = AC[0]*AD[1] - AC[1]*AD[0]
    # print('косое: ', V_kos_1, V_kos_2)
    # if (V_kos_1 > 0 and V_kos_2 > 0) or (V_kos_1 < 0 and V_kos_2 < 0):
    #     print('NO wrong sequence')
    #     return False
    # elif V_kos_1 == 0 or V_kos_2 == 0:
    #     return False
    # elif len_AC < len_AD and len_AC < len_AB:
    #     print('NO vpuklyi')
    #     return False

    BC = [a[4] - a[2], a[5] - a[3]]
    len_B = (BC[0]**2 + BC[1]**2)
    BA = [a[0] - a[2], a[1] - a[3]]
    print(BC)
    print(BA)

    CB = [a[2] - a[4], a[3] - a[5]]
    CD = [a[6] - a[4], a[7] - a[5]]
    len_C = (CD[0]**2 + CD[1]**2)
    print(CB)
    print(CD)

    DA = [a[0] - a[6], a[1] - a[7]]
    DC = [a[4] - a[6], a[5] - a[7]]
    print(DA)
    print(DC)

    print('---', (len_D1 + len_D2))
    print('---___', (len_A + len_B + len_C + len_D))

    if (len_D1 + len_D2) == (len_A + len_B + len_C + len_D):
        return True
    else:
        return False

    S1 = AB[0]*AD[1]-AB[1]*AD[0]
    S2 = BC[0]*BA[1]-BC[1]*BA[0]
    S3 = CD[0]*CB[1]-CD[1]*CB[0]
    S4 = DA[0]*DC[1]-DA[1]*DC[0]

    print(S1, S2, S3, S4)
    # if S1 == S2 == S3 == S4:
    #     return True
    # else:
    #     return False

    # len_BC = round((BC[0]**2 + BC[1]**2)**(1/2), 3)
    # print(BC, len_BC)
    # CD = [a[6] - a[4], a[7] - a[5]]
    # len_CD = round((CD[0]**2 + CD[1]**2)**(1/2), 3)
    # print(CD, len_CD)
    # DA = [a[0] - a[6], a[1] - a[7]]
    # len_DA = round((DA[0]**2 + DA[1]**2)**(1/2), 3)
    # print(DA, len_DA)
    #
    # V_len_list = [len_AB, len_BC, len_CD, len_DA]
    # if V_len_list.count(len_AB) == 3 or V_len_list.count(len_DA) == 3:
    #     print('NO triangle')
    #     return False
    #
    # V_len_set = {len_AB, len_BC, len_CD, len_DA}
    # print(V_len_set)
    # cos_AB_BC = (AB[0] * BC[0] + AB[1] * BC[1]) / (len_AB * len_BC)
    # cos_BC_CD = (BC[0] * CD[0] + BC[1] * CD[1]) / (len_BC * len_CD)
    # cos_CD_DA = (CD[0] * DA[0] + CD[1] * DA[1]) / (len_CD * len_DA)
    # cos_DA_AB = (AB[0] * DA[0] + AB[1] * DA[1]) / (len_AB * len_DA)
    # cos_AC_AB = (AC[0] * AB[0] + AC[1] * AB[1]) / (len_AC * len_AB)
    # cos_AC_AD = (AC[0] * AD[0] + AC[1] * AD[1]) / (len_AC * len_AD)
    #print(cos_AC_AD, cos_AC_AB)
    # V_cos_list = [cos_AB_BC, cos_BC_CD, cos_CD_DA, cos_DA_AB]
    # print(V_cos_list)
    # print('сумма: ', sum(V_cos_list))

    # if len(V_len_set) <= 2:
    #     return True
    # else:
    #     return False

# def sorted_list_check(t_s):
#     t_x_1 = [t_s[3][0] - t_s[2][0], t_s[1][0] - t_s[0][0]]
#     t_x_2 = [t_s[3][0] - t_s[1][0], t_s[2][0] - t_s[0][0]]
#     t_y_1 = [t_s[3][1] - t_s[2][1], t_s[1][1] - t_s[0][1]]
#     t_y_2 = [t_s[3][1] - t_s[1][1], t_s[2][1] - t_s[0][1]]
#     if (t_x_1[0] != t_x_1[1] or t_x_2[0] != t_x_2[1]
#             or t_y_1[0] != t_y_1[1] or t_y_2[0] != t_y_2[1]):
#         return False
#     else:
#         return True
def combinations_list(t):
    combinations = []
    t1 = t.copy()
    for i1 in range(0, 4):
        k = t1.pop(i1)
        x = t1.copy()
        for i2 in range(0, 3):
            l = x.pop(i2)
            y = x.copy()
            for i3 in range(0, 2):
                m = y.pop(i3)
                z = y.copy()
                combinations.append([k, l, m, y[0]])
                y = x.copy()
            x = t1.copy()
        t1 = t.copy()
    return combinations

def parallelogram_check(a):
    t = [(a[0], a[1]), (a[2], a[3]), (a[4], a[5]), (a[6], a[7])]
    t_set = set(t)
    if len(t_set) < 4:
        return False
    combinations = combinations_list(t)
    for item in combinations:
        if vector_ugol_check(item):
            return True
    return False

with open(file = 'input_B.txt', mode = 'r', encoding='utf-8') as file:
    b = file.read().split('\n')
    print(b)
n = int(b[0])
a = b[1:n+1]
result = ''
for i in a:
    print('\n', i)
    try:
    #list__ = [int(n) for n in i.split(" ")]
        l = (i.lower().replace('o', '0').replace('о', '0')
             .replace('- ', '-').replace('l', '1')
             .replace('i', '1').replace('  ', ' ').strip().split(' '))
        list__ = [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), int(l[6]), int(l[7])]
    #list__= list(map(int, list_[:8]))
        figure_is_p = parallelogram_check(list__)
    except:
        figure_is_p = False
    print(figure_is_p)
    if figure_is_p:
        result += 'YES\n'
    else:
        result += 'NO\n'
with open(file = 'output_B.txt', mode = 'w') as file2:
    file2.write(result)




