#Задание№3
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

# def weird_string(string):
#     result = ""
#     for index in range(len(string)) :
#         if index % 2 == 0 :
#             result += string[index].upper()
#         else :
#             result += string[index].lower()
#     return result
#
# print (weird_string("Weird string case"))



