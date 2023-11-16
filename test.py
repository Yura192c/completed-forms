import httpx

api_url = "http://localhost:8000"


def test_existing_form():
    response = httpx.post(
        f"{api_url}/get_form?user_name=John&user_email=a@gmail.ru&user_password=123qwerty&user_date_of_birth=11.12.2003")
    assert response.status_code == 200
    assert response.json() == {"template_name": "User registration form"}


def test_non_existing_form():
    response = httpx.post(f"{api_url}/get_form?user_name=John&user_email=a@gmail.ru&user_password=123qwerty")
    assert response.status_code == 200
    assert response.json() == {"user_name": "text",
                               "user_email": "email",
                               "user_password": "text"}


def test_additional_fields():
    response = httpx.post(
        f"{api_url}/get_form?user_name=John&user_email=a@gmail.ru&user_password=123qwerty&user_date_of_birth=11.12.2003&ord_email=rr@gmail.ru")
    assert response.status_code == 200
    assert response.json() == {"template_name": "User registration form"}


def test_add_template():
    new_template_data = {
        "field_name_1": "email",
        "field_name_2": "text"
    }
    response = httpx.post(f"{api_url}/add_template", json=new_template_data)
    assert response.status_code == 200
    assert "template_id" in response.json()


def run_tests():
    print("Running tests...")
    test_add_template()
    test_existing_form()
    test_non_existing_form()
    test_additional_fields()
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
