from typing import TypedDict

from httpx import Response

from clients.api_clients import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса для получения списка заданий.
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры тела запроса для создания задания.
    """
    title: str
    description: str
    maxScore: int
    minScore: int
    courseId: str


class UpdateExerciseRequestDict(TypedDict, total=False):
    """
    Описание структуры тела запроса для обновления задания.
    Поля могут быть частично обновлены, поэтому total=False.
    """
    title: str
    description: str
    maxScore: int
    minScore: int

class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получение списка заданий по курсу.

        :param query: Словарь с courseId.
        :return: Response с данными списка заданий.
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получение информации о задании по его идентификатору.

        :param exercise_id: UUID задания.
        :return: Response с данными задания.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создание нового задания.

        :param request: Словарь с полями задания.
        :return: Response с данными созданного задания.
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Частичное обновление данных задания.

        :param exercise_id: UUID задания.
        :param request: Словарь с обновляемыми полями.
        :return: Response с обновлёнными данными.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаление задания по его идентификатору.

        :param exercise_id: UUID задания.
        :return: Response с результатом удаления.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")