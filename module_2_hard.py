print('Введите число от 3 до 20 ')
numbers = int(input())
result = []
for i in range(1, 20):
    if numbers <= 2:
        print('Это число не используется')
        break
    for j in range(1, 20):
        if i >= j:
            continue
        else:
            kratno = numbers % (i + j)
            if kratno == 0:
                result.append(i), result.append(j)
print(f'Для числа {numbers} пароль: ', ''.join(map(str, result)))
