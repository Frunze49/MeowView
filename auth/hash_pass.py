import bcrypt

# Функция для хэширования пароля
def hash_password(password):
    # Генерация соли и хэширование пароля
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
