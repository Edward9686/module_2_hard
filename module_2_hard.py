print('Введите число от 3 до 20 ')
numbers = int(input())
list_ = []
for i in range(1, 20):
    if numbers <= 0 or numbers <= 2:
        print('Это число не используется')
        break
    for j in range(1, 20):
        if i >= j:
            continue
        else:
            kratno = numbers % (i + j)
            if kratno == 0:
                list_.append([i, j])
print('Пары чисел ', *list_)
