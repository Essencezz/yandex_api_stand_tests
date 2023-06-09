import sender_stand_request
import data

# Функция для позитивной проверки
def positive_assert(first_name):
    # В переменную user_body сохраняется обновленное тело запроса
    user_body = get_user_body(first_name)
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    user_response = sender_stand_request.post_new_user(user_body)

    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert user_response.json()["authToken"] != ""

    # В переменную users_table_response сохраняется результат запроса на получение данных из таблицы user_model
    users_table_response = sender_stand_request.get_users_table()

    # Строка, которая должна быть в ответе
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Проверка, что такой пользователь есть, и он единственный
    assert users_table_response.text.count(str_user) == 1

    #Test5.
    def test_create_user_english_letter_in_first_name_get_success_response():
        positive_assert("QWErty")

    # Test6.
    def test_create_user_english_letter_in_first_name_get_success_response():
        positive_assert("Мария")

    # Тест 11. Ошибка
    # Параметр fisrtName состоит из пустой строки
    def test_create_user_empty_first_name_get_error_response():
        # В переменную user_body сохраняется обновлённое тело запроса
        user_body = get_user_body("")
        # Проверка полученного ответа
        negative_assert_no_firstname(user_body)
