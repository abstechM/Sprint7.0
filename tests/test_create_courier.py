import pytest
import requests
import allure
from faker import Faker


faker = Faker()
class TestCourier:
    @allure.title("Проверка создания Курьера")
    def test_success_create(self):
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
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = payload)
        print(response.status_code)
        assert 201 == response.status_code
        assert response.json()["ok"] == True



    @allure.title('Проверка на создание такого же курьера')
    def test_double_create(self):
        login = faker.word()
        password = faker.word()
        first_name = faker.first_name()

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = payload)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = payload)
        print(response.status_code)
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
        assert response.status_code == 409


    @pytest.mark.parametrize("method", [{"password": faker.word(),"firstName": faker.first_name()},
                                        {"login": faker.word(),"firstName": faker.first_name()}])
    @allure.title("Проверка создания Курьера без {method}")
    def test_without_login_psw(self, method):
        # собираем тело запроса
        payload = method
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        print(response.status_code)
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
        assert response.status_code == 400