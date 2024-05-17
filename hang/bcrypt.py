import hashlib
import os

def hash_password(password):
    # Генерируем случайную соль
    salt = os.urandom(32)  # 32 байта для соли

    # Конвертируем пароль в байтовую строку
    password_bytes = password.encode('utf-8')

    # Добавляем соль к паролю и хешируем результат
    hashed_password = hashlib.sha256(salt + password_bytes).hexdigest()

    return hashed_password, salt

def check_password(password, hashed_password, salt):
    # Конвертируем пароль в байтовую строку
    password_bytes = password.encode('utf-8')

    # Проверяем соответствие хэша
    return hashed_password == hashlib.sha256(salt + password_bytes).hexdigest()

# # Пример использования:
# if __name__ == "__main__":
#     # Пользователь вводит пароль
#     user_password = input("Введите пароль: ")

#     # Хешируем пароль
#     hashed_password, salt = hash_password(user_password)

#     print("Хэш пароля:", hashed_password)
#     print("Соль:", salt)

#     # Пользователь вводит пароль для проверки
#     login_password = input("Введите пароль для проверки: ")

#     # Проверяем пароль
#     if check_password(login_password, hashed_password, salt):
#         print("Пароль верный!")
#     else:
#         print("Неверный пароль!")
