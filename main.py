class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id       # Приватный атрибут, инкапсуляция
        self.__name = name             # Приватный атрибут, инкапсуляция
        self.__access_level = 'user'   # Уровень доступа, по умолчанию 'user'

    # Методы для получения доступа к приватным атрибутам
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)  # Наследуем данные от User
        self.__access_level = 'admin'    # Уровень доступа 'admin' для администратора
        self.__user_list = []            # Лист пользователей, которыми управляет администратор

    # Переопределение метода для доступа к уровню администратора
    def get_access_level(self):
        return self.__access_level

    # Метод для добавления пользователя
    def add_user(self, user):
        if isinstance(user, User):  # Проверяем, является ли объект экземпляром User
            self.__user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: можно добавлять только объекты типа User.")

    # Метод для удаления пользователя по ID
    def remove_user(self, user_id):
        for user in self.__user_list:
            if user.get_user_id() == user_id:
                self.__user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    # Метод для отображения всех пользователей
    def display_users(self):
        if self.__user_list:
            print("Список пользователей:")
            for user in self.__user_list:
                print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
        else:
            print("Список пользователей пуст.")

