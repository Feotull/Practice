# адача "Распаковка":
#
# 1.Функция с параметрами по умолчанию:
#
def print_params (a = 1, b = "строка", c = True): # Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
    print(a, b, c) # Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(7, None, False)
print_params(b = "jgkfl", c = None)
print_params("привет", 367483)
print_params()
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = "25")
print_params(c = [1,2,3])

# 2.Распаковка параметров:
#
# Создайте список values_list с тремя элементами разных типов.
values_list = ["My year of birth is", 1987, True]
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict = {'a': 26, 'b': "октября", 'c': False}
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
#
# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [54.32, 'Строка']
# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
# Пример результата выполнения программы:
#
# Исходный код:
#
# values_list_2 = [54.32, 'Строка' ]
#
# print_params(*values_list_2, 42)
#
# Вывод на консоль:
#
# 54.32 'Строка' 42