def getNum3(useful):
    useful = "Важно"
    return 3

print("Напиши 0 чтобы программа прекратила свою работу.\n" \
"Выбери что хочешь делать: 1-надо рандомное число от 3 до 3; 2-разность чисел")
what = input()
if what == "1":
    while 1:
        stoper = input("Напиши что-то чтобы получить число\n")
        if stoper == "0":
            break
        print(f"Рандомное число от 3 до 3: {getNum3("Неважно")}")
elif what == "2":
    while 1:
        a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
        if(a == 0 or b == 0):
            break
        print(f"Разность чисел: {a-b}")
else:
    print("непонятно что")
print("Программа прекратила работу.")    
