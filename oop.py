
# """
# Наследование - принцип ООП, где мы можем в дочернем классе унаследовать, 
# переопределять и использовать все методы и аттрибуты родительского класса
# """
# class A:
#     def method(self):
#         print("method is class A")

# class B(A):
#     """Наследовали все методы и аттрибуты у класса А"""

# b = B() # Создали обьект (экземпляр) от класса B
# b.method1() #Может вызывать метод method1, который был создан в классе A

# """
# Полиморфизм - принцип ООП. Мы можем создавать в разных классах
# одноименные методы и аттрибуты с разным функционалом
# """

# class A:
#     def __str__(self) -> str:
#         """
#         метод __str__ работает когда:
#         1. мы оборачиваем обьект в str -> str(A())
#         2. принтим обьект -> print(A())
#         """
#         return "A object"

# class B:
#     def __str__(self):
#         return "B object"

# print(A()) # A 'object'
# print(B()) # B 'object'
# """
# Инкапсуляция - принцип ООП, где мы можем делать атрибуты и методы
# с разным уровнем доступа
# """
# class A:
#     attribute1 = "публичный аттрибут"
#     _attribute2 = "защищенный аттрибут"
#     __attribute3 = "приватный аттрибут (но можно обратиться так: _A__attribute3)"

#     def method1(self):
#         return "публичный метод"

#     def _method2(self):
#         return "защищенный метод"

#     def __method3(self):
#         self.__attribute3
#         return "приватный метод (_A__method3)"

# # A().__attribute3 -> AttributeError
# # A()._A__attribute3 -> "приватный аттрибут (но можно обратиться так: _A__attribute3)"

# """
# Множественное наследование - принцип ООП, в котором мы наследуем 
# все аттрибуты и методы у всех родителей
# """
# class A:
#     def method_a(self):
#         ...

# class B:
#     def method_b(self):
#         ...

# class C(A, B):
#     """Класс унаследовал все аттрибуты и мотоды класса А и 
#     класса B и все аттрибуты и методы их родителей (object)
#     """

# c = C()
# c.method_a()
# c.method_b()

# """Методы множественного наследования"""
# # 1. - Проблема ромба (решена через mro)
# # 2. - Проблема перекрестного наследования (не решена)
# class A:
#     """корневой класс"""

#     def method_a(self):
#         return "A"

# class B(A):
#     """Первый дочерний класс от А"""

#     def method_b(self):
#         return "B"

# class C(B):
#     """Второй дочерний класс от А"""
 
#     def method_c(self):
#         return "C"

# class D(C):
#     """Дочерний класс от А"""

#     def method_c(self):
#         return "D"


# d = D()
# d.method_a()
# d.method_b()
# d.method_c()
# d.method_d()

"""Getters and Setters"""
# это методы, через которые мы можем получить (getter)
# и изменить (setter) значения защищенныз и приватных аттрибутов
