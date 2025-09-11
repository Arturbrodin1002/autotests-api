import grpc
import course_service_pb2
import course_service_pb2_grpc

# Создаем канал до сервера
channel = grpc.insecure_channel("localhost:50051")
stub = course_service_pb2_grpc.CourseServiceStub(channel)

# Отправляем запрос
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))

# Выводим ответ в нужном формате
print(f'course_id: "{response.course_id}"')
print(f'title: "{response.title}"')
print(f'description: "{response.description}"')
