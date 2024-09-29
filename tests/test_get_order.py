import pytest
import requests
import allure


class TestGetOrder:

    @allure.title('Получение заказов')
    def test_get_order(self):
        response = requests.get("https://qa-scooter.praktikum-services.ru/api/v1/orders")
        assert response.status_code == 200
        assert response.json()["orders"]

    @allure.title('Проверка заказа метро Комсомольская')
    def test_get_order(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders?limit=10&page=0&nearestStation=["6"]')
        assert response.status_code == 200
        assert response.json()["orders"][0]["metroStation"] == "6"
