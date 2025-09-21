import httpx
from tools.fakers import generate_fake_email

data = {
  "email": f"{generate_fake_email()}",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
# Создание пользоваетля
response = httpx.post("http://localhost:8000/api/v1/users", json=data)
create_user_response_data = response.json()
print(f"create user status code {response.status_code}" )

#Аутентификация
login_data = {
  "email": data['email'],
  "password": data['password']
}

response_login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_data)
login_response_data = response_login.json()
print(f"auth status code {response_login.status_code}")

#Обновление
patch_data = {
  "email": f"{generate_fake_email()}",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
put_user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

response_patch = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}", headers=put_user_headers, json=patch_data)
print(f"patch status code {response_patch.status_code}")
