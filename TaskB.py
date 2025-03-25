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

    BD = [a[6] - a[2], a[7] - a[3]]
    len_D2 = (BD[0]**2 + BD[1]**2)
    AC = [a[4] - a[0], a[5] - a[1]]
    len_D1 = (AC[0]**2 + AC[1]**2)
    AD = [a[6] - a[0], a[7] - a[1]]
    len_D = (AD[0]**2 + AD[1]**2)
    AB = [a[2] - a[0], a[3] - a[1]]
    len_A = (AB[0]**2 + AB[1]**2)
    BC = [a[4] - a[2], a[5] - a[3]]
    len_B = (BC[0]**2 + BC[1]**2)
    CD = [a[6] - a[4], a[7] - a[5]]
    len_C = (CD[0]**2 + CD[1]**2)

    if (len_D1 + len_D2) == (len_A + len_B + len_C + len_D):
        return True
    else:
        return False

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
n = int(b[0])
a = b[1:n+1]
result = ''
for i in a:
    try:
        l = (i.lower().replace('o', '0').replace('о', '0')
             .replace('- ', '-').replace('l', '1')
             .replace('i', '1').replace('  ', ' ').strip().split(' '))
        list__ = [int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5]), int(l[6]), int(l[7])]
        figure_is_p = parallelogram_check(list__)
    except:
        figure_is_p = False
    if figure_is_p:
        result += 'YES\n'
    else:
        result += 'NO\n'
with open(file = 'output_B.txt', mode = 'w') as file2:
    file2.write(result)




