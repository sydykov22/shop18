
# [obj, c, b, d]

# mro

# Mixins - Примеси

# в конце название хранить Mixin

# PostMixin

# не должен хранить состояние


# from multiprocessing import AuthenticationError


# class CreateMixin:
#     def create(self):
#         print("Create")

# class UpdateMixin:
#     def update(self):
#         print("Update")

# class DeleteMixin:
#     def update(self):
#         print("Delete")


# class CreateRestoran():
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

#     def create_restoran(self):
#         self.create()


# user = {
#     "user1": 123,
#     "user2": 321
# }

# def login_required(func):
#     def wrapper(*args, **kwargs):
#         for x in kwargs.keys():
#             if x not in user.values():
#                 raise AuthenticationError("User in not Authenticated")
#         func()
#         print("Успешно авторизован")
#         return
    
#     return wrapper 

# @login_required
# def some_page(user):
#     pass

# some_page(123)

# class View():
#     def __init__(self) -> None:
#         self.users = []

    # def dispath(self):
    #     print("метод диспатч")
    #     user.users

# class LoginRequiredMixin:
#     def dispath(self):
#         if user not in self.users:
#             raise AuthenticationError("User is not authenticated")
#         return self.users

# class AboutPage(View, LoginRequiredMixin):
#     pass

# obj = AboutPage()
# obj.dispath("test", "anon")


# композиция

# class Author:
#     pass

# class Restoran:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.owner = Author()

# res = Restoran("test", "test")
# print(res.owner.name)
# res.owner.get()




























