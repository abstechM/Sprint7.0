import pytest
import requests
import allure


class TestMakeOrder:
    @pytest.mark.parametrize("color_sam", ["GREY", "BLACK", "GREY, BLACK"])
    @allure.title("Создание успешного заказа с цветом {color_sam}")
    def test_success_order(self, color_sam):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                f"{color_sam}"
            ]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)
        print(response.status_code)
        print(response.json()['track'])
        assert response.status_code == 201
        assert response.json()['track']

    @allure.title("Создание успешного заказа без цвета")
    def test_success_order_without_color(self):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)
        print(response.status_code)
        print(response.json()['track'])
        assert response.status_code == 201
        assert response.json()['track']