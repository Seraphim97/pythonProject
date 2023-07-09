import requests
import pytest
from bs4 import BeautifulSoup

def test_sign_up_page_status_code():
    response = requests.get("http://sok-test-task.alexon.tech/sign_up.php")
    assert response.status_code == 200

def test_sign_up_page_content():
    response = requests.get("http://sok-test-task.alexon.tech/sign_up.php")
    assert "Sign Up" in response.text

def test_invalid_credentials():

    data = {
        "email": "serafim@gmail.com",
        "password": "12345"
    }

    response = requests.post("http://sok-test-task.alexon.tech/sign_up.php", data=data)
    assert response.status_code == 200
    # assert "Username or password is incorrect. Try again" in response.text


def test_valid_credentials():
    data = {
        "email": "е",
        "password": "е"
    }

    response = requests.post("http://sok-test-task.alexon.tech/sign_up.php", data=data)
    assert response.status_code == 200
    # assert "Successful login message" in response.text



def test_about_page_status_code():
    response = requests.get("http://sok-test-task.alexon.tech/about.php")
    assert response.status_code == 200

def test_about_page_content():
    response = requests.get("http://sok-test-task.alexon.tech/about.php")
    assert "About" in response.text


def test_successful_registration():
    data = {
        "email": "11",
        "password": "1"
    }

    response = requests.post("http://sok-test-task.alexon.tech/register.php", data=data)
    assert response.status_code == 200
    # assert "Successful registration message" in response.text



if __name__ == "__main__":
    pytest.main()


