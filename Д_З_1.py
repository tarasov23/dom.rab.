num = int(input('Введите длину последовательности:'))
lst = []
for i in range(num):
    for j in range(i + 1):
        lst.append(i + 1)
        if len(lst) == num:
            break
    if len(lst) == num:
        break
print(*lst)
