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

def parallelogram_check(a):
    t = ((int(a[0]), int(a[1])), (int(a[2]), int(a[3])),
         (int(a[4]), int(a[5])), (int(a[6]), int(a[7])))
    t_set = set(t)
    t_x = (int(a[0]), int(a[2]), int(a[4]), int(a[6]))
    t_x_set = set(t_x)
    t_y = (int(a[1]), int(a[3]), int(a[5]), int(a[7]))
    t_y_set = set(t_y)
    t_s = ()
    if len(t_x_set) == 4:
        t_s = sorted(t, key=lambda value: value[0])
    elif len(t_y_set) == 4:
        t_s = sorted(t, key=lambda value: value[1])
    elif len(t_x_set) == 3:
        t_s = sorted(t, key=lambda value: value[0])
    elif len(t_y_set) == 3:
        t_s = sorted(t, key=lambda value: value[1])
    elif len(t_x_set) == 2 and len(t_y_set) == 2:
        t_s = sorted(t, key=lambda value: value[0] + value[1])
    t_x_s = sorted(t_x)
    t_y_s = sorted(t_y)

    if len(t_set) < 4:
        return False
    elif (t_x_s.count(t_x_s[0]) == 3 or t_x_s.count(t_x_s[3]) == 3
          or t_y_s.count(t_y_s[0]) == 3 or t_y_s.count(t_y_s[3]) == 3):
        return False
    elif len(t_s) == 0:
        return False
    else:
        t_x_1 = {(t_s[3][0] - t_s[2][0]), (t_s[1][0] - t_s[0][0])}
        t_x_2 = {(t_s[3][0] - t_s[1][0]), (t_s[2][0] - t_s[0][0])}
        t_y_1 = {(t_s[3][1] - t_s[2][1]), (t_s[1][1] - t_s[0][1])}
        t_y_2 = {(t_s[3][1] - t_s[1][1]), (t_s[2][1] - t_s[0][1])}
        if len(t_x_1) == 2 or len(t_y_1) == 2 or len(t_x_2) == 2 or len(t_y_2) == 2:
            return False
        else:
            return True

with open(file = 'input_B.txt', mode = 'r',) as file:
    b = file.read().split('\n')
n = int(b[0])
result = ''
for i in b[1:n+1]:
    a = i.split(' ')
    figure_is_p  = parallelogram_check(a)
    if figure_is_p:
        result += 'YES\n'
    else:
        result += 'NO\n'

with open(file = 'output_B.txt', mode = 'a') as file2:
    file2.write(result)



