class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.__users = []

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Объект не является пользователем.")

    def remove_user(self, user_id):
        user_to_remove = None
        for user in self.__users:
            if user.get_user_id() == user_id:
                user_to_remove = user
                break

        if user_to_remove:
            self.__users.remove(user_to_remove)
            print(f"Пользователь с ID {user_id} удален.")
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def get_users(self):
        return self.__users


# Пример использования
admin = Admin(user_id=1, name="Админ Иван")
user1 = User(user_id=2, name="Работник Петр")
user2 = User(user_id=3, name="Работник Анна")

admin.add_user(user1)
admin.add_user(user2)

# Печать списка пользователей
for user in admin.get_users():
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

admin.remove_user(user_id=2)

