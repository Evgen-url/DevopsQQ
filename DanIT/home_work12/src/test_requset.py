import requests
import sys


# URL локального сервера
BASE_URL = "http://127.0.0.1:5000/users"

def log_result(message, file_path='test.txt'):
    """Логирование результатов в консоль и файл"""
    print(message)
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

def test_rest_api():
    # Очистка файла с результатами
    open('test.txt', 'w').close()

    # 1. Получаем всех пользователей (GET)
    log_result("\n1. Получаем всех пользователей:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Пользователи: {response.json()}")

    # 2. Создание пользователей (POST)
    students = [
        {"name": "qaz", "surname": "zaq", "age": "11"},
        {"name": "qaz1", "surname": "zaq1", "age": "22"},
        {"name": "qaz2", "surname": "zaq2", "age": "33"}
    ]
    
    created_students = []
    log_result("\n2. Создание пользователей:")
    for student in students:
        response = requests.post(BASE_URL, json=student)
        log_result(f"Создан: {response.json()}")
        created_students.append(response.json())
    
    # Получаем ID пользователей
    first_student_id = created_students[0]['id']
    second_student_id = created_students[1]['id']
    third_student_id = created_students[2]['id']

    # 3. Получаем всех пользователей (GET)
    log_result("\n3. Получаем всех пользователей:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Пользователи: {response.json()}")

    # 4. Обновление возраста второго пользователя (PATCH)
    log_result(f"\n4. Обновляем возраст второго пользователя (ID: {second_student_id}):")
    patch_data = {"age": "11"}
    response = requests.patch(f"{BASE_URL}/{second_student_id}", json=patch_data)
    log_result(f"Обновлен: {response.json()}")

    # 5. Получаем информацию о втором пользователе (GET)
    log_result(f"\n5. Получаем второго пользователя (ID: {second_student_id}):")
    response = requests.get(f"{BASE_URL}/{second_student_id}")
    log_result(f"Пользователь: {response.json()}")

    # 6. Обновляем 3-го пользователя (PUT)
    log_result(f"\n6. Обновляем первого пользователя (ID: {third_student_id}):")
    put_data = {"name": "qwerty", "surname": "Ytrewq", "age": "12"}
    response = requests.put(f"{BASE_URL}/{third_student_id}", json=put_data)
    log_result(f"Обновлен: {response.json()}")

    # 7. Получаем первого пользователя (GET)
    log_result(f"\n7. Получаем первого пользователя (ID: {third_student_id}):")
    response = requests.get(f"{BASE_URL}/{third_student_id}")
    log_result(f"Пользователь: {response.json()}")

    # 8. Получаем всех пользователей (GET)
    log_result("\n8. Получаем всех пользователей:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Пользователи: {response.json()}")

    # 9. Удаляем первого пользователя (DELETE)
    log_result(f"\n9. Удаляем первого пользователя (ID: {first_student_id}):")
    response = requests.delete(f"{BASE_URL}/{first_student_id}")
    log_result(f"Удаление: {response.json()}")

    # 10. Получаем всех пользователей (GET)
    log_result("\n10. Получаем всех пользователей:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Пользователи: {response.json()}")

if __name__ == "__main__":
    test_rest_api()
