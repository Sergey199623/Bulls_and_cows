import random

STRONG = 5040 #Уровень силы компьютера

# Функция ниже (get_all_answers) создает список всех возможных ответов
def get_all_answers():
    ans = []
    for i in range(10000):
        tmp = str(i).zfill(4) #Здесь i преобразуется в строку и zfill заполняет недостающее значение нулями (4-х значные числа)
        #print(tmp)
        # вариант 1 - множества
    #     if len(set(map(int, tmp))) == 4:  #Функция set преобразует обект в множество (набор не повторяющихся символов)
    #         ans.append(list(map(int, tmp))) #Функция лист создает список
    # #print(ans)

        #вариант 2 - генератор списков
        lst = ['x' for num in tmp if tmp.count(num) == 1] #Переменная tmp внутри цикла for и вытаскиваем из tmp значения
                                                            #и кладем их в переменную num, а функция count проверяет, сколько раз встречается значение в num
        if len(lst) == 4:
            ans.append(list(map(int, tmp)))
    #print(ans)
    return ans


# Функция ниже (get_one_answer) позволяет выбирать один ответ из всех возможных
def get_one_answer(ans):
    num = random.choice(ans) #Функция на вход получает несколько значений и кладет в переменную num и выбирает оттуда случайное значение
    return num

# Функция ниже (input_number) будет общаться с пользователем и будет получать от него ответ
def input_number():
    while True:
        nums = input("Введите 4 неповторяющихся числа: ") #Сюда пользователь вводит значение
        if len(nums) != 4 or not nums.isdigit(): #Проверяем, введены ли 4 числа или вообще не цифры
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums

# Функция ниже (check) сравнивает два числа и сообщает количество быков и коров
def check(nums, true_nums):
    bulls, cows = 0, 0
    for i, num in enumerate(nums): #В данном цикле i - счетчик, а num - как содержимое переменной nums
        if num in true_nums: #Если наша цифра входит в список истинных цифр (true_nums)
            if nums[i] == true_nums[i]: #Если i в nums на той же позиции, что и в true_nums, то бык
                bulls += 1
            else:
                cows += 1

    return bulls, cows

# Функция ниже (del_bad_answer) анализирует ответы и решает, что надо запомнить или удалить
def del_bad_answers(ans, enemy_try, bull, cow):
    i = 0
    for num in ans[:]:
        i += 1
        temp_bull, temp_cow = check(num, enemy_try)
        if temp_bull != bull or temp_cow != cow:
            ans.remove(num)
        if i > STRONG:
            break
    return ans


if  __name__ == '__main__':
    STRONG = 1008  #Выставление "мощи" компьютера (Уровень сложности)
    print("Игра Быки и Коровы")
    answers = get_all_answers()         #Всевозможные варианты
    player = input_number()             #число которое загадал игрок
    enemy = get_one_answer(answers)      #число которое загадал компьютер

    while True:
        print('=' * 15, 'Ход игрока', '=' * 15)
        print('Угадайте число компьютера')
        number = input_number() #Здесь пользователь угадывает число компьютера
        bulls, cows = check(number, enemy)
        print('Быки: ', bulls, 'Коровы: ', cows)
        if bulls == 4:
            print('Победил игрок')
            print('Компьютер загадал число: ', enemy)
            break

        print('=' * 15, 'Ход компьютера', '=' * 15)
        enemy_try = get_one_answer(answers)
        print('Компьютер считает, что вы загадали число ', enemy_try)
        print('В памяти ', len(answers), ' вариантов')
        bulls, cows = check(enemy_try, player)
        print('Быки: ', bulls, 'Коровы: ', cows)
        if bulls == 4:
            print('Победил компьютер')
            print('Компьютер загадал число: ', enemy)
            break
        else:
            answers = del_bad_answers(answers, enemy_try, bulls, cows)

