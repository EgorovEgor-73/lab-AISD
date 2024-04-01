# 1 лаба
'''
print("Четырехзначных чисел, меньших 1024 и у которых вторая справа цифра не существует.")
Нечетные четырехричные числа, не превышающие 102410, у которых вторая справа цифра равна 3. 
Выводит на экран цифры числа, исключая тройки. Вычисляется среднее число между минимальным и максимальным и выводится прописью.

'''

def replace_letter(s):
    for symb in s:
        if (symb.isdigit()) or symb == "-":
            continue
        else:
            s = s.replace(symb, " ")
    s = s.split()
    res1 = []
    for i in s:
        try:
            x = int(i)
            res1.append(x)
        except:
            continue
    return res1

d = {'0': 'ноль',
     '1': 'один',
     '2': 'два',
     '3': 'три',
     '4': 'четыре',
     '5': 'пять',
     '6': 'шесть',
     '7': 'семь',
     '8': 'восемь',
     '9': 'девять'}

min_ = 10 ** 19
max_ = -10 ** 19
res = []

f = open("C:/Users/LarinDJ/Downloads/text.txt", "r")
while True:
    s = f.readline()
    s1 = replace_letter(s)
    
    if not s:
        print("\nФайл закончился")
        break
    else:
        try:
            if s1 != []:
                for x in s1:
                    if abs(x) < 1025 and ((x // 10) % 10) == 3 and len(str(abs(x))) == 4:
                        res.append(x)
        except:
            continue
if len(res) > 0:
    print("Список чисел, удовлетворяющих условию: ",res)
    min_ = min(res)
    max_ = max(res)
    
    print("Цифры чисел, исключая тройки:")
    for num in res:
        num1 = str(num)
        print(''.join([digit for digit in str(abs(num)) if digit != '3']))
        
    avg_ = (min_ + max_) // 2
    avg_ = ' '.join([d[digit] for digit in str(abs(avg_))])
    print(f"Среднее число между минимальным ({min_}) и максимальным ({max_}): {avg_}")

else:
    print("Нет чисел для обработки.")

f.close()
