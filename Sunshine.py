#Задание№3
# Напишите функцию, которая принимает возраст собаки и нужно вычислить, возраст собаки в человеческих годах.(В течение первых двух лет собачий год равен 10.5 человеческим годам. После этого каждый год собаки равен 4 человеческим годам).

# x = int(input('->'))
# def age():
#     age = 10.5
#     age_2 = 4
#     if x<= 2:
#         print(x*age)
#     else:
#         print(2*age + x*age_2)
# age()
#ЗАдание№4
# N = 19
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1.
# Output: true
# N = 2;
# Output: false
# def happy(n):
#     numbers = list(filter(bool, map(int, str(n)))) #
#     res = sum(i*i for i in numbers)
#     if res == 1:
#         return True
#     elif len(numbers) == 1:
#         return False
#     return happy(res)
#
# print(happy(19))
#Задание№6
# ПрИмЕрЫ:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
# to_weird_case('This') # => returns 'ThIs'
# to_weird_case('is') # => returns 'Is'
# to_weird_case('This is a test') # => returns 'ThIs Is A TeSt'

# def to_weird_string(string):
#     result = ""
#     for index in range(len(string)) :
#         if index % 2 == 0 :
#             result += string[index].upper()
#         else :
#             result += string[index].lower()
#     return result
#
# print(to_weird_string("Weird string case"))
#Задание№5
# примеры:
# title_case('a clash of KINGS', 'a an the of') #
# должен вернуть: 'A Clash of Kings'
#
# title_case('THE WIND IN THE WILLOWS', 'The In') #
# должен вернуть: 'The Wind in the Willows'
#
# title_case('the quick brown fox') #
# должен вернуть: 'The Quick Brown Fox'


# def title_case(title, minor_words = ''):
#     new_title = []
#     new_minor_words = [word.lower() for word in minor_words.split(' ')]
#     if not len(title):
#         return title
#     for index, word in enumerate(title.split(' ')):
#         if index == 0:
#             new_title.append(word.title())
#             continue
#
#         if word.lower() in new_minor_words:
#             new_title.append(word.lower())
#             continue
#
#         new_title.append(word.title())
#
#     return ' '.join(new_title)
#
# print(title_case('a clash of KINGS', 'a an the of'))
# print(title_case('THE WIND IN THE WILLOWS', 'The In'))
# print(title_case('the quick brown fox'))

# 1. Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение.

# def func():
#     file = input('->')
#     if '.' in file[1:-1]:
#         print(file[file.rfind('.'):])
#     else:
#         except Exception(''):
#     return file
# func()
# 2. Напишите функцию, которая принимает год и определяет, является ли год с данным номером високосным. Если год является високосным, то возвращает «YES», иначе возвращает «NO».Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.

# def func():
#     a = int(input('Введите год :'))
#
#     if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#         print('YES')
#     else:
#         print('NO')
# func()

# 7. ваша задача — создать функцию, которая превращает строку в мексиканскую волну. Вам будет передана строка, и вы должны вернуть эту строку в виде массива, где заглавная буква означает стоящего человека (https://ru.wikipedia.org/wiki/Волна_(стадион).
#
# Правила:
# 1. Строка ввода всегда будет строчной, но может быть и пустой.
# 2. Если символ в строке является пробелом, пропустите его, как если бы это было пустое место.


# def wave(word):
#     words = []
#     for num,num1 in enumerate(word):
#         if num1 == ' ':
#             pass
#         else:
#             new = list(word)
#             new[num] = new[num].upper()
#             new = ''.join(new)
#             words.append(new)
#     return(words)
#
# print(wave(input('->')))