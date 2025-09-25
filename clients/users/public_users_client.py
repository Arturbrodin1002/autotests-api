from httpx import Response
from typing import TypedDict
from clients.api_clients import APIClient


class CreateUserRequest(TypedDict):
    """
    Структура входных данных для создания пользователя.

    Attributes:
        email (str): Электронная почта пользователя.
        password (str): Пароль пользователя.
        lastName (str): Фамилия пользователя.
        firstName (str): Имя пользователя.
        middleName (str): Отчество пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    API клиент для работы с публичными методами /api/v1/users,
    которые не требуют авторизации.
    """

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Выполняет POST-запрос для создания пользователя.

        Args:
            request (CreateUserRequest): Данные пользователя для создания,
            включая email, пароль, имя, фамилию и отчество.

        Returns:
            Response: Ответ сервера с результатом выполнения запроса.
        """
        return self.post("/api/v1/users", json=request)