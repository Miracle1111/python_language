"""
1. Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""

a = [int(i) for i in input().split()]

for i in range(0, len(a), 2):
	print(a[i])

	
"""
2. Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
"""

a = [int(i) for i in input().split() if int(i) % 2 == 0]

for i in a:
    print(i)

	
"""
3. Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""

a = [int(i) for i in input().split()]

for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

		
"""
4. Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
"""

a = [int(i) for i in input().split()]

for i in range(1, len(a)):
    if a[i] * a[i - 1] >= 0:
        print(a[i - 1])
        print(a[i])
        break

		
"""
5. Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""

a = [int(i) for i in input().split()]
count = 0

for i in range(1, len(a) - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        count += 1
print(count)


"""
6. Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
"""

a = [int(i) for i in input().split()]
index = 0
max = a[0]

for i in range(1, len(a)):
    if a[i] > max:
        max = a[i]
        index = i 
print(max, index)	


"""
7. Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
"""

a = [int(i) for i in input().split()]
x = int(input())
index = 1

for i in range(0, len(a)):
    if a[i] < x:
        index = i + 1
        break
else:
    index = len(a) + 1
print(index)	


"""
8. Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
"""

a = [int(i) for i in input().split()]
b = []

for i in a:
    for j in b:
        if i == j:
            break
    else:
        b.append(i)
print(len(b))


"""
9. Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент остается на своем месте.
"""

a = [int(i) for i in input().split()]

for i in range(0, len(a) - 1, 2):
    a[i], a[i+1] = a[i+1], a[i]
for i in a:
    print(i)

	
"""
10. В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""

a = [int(i) for i in input().split()]
max = 0
min = 0

for i in range(len(a)):
    if a[i] > a[max]:
        max = i
    if a[i] < a[min]:
        min = i
a[min], a[max] = a[max], a[min]

for i in a:
    print(i)


"""
11. Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.
"""

a = [int(i) for i in input().split()]
k = int(input())

for j in range(k, len(a) - 1):
    a[j], a[j + 1] = a[j + 1], a[j]
a.pop()
for i in a:
    print(i)


"""
12. Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
"""

a = [int(i) for i in input().split()]
k, c = [int(i) for i in input().split()]
temp = c

for j in range(k, len(a)):
    a[j], temp = temp, a[j]
a.append(temp)

for i in a:
    print(i)


"""
13. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""

a = [int(i) for i in input().split()]
count = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            count += 1
print(count)	


"""
14. Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

a = [int(i) for i in input().split()]

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j] and i != j:
            break
    else:
        print(a[i])
		
		
"""
15. N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1? li? ri? N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""

n, k = [int(i) for i in input().split()]
throws = [[int(i) for i in input().split()] for j in range(k)]

for i in range(1, n + 1):
    for j in throws:
        if i >= j[0] and i <= j[1]:
            print('.', end = '')
            break
    else:
        print('I', end = '')


"""
16. Известно, что на доске 8?8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""

queens = [[int(i) for i in input().split()] for j in range(8)]
beat = False

for i in range(len(queens)):
    x1 = queens[i][0]
    y1 = queens[i][1]
    for j in range(len(queens)):
        if i == j:
            continue
        x2 = queens[j][0]
        y2 = queens[j][1]
        if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
            beat = True
            break
if beat:
    print('YES')
else:
    print('NO')
		