# Данные для курьеров
valid_courier = {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
}

invalid_courier_missing_login = {
    "password": "test_password",
    "firstName": "test_firstName"
}

invalid_courier_missing_password = {
    "login": "test_login",
    "firstName": "test_firstName"
}

invalid_courier_missing_firstName = {
    "login": "test_login",
    "password": "test_password"
}

duplicate_courier = {
    "login": "test_login",
    "password": "test_password",
    "firstName": "test_firstName"
}

existing_login_payload = {
    "login": "test_login",
    "password": "newpassword",
    "firstName": "newFirstName"
}

# Базовый словарь заказа
base_order = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}

# Создание различных заказов путем обновления базового словаря
order_with_color_BLACK = base_order.copy()
order_with_color_BLACK["color"] = ["BLACK"]

order_with_color_GREY = base_order.copy()
order_with_color_GREY["color"] = ["GREY"]

order_with_colors_BOTH = base_order.copy()
order_with_colors_BOTH["color"] = ["BLACK", "GREY"]

order_without_color = base_order.copy()
order_without_color.pop("color")

# Данные для списка заказов
orders_list_response = {
    "orders": [
        {
            "id": 4,
            "courierId": None,
            "firstName": "ваыпывп",
            "lastName": "ывпывп",
            "address": "пывпывп",
            "metroStation": "2",
            "phone": "423424234432",
            "rentTime": 4,
            "deliveryDate": "2020-06-21T21:00:00.000Z",
            "track": 400443,
            "color": [
                "BLACK",
                "GREY"
            ],
            "comment": "ываимм",
            "createdAt": "2020-06-21T13:21:30.067Z",
            "updatedAt": "2020-06-21T13:21:30.067Z",
            "status": 0
        },
        {
            "id": 5,
            "courierId": None,
            "firstName": "вфцфвц",
            "lastName": "вфцвфцв",
            "address": "вфцвфцвфц",
            "metroStation": "4",
            "phone": "1441412414",
            "rentTime": 4,
            "deliveryDate": "2020-06-08T21:00:00.000Z",
            "track": 189237,
            "color": [
                "BLACK",
                "GREY"
            ],
            "comment": "вфцвфцвфцв",
            "createdAt": "2020-06-21T13:23:09.404Z",
            "updatedAt": "2020-06-21T13:23:09.404Z",
            "status": 0
        }
    ],
    "pageInfo": {
        "page": 0,
        "total": 3,
        "limit": 2
    },
    "availableStations": [
        {
            "name": "Черкизовская",
            "number": "2",
            "color": "#D92B2C"
        },
        {
            "name": "Преображенская площадь",
            "number": "3",
            "color": "#D92B2C"
        },
        {
            "name": "Сокольники",
            "number": "4",
            "color": "#D92B2C"
        }
    ]
}

orders_list_not_found_response = {
  "message": "Курьер с идентификатором {courierId} не найден"
}

orders = [
    {
        "order_id": 1,
        "courier_id": 213
    },
    {
        "order_id": 2,
        "courier_id": 214
    }
]

class ResponseMessages:
    COURIER_CREATED = {"message": "Курьер успешно создан"}
    MISSING_COURIER_ID = {"message": "Недостаточно данных для поиска"}
    INVALID_COURIER_ID = {"message": "Курьера с таким id не существует"}
    MISSING_ORDER_ID = {"message": "Недостаточно данных для поиска"}
    INVALID_ORDER_ID = {"message": "Заказа с таким id не существует"}
