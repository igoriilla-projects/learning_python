import random


def main():
    counter = 0
    random_number = set_random_number()
    while True:
        counter += 1
        print("Введите число от 1 до 100 включительно:")
        user_number = input()
        if is_valid(user_number):
            if check_number(int(user_number), counter, random_number):
                break
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue


def repeat():
    print("Желаете сыграть еще раз? y = yes, n = no")
    answer = input()
    if answer == 'y':
        main()
    elif answer == 'n':
        print("Спасибо что сыграли, до новых встреч!")
        quit()
    else:
        print("Неизвестный ответ, будет расценен как нет :)")
        quit()


def set_random_number():
    return random.randrange(1, 100)


def is_valid(string):
    if string.isdigit():
        return True
    return False


def check_number(number, counter, random_number):

    if number < random_number:
        print("Ваше число меньше загаданного, попробуйте еще разок...")

        return False
    elif number > random_number:
        print("Ваше число больше загаданного, попробуйте еще разок...")
        return False
    else:
        print("Вы угадали, поздравляем!")
        print("Колисчество попыток:", counter)
        repeat()


print('Добро пожаловать в числовую угадайку!')
main()
