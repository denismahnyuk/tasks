"""
Есть класс User, необходимо чтобы пример кода ниже отрабатывал без ошибок
и выводил соответствующие значения. Задача в том, чтобы правильно реализовать
классс User c доп. возможностью обращаться по ключу к существующим
атрибутам класса, в случае если же такого атрибута по ключу не существует
у объекта, то возвращать None.
"""

class User:
    def __getitem__(self, key: str):
        return getattr(self, key, None)


user1 = User()
user1.name = "John"
user1.age = 25

print(user1.name)  # John
print(user1.age)  # 25
print(user1.email)  # exception: AttributeError

print(user1["name"])  # John
print(user1["age"])  # 25
print(user1["email"])  # None
