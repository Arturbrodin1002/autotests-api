import httpx


data = {
  "email": "user@example.com",
  "password": "string"
}

response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=data)
headers = {"Authorization": f"Bearer {response.json()['token']['accessToken']}"}

get_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(get_response.json())
print(get_response.status_code)