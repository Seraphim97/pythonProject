import requests
import pytest

def test_api():
    url = "https://automationexercise.com/api/productsList"
    response = requests.get(url)

    assert response.status_code == 200
    assert 'products' in response.json()
    products = response.json()['products']
    assert len(products) > 0
    # assert response.json() is not None
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"


def test_post_request():
    url = "https://automationexercise.com/api/productsList"
    response = requests.post(url)

    assert response.status_code == 200
    expected_message = "This request method is not supported."
    assert expected_message in response.json().values()

def test_get_brands_list():
    url = "https://automationexercise.com/api/brandsList"
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json() is not None
    assert 'brands' in response.json()
    brands = response.json()['brands']
    assert len(brands) > 0



def test_put_request():
    url = "https://automationexercise.com/api/brandsList"
    response = requests.put(url)
    assert response.status_code == 200
    expected_message = '{"responseCode": 405, "message": "This request method is not supported."}'
    assert response.text == expected_message


def test_search_product():
    url = "https://automationexercise.com/api/searchProduct"
    search_product = "top"

    payload = {
        "search_product": search_product
    }

    response = requests.post(url, data=payload)

    assert response.status_code == 200
    assert response.json() is not None
    search_product = response.json()
    assert 'products' in search_product





def test_search_product_missing_parameter():
    url = "https://automationexercise.com/api/searchProduct"
    response = requests.post(url)
    assert response.status_code == 200
    expected_message = '{"responseCode": 400, "message": "Bad request, search_product parameter is missing in POST request."}'
    assert response.text == expected_message


def test_verify_login():
    url = "https://automationexercise.com/api/verifyLogin"
    email = "email"
    password = "password"

    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(url, data=payload)
    assert response.status_code == 200
    expected_message = '{"responseCode": 404, "message": "User not found!"}'
    assert response.text == expected_message


def test_verify_login_missing_email():
    url = "https://automationexercise.com/api/verifyLogin"
    password = "password"

    payload = {
        "password": password
    }

    response = requests.post(url, data=payload)
    assert response.status_code == 200
    expected_message = '{"responseCode": 400, "message": "Bad request, email or password parameter is missing in POST request."}'
    assert response.text == expected_message


def test_verify_login_delete():
    url = "https://automationexercise.com/api/verifyLogin"
    response = requests.delete(url)
    assert response.status_code == 200
    expected_message = '{"responseCode": 405, "message": "This request method is not supported."}'
    assert response.text == expected_message


def test_verify_login_invalid_credentials():
    url = "https://automationexercise.com/api/verifyLogin"
    email = "invalid@gmail.com"
    password = "password"

    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(url, data=payload)
    assert response.status_code == 200
    expected_message = '{"responseCode": 404, "message": "User not found!"}'
    assert response.text == expected_message


def test_create_account():
    url = "https://automationexercise.com/api/createAccount"
    payload = {
        "name": "Serafim Savichev",
        "email": "savichevserafim@gmail.com",
        "password": "serafim777",
        "title": "Mr",
        "birth_date": "06",
        "birth_month": "01",
        "birth_year": "1997",
        "firstname": "Serafim",
        "lastname": "Savichev",
        "company": "cp Company",
        "address1": "adress",
        "address2": "adress2",
        "country": "Estonia",
        "zipcode": "12345",
        "state": "Harjumaa",
        "city": "Tallinn",
        "mobile_number": "111111"
    }

    response = requests.post(url, data=payload)
    assert response.status_code == 200
    response_body = response.json()
    expected_message = '{"responseCode": 400, "message": "Email already exists!"}'
    assert response.text == expected_message





def test_delete_account():
    url = "https://automationexercise.com/api/deleteAccount"
    email = "serafim888@gmail.com"
    password = "password"

    payload = {
        "email": email,
        "password": password
    }

    response = requests.delete(url, data=payload)

    assert response.status_code == 200
    expected_message = '{"responseCode": 404, "message": "Account not found!"}'
    assert response.text == expected_message


def test_update_account():
    url = "https://automationexercise.com/api/updateAccount"
    payload = {
        "name": "Serafim",
        "email": "serafim@gmail.com",
        "password": "newpassword123",
        "title": "Mr",
        "birth_date": "01",
        "birth_month": "06",
        "birth_year": "1997",
        "firstname": "Serafim",
        "lastname": "Savichev",
        "company": "Company",
        "address1": "address1",
        "address2": "address2",
        "country": "Estonia",
        "zipcode": "12345",
        "state": "Harjumaa",
        "city": "Tallinn",
        "mobile_number": "123456"
    }

    response = requests.put(url, data=payload)
    assert response.status_code == 200
    expected_message = '{"responseCode": 404, "message": "Account not found!"}'
    assert response.text == expected_message



def test_get_user_detail_by_email():
    url = "https://automationexercise.com/api/getUserDetailByEmail"
    email = "serafim@gmail.com"
    params = {
        "email": email
    }

    response = requests.get(url, params=params)
    assert response.status_code == 200
    assert response.json() is not None
    user_detail = response.json()
    assert "user" in user_detail, "Response does not contain 'user' key"



def test_total_price_in_cart():
    url = "https://www.automationexercise.com/view_cart"
    payload = {
        'product_id': '2',
        'quantity': 4,
        'price': 1600

    }
    response = requests.post(url, data=payload)
    assert response.status_code == 403


def test_delete_product_from_cart():
    url = "https://www.automationexercise.com/view_cart"
    response = requests.delete(url)
    assert response.status_code == 403


def test_check_products_categories():
    url = "https://www.automationexercise.com/category_products/1"

    response = requests.get(url)
    assert response.status_code == 200
    category = response.text
    assert 'category' in response.text


def test_product_details():
    url = "https://www.automationexercise.com/product_details/3"
    response = requests.get(url)
    assert response.status_code == 200
    assert 'Availability' in response.text
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"




def test_positive_login():
    url = "https://www.automationexercise.com/login"

    email = "savichevserafim@gmail.com"
    password = "serafim777"

    payload = {
        "email": 'savichevserafim@gmail.com',
        "password": 'serafim111'
    }

    response = requests.post(url, data=payload)
    assert response.status_code == 403



def test_negative_login():
    url = "https://www.automationexercise.com/login"

    email = "serafim@gmail.com"
    password = "serafim777"

    payload = {
        "email": 'savichevserafim@gmail.com',
        "password": 'serafim1111'
    }

    response = requests.post(url, data=payload)
    assert response.status_code == 403


if __name__ == "__main__":
    pytest.main()