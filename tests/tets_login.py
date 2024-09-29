import pytest
import requests
import allure
from faker import Faker

faker = Faker()

class TestLogin:
    @allure.title('Успешный логин курьера')
    def test_login_success(self):
        # генерируем логин, пароль и имя курьера
        login = faker.word()
        password = faker.word()
        first_name = faker.first_name()

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        payload_login = {
            "login": login,
            "password": password,
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = payload)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data = payload_login)
        print(response.status_code)
        print(response.text)
        assert response.status_code == 200
        assert response.json()['id']

        requests.delete(f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{response.json()['id']}")

    @pytest.mark.parametrize("login_c", [{"login": faker.word(),"password": "123445", "firstName": faker.first_name()},
                                         {"login": "Suprer","password": faker.word(), "firstName": faker.first_name()}])
    @allure.title('Введен не верный пароль/логин')
    def test_wrong_psw_login(self, login_c):

        first_name = faker.first_name()
        # собираем тело запроса
        payload = {
            "login": 'Super',
            "password": '123445',
            "firstName": first_name
        }
        payload_login = login_c
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = payload)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data = payload_login)
        print(response.status_code)
        print(response.text)
        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"


    @allure.title('Логин курьера без логина')
    def test_without_login(self):
        # генерируем логин, пароль и имя курьера
        login = faker.word()
        password = faker.word()
        first_name = faker.first_name()

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        payload_login = {
            "password": password,
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = payload)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data = payload_login)
        print(response.status_code)
        print(response.text)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для входа"


    @allure.title('Логин курьера без пароля')
    def test_without_psw(self):
        # генерируем логин, пароль и имя курьера
        login = faker.word()
        password = faker.word()
        first_name = faker.first_name()

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        payload_login = {
            "login": login
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = payload)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data = payload_login)
        print(response.status_code)
        print(response.text)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для входа"
